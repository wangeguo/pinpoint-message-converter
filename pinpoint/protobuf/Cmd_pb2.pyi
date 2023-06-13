from google.protobuf import wrappers_pb2 as _wrappers_pb2
from pinpoint.protobuf import ThreadDump_pb2 as _ThreadDump_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ACTIVE_THREAD_COUNT: PCommandType
ACTIVE_THREAD_DUMP: PCommandType
ACTIVE_THREAD_LIGHT_DUMP: PCommandType
DESCRIPTOR: _descriptor.FileDescriptor
ECHO: PCommandType
NONE: PCommandType
PING: PCommandType
PONG: PCommandType

class PCmdActiveThreadCount(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PCmdActiveThreadCountRes(_message.Message):
    __slots__ = ["activeThreadCount", "commonStreamResponse", "histogramSchemaType", "timeStamp"]
    ACTIVETHREADCOUNT_FIELD_NUMBER: _ClassVar[int]
    COMMONSTREAMRESPONSE_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAMSCHEMATYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    activeThreadCount: _containers.RepeatedScalarFieldContainer[int]
    commonStreamResponse: PCmdStreamResponse
    histogramSchemaType: int
    timeStamp: int
    def __init__(self, commonStreamResponse: _Optional[_Union[PCmdStreamResponse, _Mapping]] = ..., histogramSchemaType: _Optional[int] = ..., activeThreadCount: _Optional[_Iterable[int]] = ..., timeStamp: _Optional[int] = ...) -> None: ...

class PCmdActiveThreadDump(_message.Message):
    __slots__ = ["limit", "localTraceId", "threadName"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCALTRACEID_FIELD_NUMBER: _ClassVar[int]
    THREADNAME_FIELD_NUMBER: _ClassVar[int]
    limit: int
    localTraceId: _containers.RepeatedScalarFieldContainer[int]
    threadName: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, limit: _Optional[int] = ..., threadName: _Optional[_Iterable[str]] = ..., localTraceId: _Optional[_Iterable[int]] = ...) -> None: ...

class PCmdActiveThreadDumpRes(_message.Message):
    __slots__ = ["commonResponse", "subType", "threadDump", "type", "version"]
    COMMONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    THREADDUMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    commonResponse: PCmdResponse
    subType: str
    threadDump: _containers.RepeatedCompositeFieldContainer[_ThreadDump_pb2.PActiveThreadDump]
    type: str
    version: str
    def __init__(self, commonResponse: _Optional[_Union[PCmdResponse, _Mapping]] = ..., threadDump: _Optional[_Iterable[_Union[_ThreadDump_pb2.PActiveThreadDump, _Mapping]]] = ..., type: _Optional[str] = ..., subType: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class PCmdActiveThreadLightDump(_message.Message):
    __slots__ = ["limit", "localTraceId", "threadName"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOCALTRACEID_FIELD_NUMBER: _ClassVar[int]
    THREADNAME_FIELD_NUMBER: _ClassVar[int]
    limit: int
    localTraceId: _containers.RepeatedScalarFieldContainer[int]
    threadName: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, limit: _Optional[int] = ..., threadName: _Optional[_Iterable[str]] = ..., localTraceId: _Optional[_Iterable[int]] = ...) -> None: ...

class PCmdActiveThreadLightDumpRes(_message.Message):
    __slots__ = ["commonResponse", "subType", "threadDump", "type", "version"]
    COMMONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    THREADDUMP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    commonResponse: PCmdResponse
    subType: str
    threadDump: _containers.RepeatedCompositeFieldContainer[_ThreadDump_pb2.PActiveThreadLightDump]
    type: str
    version: str
    def __init__(self, commonResponse: _Optional[_Union[PCmdResponse, _Mapping]] = ..., threadDump: _Optional[_Iterable[_Union[_ThreadDump_pb2.PActiveThreadLightDump, _Mapping]]] = ..., type: _Optional[str] = ..., subType: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class PCmdEcho(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class PCmdEchoResponse(_message.Message):
    __slots__ = ["commonResponse", "message"]
    COMMONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    commonResponse: PCmdResponse
    message: str
    def __init__(self, commonResponse: _Optional[_Union[PCmdResponse, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class PCmdMessage(_message.Message):
    __slots__ = ["failMessage", "handshakeMessage"]
    FAILMESSAGE_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKEMESSAGE_FIELD_NUMBER: _ClassVar[int]
    failMessage: PCmdResponse
    handshakeMessage: PCmdServiceHandshake
    def __init__(self, handshakeMessage: _Optional[_Union[PCmdServiceHandshake, _Mapping]] = ..., failMessage: _Optional[_Union[PCmdResponse, _Mapping]] = ...) -> None: ...

class PCmdRequest(_message.Message):
    __slots__ = ["commandActiveThreadCount", "commandActiveThreadDump", "commandActiveThreadLightDump", "commandEcho", "requestId"]
    COMMANDACTIVETHREADCOUNT_FIELD_NUMBER: _ClassVar[int]
    COMMANDACTIVETHREADDUMP_FIELD_NUMBER: _ClassVar[int]
    COMMANDACTIVETHREADLIGHTDUMP_FIELD_NUMBER: _ClassVar[int]
    COMMANDECHO_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    commandActiveThreadCount: PCmdActiveThreadCount
    commandActiveThreadDump: PCmdActiveThreadDump
    commandActiveThreadLightDump: PCmdActiveThreadLightDump
    commandEcho: PCmdEcho
    requestId: int
    def __init__(self, requestId: _Optional[int] = ..., commandEcho: _Optional[_Union[PCmdEcho, _Mapping]] = ..., commandActiveThreadCount: _Optional[_Union[PCmdActiveThreadCount, _Mapping]] = ..., commandActiveThreadDump: _Optional[_Union[PCmdActiveThreadDump, _Mapping]] = ..., commandActiveThreadLightDump: _Optional[_Union[PCmdActiveThreadLightDump, _Mapping]] = ...) -> None: ...

class PCmdResponse(_message.Message):
    __slots__ = ["message", "responseId", "status"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSEID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    message: _wrappers_pb2.StringValue
    responseId: int
    status: int
    def __init__(self, responseId: _Optional[int] = ..., status: _Optional[int] = ..., message: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PCmdServiceHandshake(_message.Message):
    __slots__ = ["supportCommandServiceKey"]
    SUPPORTCOMMANDSERVICEKEY_FIELD_NUMBER: _ClassVar[int]
    supportCommandServiceKey: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, supportCommandServiceKey: _Optional[_Iterable[int]] = ...) -> None: ...

class PCmdStreamResponse(_message.Message):
    __slots__ = ["message", "responseId", "sequenceId"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSEID_FIELD_NUMBER: _ClassVar[int]
    SEQUENCEID_FIELD_NUMBER: _ClassVar[int]
    message: _wrappers_pb2.StringValue
    responseId: int
    sequenceId: int
    def __init__(self, responseId: _Optional[int] = ..., sequenceId: _Optional[int] = ..., message: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PCommandType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
