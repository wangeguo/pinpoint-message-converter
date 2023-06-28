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
#
# TSpanChunk
# - agentId
# - applicationName
# - agentStartTime
# - serviceType
# - transactionId
# - appkey
# - spanId
# - endPoint
# - spanEventList
# - applicationServiceType
# - appId
# - tenant
# - threadId
# - threadName
# - userId
# - sessionId
# - startTime (None)
def encode(input: TSpanChunk, trace_id: str) -> List[DDSpan]:
    trace = []
    transaction_id = xid(input)

    # # root span
    # root = DDSpan()
    # root.span_id = int(input.spanId)
    # root.parent_id = 0
    # root.service = str(input.applicationName)
    # root.name = service_name(input.serviceType)
    # root.resource = str(input.endPoint)
    # root.start = int(input.agentStartTime) * 1000
    # # root.duration = int(input.elapsed)
    # root.type = service_type(input.serviceType)

    # root.meta = {}
    # for k, v in input.__dict__.items():
    #     root.meta[k] = str(v)

    # # Overwrites
    # root.meta["trace_id"] = trace_id
    # root.meta["transactionId"] = transaction_id
    # root.meta["original_type"] = "SpanChunk"

    # # root.meta.pop('spanEventList')

    # trace.append(root)

    # span event list
    if input.spanEventList is not None:
        parent_id = abs(int(input.spanId))
        for event in input.spanEventList:
            span = span_event.encode(
                input, event, trace_id, transaction_id, parent_id
            )
            trace.append(span)
            parent_id = span.span_id

    return trace
