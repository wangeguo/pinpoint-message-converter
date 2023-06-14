import time

from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from pinpoint.protobuf.Span_pb2 import PSpan, PSpanMessage, PTransactionId
from pinpoint.thrift.Apptrace.ttypes import TSpan
from pinpoint_parser import xid

# Decode Span from thrift message to TSpan
def decode(message: bytes) -> TSpan:
    buffer = TMemoryBuffer(message)
    Protocol =  TCompactProtocol(buffer)
    span = TSpan()
    span.read(Protocol)

    # print(span)
    return span

# Encode TSpan to Protobuf message and yield the result
def encode(input: TSpan) -> PSpanMessage:
    span = PSpan()
    # span.version = input.version

    (_, timestamp, agent_id, sequence) = xid(input.transactionId, input.appId, input.agentId).split('^')
    span.transactionId.agentId = agent_id
    span.transactionId.agentStartTime = int(timestamp)
    span.transactionId.sequence = int(sequence)

    span.spanId = input.spanId
    span.parentSpanId = input.parentSpanId

    span.startTime = input.startTime
    # span.startTime = int(time.time() * 1000)

    span.elapsed = input.elapsed
    span.apiId = input.apiId
    span.serviceType = input.serviceType
    # span.acceptEvent = input.acceptEvent
    # span.annotations = input.annotations
    # span.flags = input.flags
    if input.err is not None:
        span.err = int(input.err)
    # span.spanEvent = input.spanEvent
    if input.exceptionInfo is not None:
        span.exceptionInfo.intValue = input.exceptionInfo.intValue
        span.exceptionInfo.stringValue = input.exceptionInfo.stringValue
    span.applicationServiceType = input.applicationServiceType
    if input.loggingTransactionInfo is not None:
        span.loggingTransactionInfo = input.loggingTransactionInfo

    return PSpanMessage(span=span)
