#!/usr/bin/python3

import os
import grpc
from parse import parse;
import pinpoint.protobuf.Service_pb2_grpc as rpc
from confluent_kafka import Consumer, KafkaError
from pinpoint_parser import xid
from utils import extract_trace_id
from redis import Redis

# Parse message, parse message body to thrift struct, convert to protobuf struct, and send to DataKit Pinpoint Collector
def handle(stub: rpc.SpanStub, redis: Redis, message: bytes):
    thrift_struct, protobuf_struct = parse(message)

    trace_id = None
    tid = xid(thrift_struct.transactionId, thrift_struct.appId, thrift_struct.agentId)
    # Extract X-B3-TraceId from http request header
    if hasattr(thrift_struct, 'httpRequestHeader')  \
        and thrift_struct.httpRequestHeader is not None:
        trace_id = extract_trace_id(thrift_struct.httpRequestHeader)
        if trace_id is not None:
            redis.set(tid, trace_id)
    else:
        # Get previous X-B3-TraceId from redis by transaction id
        cached_trace_id = redis.get(tid)
        if cached_trace_id is not None:
            trace_id = cached_trace_id

    if thrift_struct.applicationName is not None:
        application_name = thrift_struct.applicationName

    metadata = (('applicationname', application_name),
                ('x-b3-traceid', trace_id))

    stub.SendSpan.with_call(iter([protobuf_struct]), metadata=metadata)

    return "OK"

def main():
    try:
        # Create Kafka Consumer with topic and bootstrap server
        kafka_bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
        kafka_group_id = os.getenv('KAFKA_GROUP_ID', 'pinpoint-message-convertor')
        kafka_consumer_offset_reset = os.getenv('KAFKA_CONSUMER_OFFSET_RESET', 'latest')
        consumer = Consumer({
            'bootstrap.servers': kafka_bootstrap_servers,
            'group.id': kafka_group_id,
            'auto.offset.reset': kafka_consumer_offset_reset,
        })
        kafka_topics = os.getenv('KAFKA_TOPICS', 'SpanTopic')
        consumer.subscribe(kafka_topics.split(','))

        # Create Redis client
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        redis_password = os.getenv('REDIS_PASSWORD', '')
        redis_port = os.getenv('REDIS_PORT', 6379)
        redis_db = os.getenv('REDIS_DB', 0)
        redis = Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password)

        # Create gRPC channel with gRPC server address
        grpc_server_address = os.getenv('GRPC_SERVER_ADDRESS', 'localhost:9991')
        channel = grpc.insecure_channel(grpc_server_address)
        stub = rpc.SpanStub(channel)

        # Consume Kafka message and send to DataKit Pinpoint Collector
        while True:
            message = consumer.poll(1.0)

            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print("Consumer error: {}".format(message.error()))
                    continue

            try:
                handle(stub, redis, message.value())
            except Exception as e:
                print("Handle error: {} {}".format(type(e), str(e)))
                continue
    except Exception as e:
        consumer.close()
        redis.close()
        channel.close()
        print("Error: {}".format(str(e)))

# Run main function in loop to prevent process exit
if __name__ == '__main__':
    while True:
        main()
