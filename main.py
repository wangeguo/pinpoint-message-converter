#!/usr/bin/python3

import json
import os
from ddtrace import DDSpanEncoder
from parse import get_trace_id, parse;
from confluent_kafka import Consumer, KafkaError
from pinpoint.thrift.Apptrace.ttypes import TSpan
from redis import Redis
import traceback
import logging
import requests
import span
import span_chunk

HTTP_HEADERS = {'Content-Type': 'application/json; charset=utf-8'}

# Setup logging level and format
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s %(levelname)s %(message)s')

TRACE_ID_KEY = os.getenv('TRACE_ID_KEY', 'x-b3-traceid')

# Parse message, parse message body to thrift struct, convert to JSON object,
# and send to DataKit DDtrace Collector
def handle(endpoint: str, redis: Redis, message: bytes):
    # Check message header and parse message body to thrift struct,
    # convert to JSON If message is valid.
    struct = parse(message)
    trace_id = get_trace_id(struct, redis, TRACE_ID_KEY)

    if isinstance(struct, TSpan):
        trace = span.encode(struct, trace_id)
    else:
        trace = span_chunk.encode(struct, trace_id)

    payload = json.dumps([trace], cls=DDSpanEncoder)
    logging.debug("Payload: {}".format(payload))

    # Send JSON to DataKit DDtrace Collector
    r = requests.post(endpoint, data=payload, headers=HTTP_HEADERS)
    logging.debug("Response: {}".format(str(r)))

    return r

def main():
    try:
        # Create Kafka Consumer with topic and bootstrap server
        logging.debug("Creating Kafka Consumer with topic and bootstrap server")
        kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
        kafka_group_id = os.getenv('KAFKA_GROUP_ID', 'pinpoint-message-convertor')
        kafka_consumer_offset_reset = os.getenv('KAFKA_CONSUMER_OFFSET_RESET', 'latest')

        # When using a Kafka 0.10 broker or later you don't need to do anything
        # (api.version.request=true is the default). If you use Kafka broker 0.9 or 0.8
        # you must set api.version.request=false and set broker.version.fallback to
        # your broker version, e.g broker.version.fallback=0.9.0.1.
        broker_version = os.getenv('BROKER_VERSION', '0.9.0.1')
        api_version_request = os.getenv('API_VERSION_REQUEST', True)

        consumer = Consumer({
            'bootstrap.servers': kafka_bootstrap_servers,
            'group.id': kafka_group_id,
            'auto.offset.reset': kafka_consumer_offset_reset,
            'auto.commit.enable': True,
            'enable.auto.commit': True,
            'broker.version.fallback': broker_version,
            'api.version.request': bool(api_version_request),
        })
        kafka_topics = os.getenv('KAFKA_TOPICS', 'SpanTopic')
        consumer.subscribe(kafka_topics.split(','))

        # Create Redis client
        logging.debug("Creating Redis client")
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_password = os.getenv('REDIS_PASSWORD', '')
        redis_port = os.getenv('REDIS_PORT', 6379)
        redis_db = os.getenv('REDIS_DB', 0)
        redis = Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)

        datakit_address = os.getenv('DATAKIT_ADDRESS', 'localhost:9529')

        # localhost:9529/v0.4/traces
        endpoint = "http://{}/v0.4/traces".format(datakit_address)

        # Consume Kafka message and send to DataKit Pinpoint Collector
        while True:
            message = consumer.poll(1.0)

            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    logging.error("Consumer error: {}".format(message.error()))
                    continue

            logging.debug('Received message: {}'.format(message.value()))

            try:
                handle(endpoint, redis, message.value())
                consumer.commit()
            except Exception as e:
                logging.error("Handle error: {} {} {}".format(type(e), str(e), traceback.format_exc()))
                continue
    except Exception as e:
        consumer.close()
        redis.close()
        logging.error("Error: {} {}".format(str(e), traceback.format_exc()))

# Run main function in loop to prevent process exit
if __name__ == '__main__':
    while True:
        main()
