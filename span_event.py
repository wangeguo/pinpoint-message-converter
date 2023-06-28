from ddtrace import DDSpan
from pinpoint.thrift.Apptrace.ttypes import  TSpan, TSpanChunk, TSpanEvent
from utils import service_name, random_id, service_type

# TSpanEvent
# - spanId
# - sequence
# - startElapsed
# - endElapsed
# - rpc
# - serviceType
# - endPoint
# - annotations
# - depth
# - nextSpanId
# - destinationId
# - apiId
# - exceptionInfo
# - exceptionClassName
# - asyncId
# - nextAsyncId
# - asyncSequence
# - apiInfo
# - lineNumber
# - sql
# - retcode
# - requestHeaders
# - requestBody
# - responseBody
# - url
# - method
# - arguments

# Encode TSpanEvent to DDSpan
def encode(parent: TSpan or TSpanChunk, event: TSpanEvent,
           trace_id: str, transaction_id: str, parent_id: int) -> DDSpan:
    span = DDSpan()
    # span.span_id = event.spanId
    span.span_id = random_id()

    span.parent_id = parent_id
    span.service = str(parent.applicationName)
    span.name = service_name(event.serviceType)

    if event.rpc is not None:
        span.resource = str(event.rpc)
    elif event.annotations is not None:
        span.resource = str(event.annotations)
    elif event.sql is not None:
        span.resource = str(event.sql)
    elif event.url is not None:
        span.resource = str(event.url)
    elif event.method is not None:
        span.resource = str(event.method)
    elif event.arguments is not None:
        span.resource = str(event.arguments)
    else:
        span.resource = str(event.endPoint)

    span.start = (int(parent.agentStartTime) + int(event.startElapsed)) * 1000

    span.duration = (int(event.startElapsed) + int(event.endElapsed)) * 1000
    if span.duration == 0:
        span.duration = int(1 * 1000)

    span.type = service_type(event.serviceType)

    span.meta = {}
    for k, v in event.__dict__.items():
        span.meta[k] = str(v)

    # Overwrites
    span.meta["trace_id"] = trace_id
    span.meta["transactionId"] = transaction_id
    span.meta["original_type"] = "SpanEvent"

    return span
