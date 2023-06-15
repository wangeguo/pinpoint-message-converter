import time
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from pinpoint.protobuf.Span_pb2 import  PSpanChunk, PSpanMessage
from pinpoint.thrift.Apptrace.ttypes import  TSpanChunk
from pinpoint_parser import xid
from span import convert_span_event

# Decode Span Chunk from thrift message to TSpanChunk
def decode(message: bytes) -> TSpanChunk:
    buffer = TMemoryBuffer(message)
    Protocol =  TCompactProtocol(buffer)
    chunk = TSpanChunk()
    chunk.read(Protocol)

    # FIXME: Debug only
    # print(chunk)
    return chunk

# Encode TSpanChunk to Protobuf message
def encode(input: TSpanChunk) -> PSpanMessage:
    chunk = PSpanChunk()

    if input.applicationServiceType is not None:
        chunk.applicationServiceType = input.applicationServiceType
    if input.endPoint is not None:
        chunk.endPoint = input.endPoint

    # FIXME: Using real key time on production environment
    chunk.keyTime = input.agentStartTime
    # chunk.keyTime = int(time.time() * 1000)

    # TODO: localAsyncId: PLocalAsyncId

    # set span event from span event list of input
    if input.spanEventList is not None:
        for t_span_event in input.spanEventList:
            p_span_event = convert_span_event(t_span_event)
            chunk.spanEvent.append(p_span_event)

    chunk.spanId = input.spanId

    (_, timestamp, agent_id, sequence) = xid(input.transactionId, input.appId, input.agentId).split('^')
    chunk.transactionId.agentId = agent_id
    chunk.transactionId.agentStartTime = int(timestamp)
    chunk.transactionId.sequence = int(sequence)

    # TODO: version: int

    return PSpanMessage(spanChunk=chunk)
