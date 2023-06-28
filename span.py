from typing import List
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from ddtrace import DDSpan
from pinpoint.thrift.Apptrace.ttypes import TSpan
from utils import service_name, service_type, xid
import span_event

# Decode Span from thrift message to TSpan
def decode(message: bytes) -> TSpan:
    buffer = TMemoryBuffer(message)
    Protocol =  TCompactProtocol(buffer)
    span = TSpan()
    span.read(Protocol)

    return span

# Encode TSpan to DDSpan

def encode(input: TSpan, trace_id: str) -> List[DDSpan]:
    trace = []
    transaction_id = xid(input)

    root = DDSpan()
    root.span_id = abs(int(input.spanId))

    if input.parentSpanId < 0:
        root.parent_id = 0
    else:
        root.parent_id = int(input.parentSpanId)

    root.service = str(input.applicationName)
    root.name = service_name(input.serviceType)
    root.resource = str(input.rpc)
    root.start = int(input.startTime) * 1000
    root.duration = int(input.elapsed) * 1000
    root.type = service_type(input.serviceType)

    root.meta = {}
    for k, v in input.__dict__.items():
        root.meta[k] = str(v)

    # Overwrites
    root.meta["trace_id"] = trace_id
    root.meta["transactionId"] = xid(input)
    root.meta["original_type"] = "Span"

    root.meta.pop('spanEventList')

    trace.append(root)

    # span event list
    if input.spanEventList is not None:
        parent_id = root.span_id
        for event in input.spanEventList:
            span = span_event.encode(
                input, event, trace_id, transaction_id, parent_id
            )
            trace.append(span)
            parent_id = span.span_id

    return trace
