from typing import Tuple
from pinpoint.protobuf.Span_pb2 import PSpanMessage
from pinpoint.thrift.Apptrace.ttypes import TSpan
import span as span
import span_chunk as span_chunk
from utils import extract_trace_id
from pinpoint_parser import xid

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

def meta(thrift_struct: TSpan, redis):
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

    return (('applicationname', application_name),
                ('x-b3-traceid', trace_id))
