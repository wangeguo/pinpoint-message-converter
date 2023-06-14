import time

from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from pinpoint.protobuf.Span_pb2 import PParentInfo, PSpan, PSpanEvent, PSpanMessage, PTransactionId
from pinpoint.thrift.Apptrace.ttypes import TSpan, TSpanEvent
from pinpoint_parser import xid

# Decode Span from thrift message to TSpan
def decode(message: bytes) -> TSpan:
    buffer = TMemoryBuffer(message)
    Protocol =  TCompactProtocol(buffer)
    span = TSpan()
    span.read(Protocol)

    # print(span)
    return span

# Encode TSpan to Protobuf message
def encode(input: TSpan) -> PSpanMessage:
    span = PSpan()

    span.acceptEvent.endPoint = input.endPoint

    span.acceptEvent.parentInfo.acceptorHost = str(input.acceptorHost)
    span.acceptEvent.parentInfo.parentApplicationName = str(input.parentApplicationName)
    if input.parentApplicationType is not None:
        span.acceptEvent.parentInfo.parentApplicationType = input.parentApplicationType
    span.acceptEvent.remoteAddr = input.remoteAddr
    span.acceptEvent.rpc = input.rpc

    # TODO: set annotation from annotation list of input
    # annotation: _containers.RepeatedCompositeFieldContainer[_Annotation_pb2.PAnnotation]

    span.apiId = input.apiId
    span.applicationServiceType = input.applicationServiceType
    span.elapsed = input.elapsed
    if input.err is not None:
        span.err = int(input.err)
    if input.exceptionInfo is not None:
        span.exceptionInfo.intValue = input.exceptionInfo.intValue
        span.exceptionInfo.stringValue = input.exceptionInfo.stringValue
    span.flag = input.flag

    if input.loggingTransactionInfo is not None:
        span.loggingTransactionInfo = input.loggingTransactionInfo
    span.parentSpanId = input.parentSpanId
    span.serviceType = input.serviceType

    # set span event from span event list of input
    for t_span_event in input.spanEventList:
        p_span_event = convert_span_event(t_span_event)
        span.spanEvent.append(p_span_event)

    span.spanId = input.spanId

    # FIXME: Using real start time on production environment
    span.startTime = input.startTime
    # span.startTime = int(time.time() * 1000)

    (_, timestamp, agent_id, sequence) = xid(input.transactionId, input.appId, input.agentId).split('^')
    span.transactionId.agentId = agent_id
    span.transactionId.agentStartTime = int(timestamp)
    span.transactionId.sequence = int(sequence)

    # TODO: version: int

    return PSpanMessage(span=span)

# covert TSpanEvent to PSpanEvent
def convert_span_event(input: TSpanEvent) -> PSpanEvent:
    event = PSpanEvent()


    # TODO: annotation: _containers.RepeatedCompositeFieldContainer[_Annotation_pb2.PAnnotation]

    event.apiId = input.apiId

    # TODO: asyncEvent: int

    event.depth = input.depth
    event.endElapsed = input.endElapsed

    if input.exceptionInfo is not None:
        event.exceptionInfo.intValue = input.exceptionInfo.intValue
        event.exceptionInfo.stringValue = input.exceptionInfo.stringValue

    event.nextEvent.messageEvent.destinationId = str(input.destinationId)
    event.nextEvent.messageEvent.endPoint = str(input.endPoint)
    event.nextEvent.messageEvent.nextSpanId = int(input.nextSpanId)

    event.sequence = input.sequence
    event.serviceType = input.serviceType
    event.startElapsed = input.startElapsed

    return event
