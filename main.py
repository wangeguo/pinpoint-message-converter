#!/usr/bin/python3

import json
import os
import traceback
from logging.config import dictConfig
from typing import List

from flask import Flask, make_response, request
from redis import Redis

from parse import get_trace_id, is_span, parse
from point import Point, PointEncoder
from request import Request;
import span
import span_chunk

#from datakit_framework import DataKitFramework

# Define a abstract class DataKitFramework for mock.
# it's has a abstract method run() to do the real work.
# and also has two attributes: name and interval.
class DataKitFramework:
    name = "DataKitFramework"
    interval = 10

    def run(self):
        pass

# Setup logging level and format
dictConfig({
    'version': 1,
    'root': {
        'level': os.getenv('PMC_LOG_LEVEL', 'DEBUG'),
    }
})

debug_mode = os.getenv('PMC_DEBUG', True)

# Create Flask application instance
app = Flask(__name__)

# extend DataKitFramework class and override run() method.
class PinpointMessageConverter(DataKitFramework):
    name = "PinpointMessageConverter"
    interval = 10

    def run(self):
        try:
            # Setup redis client to app context
            app.logger.debug("Creating Redis client")
            redis_host = os.getenv('PMC_REDIS_HOST', 'localhost')
            redis_password = os.getenv('PMC_REDIS_PASSWORD', '')
            redis_port = os.getenv('PMC_REDIS_PORT', 6379)
            redis_db = os.getenv('PMC_REDIS_DB', 0)
            redis = Redis(host=redis_host, port=redis_port,
                            db=redis_db, password=redis_password,
                            socket_connect_timeout=5, socket_timeout=5)

            with app.app_context():
                app.redis = redis

            # Start flask server
            app.run(host='0.0.0.0', port=os.getenv('PMC_PORT', 38064), debug=False)
        except Exception as e:
            redis.close()
            app.logger.error("Run error: {} {}".format(str(e), traceback.format_exc()))

# Handle http request
@app.route("/", methods=['POST'])
def handle():
    try:
        # convert the raw request data (bytes) if debug mode,
        # otherwise convert the request data by Request object list (JSON).
        lines = []

        if debug_mode:
            lines.extend(convert(app.redis, request.data))
        else:
            # parse the request data to Request object list (JSON)
            requests = json.loads(request.data, object_hook=lambda d: Request(**d))
            for req in requests:
                lines.extend(convert(app.redis, req.value))

        response = make_response(json.dumps(lines, cls=PointEncoder), 200)
        response.headers['Content-Type'] = 'application/json'
        response.headers['X-category'] = 'tracing'

        return response
    except Exception as e:
        app.logger.error("Handle error: {} {}".format(str(e), traceback.format_exc()))

    return make_response('', 200)

# Parse message, parse message body to thrift struct,
# convert to JSON object and return as line protocol.
def convert(redis: Redis, message: bytes) -> List[Point]:
    app.logger.debug('Received message: {}'.format(message))

    # Check message header and parse message body to thrift struct,
    struct = parse(message)

    TRACE_ID_KEY = os.getenv('PMC_TRACE_ID_KEY', 'x-b3-traceid')
    trace_id = get_trace_id(struct, redis, TRACE_ID_KEY)

    if is_span(struct):
        lines = span.encode(struct, trace_id)
    else:
        lines = span_chunk.encode(struct, trace_id)

    app.logger.debug(json.dumps(lines, cls=PointEncoder))
    return lines

# Start PinpointMessageConverter for test.
if __name__ == '__main__':
    PinpointMessageConverter().run()
