from point import Point
from pinpoint.thrift.Apptrace.ttypes import  TSpan, TSpanChunk, TSpanEvent
from utils import service_name, random_id, service_type

# Encode TSpanEvent to Point
def encode(parent: TSpan or TSpanChunk, event: TSpanEvent,
           trace_id: str, transaction_id: str, parent_id: int) -> Point:
    line = Point()
    line.measurement = "opentelemetry"

    # fields
    line.fields['trace_id'] = str(trace_id)
    line.fields['span_id'] = str(random_id())
    line.fields['parent_id'] = str(parent_id)
    line.fields['start'] = (int(parent.agentStartTime) + int(event.startElapsed)) * 1000000

    duration = (int(event.startElapsed) + int(event.endElapsed)) * 1000000
    if duration < 0:
        duration = int(1 * 1000000)
    line.fields['duration'] = duration

    # resource
    if event.rpc is not None:
        resource = str(event.rpc)
    elif event.annotations is not None:
        resource = str(event.annotations)
    elif event.sql is not None:
        resource = str(event.sql)
    elif event.url is not None:
        resource = str(event.url)
    elif event.method is not None:
        resource = str(event.method)
    elif event.arguments is not None:
        resource = str(event.arguments)
    else:
        resource = str(event.endPoint)
    line.fields['resource'] = resource

    # tags
    line.tags['service'] = str(parent.applicationName)
    line.tags['service_name'] = service_name(event.serviceType)
    line.tags['operation'] = service_name(event.serviceType)
    line.tags['service_type'] = service_type(event.serviceType)

    # Extra tags
    line.tags['transactionId'] = transaction_id
    line.tags['original_type'] = "SpanEvent"

    for k, v in event.__dict__.items():
        line.tags[str(k)] = str(v)

    line.time = line.fields.get('start')

    return line
