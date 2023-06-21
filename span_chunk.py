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
# - startTime
def encode(input: TSpanChunk, trace_id: str) -> List[DDSpan]:
    trace = []
    transaction_id = xid(input)

    # root span
    root = DDSpan()
    root.span_id = int(input.spanId)
    root.parent_id = 0
    root.service = str(input.applicationName)
    root.name = str(input.endPoint)
    root.resource = str(input.endPoint)
    root.start = input.startTime
    # root.duration = int(input.elapsed)
    root.type = str(input.serviceType)

    root.meta = {}
    for k, v in input.__dict__.items():
        root.meta[k] = str(v)

    # Overwrites
    root.meta["trace_id"] = trace_id
    root.meta["transactionId"] = transaction_id
    root.meta.pop('spanEventList')

    trace.append(root)

    # span event list
    parent_id = int(input.spanId)
    for event in input.spanEventList:
        trace.append(span_event.encode(
            input, event, trace_id, transaction_id, parent_id
        ))
        parent_id = event.spanId

    return trace
