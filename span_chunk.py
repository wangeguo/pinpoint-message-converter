from typing import List
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from ddtrace import DDSpan
import span_event
from pinpoint.thrift.Apptrace.ttypes import  TSpanChunk
from utils import xid

# Decode Span Chunk from thrift message to TSpanChunk
def decode(message: bytes) -> TSpanChunk:
    buffer = TMemoryBuffer(message)
    Protocol =  TCompactProtocol(buffer)
    chunk = TSpanChunk()
    chunk.read(Protocol)

    return chunk

# Encode TSpanChunk to DDSpan
def encode(input: TSpanChunk, trace_id: str) -> List[DDSpan]:
    if input.spanEventList is None:
        return []

    trace = []
    transaction_id = xid(input)

    parent_id = abs(int(input.spanId))
    for event in input.spanEventList:
        span = span_event.encode(
            input, event, trace_id, transaction_id, parent_id
        )
        trace.append(span)
        parent_id = span.span_id

    return trace
