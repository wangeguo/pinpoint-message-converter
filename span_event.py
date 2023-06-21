from ddtrace import DDSpan
from pinpoint.thrift.Apptrace.ttypes import  TSpan, TSpanChunk, TSpanEvent

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
    span.span_id = event.spanId
    span.parent_id = parent_id
    span.service = str(parent.applicationName)
    span.name = str(event.rpc)
    span.resource = str(event.rpc)
    span.start = int(event.startElapsed)
    span.duration = int(event.endElapsed)
    span.type = str(event.serviceType)

    span.meta = {}
    for k, v in event.__dict__.items():
        span.meta[k] = str(v)

    # Overwrites
    span.meta["trace_id"] = trace_id
    span.meta["transactionId"] = transaction_id

    return span
