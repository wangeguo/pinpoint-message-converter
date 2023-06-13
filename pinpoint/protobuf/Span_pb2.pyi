from v1 import Annotation_pb2 as _Annotation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PAcceptEvent(_message.Message):
    __slots__ = ["endPoint", "parentInfo", "remoteAddr", "rpc"]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PARENTINFO_FIELD_NUMBER: _ClassVar[int]
    REMOTEADDR_FIELD_NUMBER: _ClassVar[int]
    RPC_FIELD_NUMBER: _ClassVar[int]
    endPoint: str
    parentInfo: PParentInfo
    remoteAddr: str
    rpc: str
    def __init__(self, rpc: _Optional[str] = ..., endPoint: _Optional[str] = ..., remoteAddr: _Optional[str] = ..., parentInfo: _Optional[_Union[PParentInfo, _Mapping]] = ...) -> None: ...

class PApiMetaData(_message.Message):
    __slots__ = ["apiId", "apiInfo", "line", "location", "type"]
    APIID_FIELD_NUMBER: _ClassVar[int]
    APIINFO_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    apiId: int
    apiInfo: str
    line: int
    location: str
    type: int
    def __init__(self, apiId: _Optional[int] = ..., apiInfo: _Optional[str] = ..., line: _Optional[int] = ..., type: _Optional[int] = ..., location: _Optional[str] = ...) -> None: ...

class PLocalAsyncId(_message.Message):
    __slots__ = ["asyncId", "sequence"]
    ASYNCID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    asyncId: int
    sequence: int
    def __init__(self, asyncId: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...

class PMessageEvent(_message.Message):
    __slots__ = ["destinationId", "endPoint", "nextSpanId"]
    DESTINATIONID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    NEXTSPANID_FIELD_NUMBER: _ClassVar[int]
    destinationId: str
    endPoint: str
    nextSpanId: int
    def __init__(self, nextSpanId: _Optional[int] = ..., endPoint: _Optional[str] = ..., destinationId: _Optional[str] = ...) -> None: ...

class PNextEvent(_message.Message):
    __slots__ = ["messageEvent"]
    MESSAGEEVENT_FIELD_NUMBER: _ClassVar[int]
    messageEvent: PMessageEvent
    def __init__(self, messageEvent: _Optional[_Union[PMessageEvent, _Mapping]] = ...) -> None: ...

class PParentInfo(_message.Message):
    __slots__ = ["acceptorHost", "parentApplicationName", "parentApplicationType"]
    ACCEPTORHOST_FIELD_NUMBER: _ClassVar[int]
    PARENTAPPLICATIONNAME_FIELD_NUMBER: _ClassVar[int]
    PARENTAPPLICATIONTYPE_FIELD_NUMBER: _ClassVar[int]
    acceptorHost: str
    parentApplicationName: str
    parentApplicationType: int
    def __init__(self, parentApplicationName: _Optional[str] = ..., parentApplicationType: _Optional[int] = ..., acceptorHost: _Optional[str] = ...) -> None: ...

class PResult(_message.Message):
    __slots__ = ["message", "success"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    message: str
    success: bool
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class PSpan(_message.Message):
    __slots__ = ["acceptEvent", "annotation", "apiId", "applicationServiceType", "elapsed", "err", "exceptionInfo", "flag", "loggingTransactionInfo", "parentSpanId", "serviceType", "spanEvent", "spanId", "startTime", "transactionId", "version"]
    ACCEPTEVENT_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    APIID_FIELD_NUMBER: _ClassVar[int]
    APPLICATIONSERVICETYPE_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_FIELD_NUMBER: _ClassVar[int]
    ERR_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONINFO_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    LOGGINGTRANSACTIONINFO_FIELD_NUMBER: _ClassVar[int]
    PARENTSPANID_FIELD_NUMBER: _ClassVar[int]
    SERVICETYPE_FIELD_NUMBER: _ClassVar[int]
    SPANEVENT_FIELD_NUMBER: _ClassVar[int]
    SPANID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    acceptEvent: PAcceptEvent
    annotation: _containers.RepeatedCompositeFieldContainer[_Annotation_pb2.PAnnotation]
    apiId: int
    applicationServiceType: int
    elapsed: int
    err: int
    exceptionInfo: _Annotation_pb2.PIntStringValue
    flag: int
    loggingTransactionInfo: int
    parentSpanId: int
    serviceType: int
    spanEvent: _containers.RepeatedCompositeFieldContainer[PSpanEvent]
    spanId: int
    startTime: int
    transactionId: PTransactionId
    version: int
    def __init__(self, version: _Optional[int] = ..., transactionId: _Optional[_Union[PTransactionId, _Mapping]] = ..., spanId: _Optional[int] = ..., parentSpanId: _Optional[int] = ..., startTime: _Optional[int] = ..., elapsed: _Optional[int] = ..., apiId: _Optional[int] = ..., serviceType: _Optional[int] = ..., acceptEvent: _Optional[_Union[PAcceptEvent, _Mapping]] = ..., annotation: _Optional[_Iterable[_Union[_Annotation_pb2.PAnnotation, _Mapping]]] = ..., flag: _Optional[int] = ..., err: _Optional[int] = ..., spanEvent: _Optional[_Iterable[_Union[PSpanEvent, _Mapping]]] = ..., exceptionInfo: _Optional[_Union[_Annotation_pb2.PIntStringValue, _Mapping]] = ..., applicationServiceType: _Optional[int] = ..., loggingTransactionInfo: _Optional[int] = ...) -> None: ...

class PSpanChunk(_message.Message):
    __slots__ = ["applicationServiceType", "endPoint", "keyTime", "localAsyncId", "spanEvent", "spanId", "transactionId", "version"]
    APPLICATIONSERVICETYPE_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    KEYTIME_FIELD_NUMBER: _ClassVar[int]
    LOCALASYNCID_FIELD_NUMBER: _ClassVar[int]
    SPANEVENT_FIELD_NUMBER: _ClassVar[int]
    SPANID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    applicationServiceType: int
    endPoint: str
    keyTime: int
    localAsyncId: PLocalAsyncId
    spanEvent: _containers.RepeatedCompositeFieldContainer[PSpanEvent]
    spanId: int
    transactionId: PTransactionId
    version: int
    def __init__(self, version: _Optional[int] = ..., transactionId: _Optional[_Union[PTransactionId, _Mapping]] = ..., spanId: _Optional[int] = ..., endPoint: _Optional[str] = ..., spanEvent: _Optional[_Iterable[_Union[PSpanEvent, _Mapping]]] = ..., applicationServiceType: _Optional[int] = ..., keyTime: _Optional[int] = ..., localAsyncId: _Optional[_Union[PLocalAsyncId, _Mapping]] = ...) -> None: ...

class PSpanEvent(_message.Message):
    __slots__ = ["annotation", "apiId", "asyncEvent", "depth", "endElapsed", "exceptionInfo", "nextEvent", "sequence", "serviceType", "startElapsed"]
    ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    APIID_FIELD_NUMBER: _ClassVar[int]
    ASYNCEVENT_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    ENDELAPSED_FIELD_NUMBER: _ClassVar[int]
    EXCEPTIONINFO_FIELD_NUMBER: _ClassVar[int]
    NEXTEVENT_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SERVICETYPE_FIELD_NUMBER: _ClassVar[int]
    STARTELAPSED_FIELD_NUMBER: _ClassVar[int]
    annotation: _containers.RepeatedCompositeFieldContainer[_Annotation_pb2.PAnnotation]
    apiId: int
    asyncEvent: int
    depth: int
    endElapsed: int
    exceptionInfo: _Annotation_pb2.PIntStringValue
    nextEvent: PNextEvent
    sequence: int
    serviceType: int
    startElapsed: int
    def __init__(self, sequence: _Optional[int] = ..., depth: _Optional[int] = ..., startElapsed: _Optional[int] = ..., endElapsed: _Optional[int] = ..., serviceType: _Optional[int] = ..., annotation: _Optional[_Iterable[_Union[_Annotation_pb2.PAnnotation, _Mapping]]] = ..., apiId: _Optional[int] = ..., exceptionInfo: _Optional[_Union[_Annotation_pb2.PIntStringValue, _Mapping]] = ..., nextEvent: _Optional[_Union[PNextEvent, _Mapping]] = ..., asyncEvent: _Optional[int] = ...) -> None: ...

class PSpanMessage(_message.Message):
    __slots__ = ["span", "spanChunk"]
    SPANCHUNK_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    span: PSpan
    spanChunk: PSpanChunk
    def __init__(self, span: _Optional[_Union[PSpan, _Mapping]] = ..., spanChunk: _Optional[_Union[PSpanChunk, _Mapping]] = ...) -> None: ...

class PSqlMetaData(_message.Message):
    __slots__ = ["sql", "sqlId"]
    SQLID_FIELD_NUMBER: _ClassVar[int]
    SQL_FIELD_NUMBER: _ClassVar[int]
    sql: str
    sqlId: int
    def __init__(self, sqlId: _Optional[int] = ..., sql: _Optional[str] = ...) -> None: ...

class PStringMetaData(_message.Message):
    __slots__ = ["stringId", "stringValue"]
    STRINGID_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    stringId: int
    stringValue: str
    def __init__(self, stringId: _Optional[int] = ..., stringValue: _Optional[str] = ...) -> None: ...

class PTransactionId(_message.Message):
    __slots__ = ["agentId", "agentStartTime", "sequence"]
    AGENTID_FIELD_NUMBER: _ClassVar[int]
    AGENTSTARTTIME_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    agentId: str
    agentStartTime: int
    sequence: int
    def __init__(self, agentId: _Optional[str] = ..., agentStartTime: _Optional[int] = ..., sequence: _Optional[int] = ...) -> None: ...
