import time
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from pinpoint.protobuf.Span_pb2 import  PSpanChunk, PSpanEvent, PSpanMessage
from pinpoint.thrift.Apptrace.ttypes import  TSpanChunk, TSpanEvent
from pinpoint_parser import xid

# Decode Span Chunk from thrift message to TSpanChunk
def decode(message: bytes) -> TSpanChunk:
    buffer = TMemoryBuffer(message)
    Protocol =  TCompactProtocol(buffer)
    chunk = TSpanChunk()
    chunk.read(Protocol)

    return chunk

# Encode TSpanChunk to Protobuf message and yield the result
def encode(input: TSpanChunk) -> PSpanMessage:
    chunk = PSpanChunk()

    (_, timestamp, agent_id, sequence) = xid(input.transactionId, input.appId, input.agentId).split('^')
    chunk.transactionId.agentId = agent_id
    chunk.transactionId.agentStartTime = int(timestamp)
    chunk.transactionId.sequence = int(sequence)

    chunk.spanId = input.spanId
    chunk.endPoint = input.endPoint

    # set span event from span event list of input
    for t_span_event in input.spanEventList:
        p_span_event = convert_span_event(t_span_event)
        chunk.spanEvent.append(p_span_event)

    chunk.applicationServiceType = input.applicationServiceType
    chunk.keyTime = input.agentStartTime
    # chunk.keyTime = int(time.time() * 1000)

    # chunk.localAsyncId = input.localAsyncId

    yield PSpanMessage(spanChunk=chunk)

# covert TSpanEvent to PSpanEvent
def convert_span_event(input: TSpanEvent) -> PSpanEvent:
    event = PSpanEvent()
    event.sequence = input.sequence
    event.depth = input.depth
    event.startElapsed = input.startElapsed
    event.endElapsed = input.endElapsed
    event.serviceType = input.serviceType
    event.apiId = input.apiId

    return event
