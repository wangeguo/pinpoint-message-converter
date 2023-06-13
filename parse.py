from typing import Tuple
from pinpoint.protobuf.Span_pb2 import PSpanMessage
from pinpoint.thrift.Apptrace.ttypes import TSpan
import span as span
import span_chunk as span_chunk

def parse_header(buf):
    if len(buf) != 4:
        return 'InvalidProtocolCode'
    signature = buf[0]
    if signature != 0xEF:
        return 'InvalidProtocolCode'
    code = 0
    if buf[2] == 0 and buf[3] == 0:
        code = 0
    elif buf[2] == 0 and buf[3] == 40:
        code = 40
    elif buf[2] == 0 and buf[3] == 70:
        code = 70
    else:
        return 'InvalidProtocolCode'
    return code

# Parse and format message to thrift struct, then covert it to protobuf struct, return theme.
def parse(message: bytes) -> Tuple[TSpan, PSpanMessage]:
    protocol_code = parse_header(message[:4])
    protocol_body = message[4:]

    if protocol_code == 40:
        thrift_struct = span.decode(protocol_body)
        protobuf_struct = span.encode(thrift_struct)
    elif protocol_code == 70:
        thrift_struct = span_chunk.decode(protocol_body)
        protobuf_struct = span_chunk.encode(thrift_struct)
    else:
        raise Exception('InvalidProtocolCode')

    return thrift_struct, protobuf_struct
