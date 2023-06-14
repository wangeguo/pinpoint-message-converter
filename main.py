#!/usr/bin/python3

import os
import grpc
from parse import meta, parse;
import pinpoint.protobuf.Service_pb2_grpc as rpc
from confluent_kafka import Consumer, KafkaError
from pinpoint_parser import xid
from utils import extract_trace_id
from redis import Redis
import traceback

# Parse message, parse message body to thrift struct, convert to protobuf struct,
# and send to DataKit Pinpoint Collector
def handle(stub: rpc.SpanStub, redis: Redis, message: bytes):
    # Check message header and parse message body to thrift struct,
    # convert to protobuf struct. If message is valid.
    thrift_struct, protobuf_struct = parse(message)

    # Extract X-B3-TraceId from http request header if message is Span, and set it to redis.
    # Get previous X-B3-TraceId from redis by transaction id if message is SpanChunk.
    metadata = meta(thrift_struct, redis)

    # Send protobuf struct to DataKit Pinpoint Collector
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
                traceback.print_exc()
                continue
    except Exception as e:
        consumer.close()
        redis.close()
        channel.close()
        print("Error: {}".format(str(e)))
        traceback.print_exc()

# Run main function in loop to prevent process exit
if __name__ == '__main__':
    while True:
        main()
