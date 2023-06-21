from pinpoint.thrift.Apptrace.ttypes import TSpan, TSpanChunk
from pinpoint_parser import pinpoint_parser

## 从 headers 字符串中提取 traceId
## headers 格式：key1,value1;key2,value2
def extract_trace_id(httpRequestHeader: str):
    trace_id = None
    for header in httpRequestHeader.split(";"):
        if header.startswith("x-b3-traceid"):
            trace_id = header.split(",")[1]
            break
    return trace_id

def xid(input: TSpan or TSpanChunk):
    return pinpoint_parser.xid(input.transactionId, input.appId, input.agentId)
