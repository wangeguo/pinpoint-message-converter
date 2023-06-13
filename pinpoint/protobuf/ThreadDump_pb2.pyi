from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
PENDING: PThreadDumpType
TARGET: PThreadDumpType
THREAD_STATE_BLOCKED: PThreadState
THREAD_STATE_NEW: PThreadState
THREAD_STATE_RUNNABLE: PThreadState
THREAD_STATE_TERMINATED: PThreadState
THREAD_STATE_TIMED_WAITING: PThreadState
THREAD_STATE_UNKNOWN: PThreadState
THREAD_STATE_WAITING: PThreadState

class PActiveThreadDump(_message.Message):
    __slots__ = ["entryPoint", "localTraceId", "sampled", "startTime", "threadDump", "transactionId"]
    ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    LOCALTRACEID_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    THREADDUMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    entryPoint: str
    localTraceId: int
    sampled: bool
    startTime: int
    threadDump: PThreadDump
    transactionId: str
    def __init__(self, startTime: _Optional[int] = ..., localTraceId: _Optional[int] = ..., threadDump: _Optional[_Union[PThreadDump, _Mapping]] = ..., sampled: bool = ..., transactionId: _Optional[str] = ..., entryPoint: _Optional[str] = ...) -> None: ...

class PActiveThreadLightDump(_message.Message):
    __slots__ = ["entryPoint", "localTraceId", "sampled", "startTime", "threadDump", "transactionId"]
    ENTRYPOINT_FIELD_NUMBER: _ClassVar[int]
    LOCALTRACEID_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    THREADDUMP_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    entryPoint: str
    localTraceId: int
    sampled: bool
    startTime: int
    threadDump: PThreadLightDump
    transactionId: str
    def __init__(self, startTime: _Optional[int] = ..., localTraceId: _Optional[int] = ..., threadDump: _Optional[_Union[PThreadLightDump, _Mapping]] = ..., sampled: bool = ..., transactionId: _Optional[str] = ..., entryPoint: _Optional[str] = ...) -> None: ...

class PMonitorInfo(_message.Message):
    __slots__ = ["stackDepth", "stackFrame"]
    STACKDEPTH_FIELD_NUMBER: _ClassVar[int]
    STACKFRAME_FIELD_NUMBER: _ClassVar[int]
    stackDepth: int
    stackFrame: str
    def __init__(self, stackDepth: _Optional[int] = ..., stackFrame: _Optional[str] = ...) -> None: ...

class PThreadDump(_message.Message):
    __slots__ = ["blockedCount", "blockedTime", "inNative", "lockName", "lockOwnerId", "lockOwnerName", "lockedMonitor", "lockedSynchronizer", "stackTrace", "suspended", "threadId", "threadName", "threadState", "waitedCount", "waitedTime"]
    BLOCKEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKEDTIME_FIELD_NUMBER: _ClassVar[int]
    INNATIVE_FIELD_NUMBER: _ClassVar[int]
    LOCKEDMONITOR_FIELD_NUMBER: _ClassVar[int]
    LOCKEDSYNCHRONIZER_FIELD_NUMBER: _ClassVar[int]
    LOCKNAME_FIELD_NUMBER: _ClassVar[int]
    LOCKOWNERID_FIELD_NUMBER: _ClassVar[int]
    LOCKOWNERNAME_FIELD_NUMBER: _ClassVar[int]
    STACKTRACE_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    THREADID_FIELD_NUMBER: _ClassVar[int]
    THREADNAME_FIELD_NUMBER: _ClassVar[int]
    THREADSTATE_FIELD_NUMBER: _ClassVar[int]
    WAITEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    WAITEDTIME_FIELD_NUMBER: _ClassVar[int]
    blockedCount: int
    blockedTime: int
    inNative: bool
    lockName: str
    lockOwnerId: int
    lockOwnerName: str
    lockedMonitor: _containers.RepeatedCompositeFieldContainer[PMonitorInfo]
    lockedSynchronizer: _containers.RepeatedScalarFieldContainer[str]
    stackTrace: _containers.RepeatedScalarFieldContainer[str]
    suspended: bool
    threadId: int
    threadName: str
    threadState: PThreadState
    waitedCount: int
    waitedTime: int
    def __init__(self, threadName: _Optional[str] = ..., threadId: _Optional[int] = ..., blockedTime: _Optional[int] = ..., blockedCount: _Optional[int] = ..., waitedTime: _Optional[int] = ..., waitedCount: _Optional[int] = ..., lockName: _Optional[str] = ..., lockOwnerId: _Optional[int] = ..., lockOwnerName: _Optional[str] = ..., inNative: bool = ..., suspended: bool = ..., threadState: _Optional[_Union[PThreadState, str]] = ..., stackTrace: _Optional[_Iterable[str]] = ..., lockedMonitor: _Optional[_Iterable[_Union[PMonitorInfo, _Mapping]]] = ..., lockedSynchronizer: _Optional[_Iterable[str]] = ...) -> None: ...

class PThreadLightDump(_message.Message):
    __slots__ = ["threadId", "threadName", "threadState"]
    THREADID_FIELD_NUMBER: _ClassVar[int]
    THREADNAME_FIELD_NUMBER: _ClassVar[int]
    THREADSTATE_FIELD_NUMBER: _ClassVar[int]
    threadId: int
    threadName: str
    threadState: PThreadState
    def __init__(self, threadName: _Optional[str] = ..., threadId: _Optional[int] = ..., threadState: _Optional[_Union[PThreadState, str]] = ...) -> None: ...

class PThreadState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PThreadDumpType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
