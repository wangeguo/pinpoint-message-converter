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

    if input.endPoint is not None:
        span.acceptEvent.endPoint = str(input.endPoint)

    if input.acceptorHost is not None:
        span.acceptEvent.parentInfo.acceptorHost = str(input.acceptorHost)
    if input.parentApplicationName is not None:
        span.acceptEvent.parentInfo.parentApplicationName = str(input.parentApplicationName)
    if input.parentApplicationType is not None:
        span.acceptEvent.parentInfo.parentApplicationType = input.parentApplicationType
    if input.remoteAddr is not None:
        span.acceptEvent.remoteAddr = str(input.remoteAddr)
    if input.rpc is not None:
        span.acceptEvent.rpc = str(input.rpc)

    # TODO: set annotation from annotation list of input
    # annotation: _containers.RepeatedCompositeFieldContainer[_Annotation_pb2.PAnnotation]

    if input.apiId is not None:
        span.apiId = input.apiId
    if input.applicationServiceType is not None:
        span.applicationServiceType = int(input.applicationServiceType)
    if input.elapsed is not None:
        span.elapsed = int(input.elapsed)
    if input.err is not None:
        span.err = int(input.err)
    if input.exceptionInfo is not None:
        if input.exceptionInfo.intValue is not None:
            span.exceptionInfo.intValue = int(input.exceptionInfo.intValue)
        if input.exceptionInfo.stringValue is not None:
            span.exceptionInfo.stringValue.value = str(input.exceptionInfo.stringValue)
    if input.flags is not None:
        span.flag = input.flag

    if input.loggingTransactionInfo is not None:
        span.loggingTransactionInfo = input.loggingTransactionInfo
    span.parentSpanId = input.parentSpanId
    if input.serviceType is not None:
        span.serviceType = int(input.serviceType)

    # set span event from span event list of input
    if input.spanEventList is not None:
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

    if input.apiId is not None:
        event.apiId = int(input.apiId)

    # TODO: asyncEvent: int

    if input.depth is not None:
        event.depth = input.depth
    if input.endElapsed is not None:
        event.endElapsed = input.endElapsed

    if input.exceptionInfo is not None:
        if input.exceptionInfo.intValue is not None:
            event.exceptionInfo.intValue = int(input.exceptionInfo.intValue)
        if input.exceptionInfo.stringValue is not None:
            event.exceptionInfo.stringValue.value = str(input.exceptionInfo.stringValue)

    if input.destinationId is not None:
        event.nextEvent.messageEvent.destinationId = str(input.destinationId)
    if input.endPoint is not None:
        event.nextEvent.messageEvent.endPoint = str(input.endPoint)
    if input.nextSpanId is not None:
        event.nextEvent.messageEvent.nextSpanId = int(input.nextSpanId)

    if input.sequence is not None:
        event.sequence = input.sequence
    if input.serviceType is not None:
        event.serviceType = input.serviceType
    if input.startElapsed is not None:
        event.startElapsed = input.startElapsed

    return event
