import logging
from redis import Redis
from pinpoint.thrift.Apptrace.ttypes import TSpan, TSpanChunk
import span as span
import span_chunk as span_chunk
from utils import extract_trace_id, xid

# Parse the protocol code
def code(buf: bytes) -> int:
    # Check the protocol length must be 4
    if len(buf) != 4:
        logging.debug("Invalid Protocol Length: {}".format(len(buf)))
        raise Exception('Invalid Protocol Length')

    # Check the protocol signature must be 0xEF
    signature = buf[0]
    if signature != 0xEF:
        logging.debug("Invalid Protocol Signature: {}".format(signature))
        raise Exception('Invalid Protocol Signature')

    code = 0
    if buf[2] == 0 and buf[3] == 0:
        code = 0
    elif buf[2] == 0 and buf[3] == 40:
        code = 40
    elif buf[2] == 0 and buf[3] == 70:
        code = 70
    else:
        logging.debug("Invalid Protocol Code: {}".format(buf[3]))
        raise Exception('Invalid Protocol Code')

    return code

# Parse and format message to thrift struct
def parse(message: bytes) -> TSpan or TSpanChunk:
    return span.decode(message[4:]) if code(message[:4]) == 40 else span_chunk.decode(message[4:])

# Get trace id from http request header or cache if the xid was already exists, otherwise return xid
def get_trace_id(input: TSpan or TSpanChunk, redis: Redis, key: str) -> str:
    trace_id = None
    tid = xid(input)

    # Get previous X-B3-TraceId from redis by transaction id
    cached_trace_id = redis.get(tid)
    if cached_trace_id is not None:
        trace_id = str(cached_trace_id)
    else:
        # Extract custom trace id from http request header
        if hasattr(input, 'httpRequestHeader')  \
            and input.httpRequestHeader is not None:
            trace_id = extract_trace_id(input.httpRequestHeader, key)
            if trace_id is not None:
                redis.set(tid, trace_id)

    return str(trace_id) if trace_id is not None else tid
