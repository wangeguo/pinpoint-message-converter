from typing import List
from thrift.protocol.TCompactProtocol import TCompactProtocol
from thrift.transport.TTransport import TMemoryBuffer
from point import Point
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

# Encode TSpan to Point
def encode(input: TSpan, trace_id: str) -> List[Point]:
    lines = []
    transaction_id = xid(input)

    root = Point()
    root.measurement = "opentelemetry"

    # fields
    root.fields['trace_id'] = str(trace_id)
    root.fields['span_id'] = str(abs(int(input.spanId)))

    parent_id = 0 if input.parentSpanId < 0 else input.parentSpanId
    root.fields['parent_id'] = str(parent_id)

    root.fields['start'] = int(input.startTime) * 1000000
    root.fields['duration'] = int(input.elapsed) * 1000000
    root.fields['resource'] = str(input.rpc)

    # tags
    root.tags['service'] = str(input.applicationName)
    root.tags['service_name'] = service_name(input.serviceType)
    root.tags['operation'] = service_name(input.serviceType)
    root.tags['service_type'] = service_type(input.serviceType)

    # Extra tags
    for k, v in input.__dict__.items():
        root.tags[str(k)] = str(v)
    root.tags.pop('spanEventList')
    root.tags['transactionId'] = transaction_id
    root.tags['original_type'] = "Span"

    root.time = int(input.startTime) * 1000000
    lines.append(root)

    # span event list
    if input.spanEventList is not None:
        parent_id = root.fields.get("span_id")
        for event in input.spanEventList:
            line = span_event.encode(
                input, event, trace_id, transaction_id, parent_id
            )
            lines.append(line)
            parent_id = line.fields.get("span_id")

    return lines
