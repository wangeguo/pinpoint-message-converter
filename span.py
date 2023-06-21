from typing import List
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from ddtrace import DDSpan
from pinpoint.thrift.Apptrace.ttypes import TSpan
from utils import xid
import span_event

# Decode Span from thrift message to TSpan
def decode(message: bytes) -> TSpan:
    buffer = TMemoryBuffer(message)
    Protocol =  TCompactProtocol(buffer)
    span = TSpan()
    span.read(Protocol)

    return span

# Encode TSpan to DDSpan
#
# TSpan:
# - agentId
# - applicationName
# - agentStartTime
# - transactionId
# - appkey
# - spanId
# - parentSpanId
# - startTime
# - elapsed
# - rpc
# - serviceType
# - endPoint
# - remoteAddr
# - annotations
# - flag
# - err
# - spanEventList
# - parentApplicationName
# - parentApplicationType
# - acceptorHost
# - apiId
# - exceptionInfo
# - applicationServiceType
# - loggingTransactionInfo
# - httpPara
# - httpMethod
# - httpRequestHeader
# - httpRequestUserAgent
# - httpRequestBody
# - httpResponseBody
# - retcode
# - httpRequestUID
# - httpRequestTID
# - pagentId
# - apidesc
# - httpResponseHeader
# - userId
# - sessionId
# - appId
# - tenant
# - threadId
# - threadName
# - hasNextCall

def encode(input: TSpan, trace_id: str) -> List[DDSpan]:
    trace = []
    transaction_id = xid(input)

    root = DDSpan()
    root.span_id = int(input.spanId)
    root.parent_id = int(input.parentSpanId)
    root.service = str(input.applicationName)
    root.name = str(input.rpc)
    root.resource = str(input.rpc)
    root.start = int(input.startTime)
    root.duration = int(input.elapsed)
    root.type = str(input.serviceType)

    root.meta = {}
    for k, v in input.__dict__.items():
        root.meta[k] = str(v)

    # Overwrites
    root.meta["trace_id"] = trace_id
    root.meta["transactionId"] = xid(input)
    root.meta.pop('spanEventList')

    trace.append(root)

    # span event list
    parent_id = int(input.spanId)
    for event in input.spanEventList:
        trace.append(span_event.encode(input, event, trace_id, transaction_id, parent_id))
        parent_id = event.spanId

    return trace
