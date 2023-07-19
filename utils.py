import random
from constants import SERVICE_MAPS
from pinpoint.thrift.Apptrace.ttypes import TSpan, TSpanChunk
from pinpoint_parser import pinpoint_parser

## 从 headers 字符串中提取 traceId
## headers 格式：key1,value1;key2,value2
def extract_trace_id(httpRequestHeader: str, key: str):
    trace_id = None
    for header in httpRequestHeader.split(";"):
        if header.startswith(key):
            trace_id = header.split(",")[1]
            break
    return trace_id

def xid(input: TSpan or TSpanChunk) -> str:
    return pinpoint_parser.xid(input.transactionId, input.appId, input.agentId)

# get service name by service type from SERVICE_TYPE
def service_name(service_type: int) -> str:
    return SERVICE_MAPS.get(service_type, ("Unknown", "custom"))[0]

# get service type by service type from SERVICE_TYPE
def service_type(service_type: int) -> str:
    return SERVICE_MAPS.get(service_type, ("Unknown", "custom"))[1]

# generate random int64 as trace_id from 2^32 to 2^64
def random_id() -> int:
    while True:
        num = random.getrandbits(63)
        num += 2**32
        if num > 0:
            return num
