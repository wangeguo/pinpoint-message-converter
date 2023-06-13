from v1 import ThreadDump_pb2 as _ThreadDump_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
JVM_GC_TYPE_CMS: PJvmGcType
JVM_GC_TYPE_G1: PJvmGcType
JVM_GC_TYPE_PARALLEL: PJvmGcType
JVM_GC_TYPE_SERIAL: PJvmGcType
JVM_GC_TYPE_UNKNOWN: PJvmGcType

class PActiveTrace(_message.Message):
    __slots__ = ["histogram"]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    histogram: PActiveTraceHistogram
    def __init__(self, histogram: _Optional[_Union[PActiveTraceHistogram, _Mapping]] = ...) -> None: ...

class PActiveTraceHistogram(_message.Message):
    __slots__ = ["activeTraceCount", "histogramSchemaType", "version"]
    ACTIVETRACECOUNT_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAMSCHEMATYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    activeTraceCount: _containers.RepeatedScalarFieldContainer[int]
    histogramSchemaType: int
    version: int
    def __init__(self, version: _Optional[int] = ..., histogramSchemaType: _Optional[int] = ..., activeTraceCount: _Optional[_Iterable[int]] = ...) -> None: ...

class PAgentInfo(_message.Message):
    __slots__ = ["agentVersion", "container", "endStatus", "endTimestamp", "hostname", "ip", "jvmInfo", "pid", "ports", "serverMetaData", "serviceType", "vmVersion"]
    AGENTVERSION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ENDSTATUS_FIELD_NUMBER: _ClassVar[int]
    ENDTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    JVMINFO_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    SERVERMETADATA_FIELD_NUMBER: _ClassVar[int]
    SERVICETYPE_FIELD_NUMBER: _ClassVar[int]
    VMVERSION_FIELD_NUMBER: _ClassVar[int]
    agentVersion: str
    container: bool
    endStatus: int
    endTimestamp: int
    hostname: str
    ip: str
    jvmInfo: PJvmInfo
    pid: int
    ports: str
    serverMetaData: PServerMetaData
    serviceType: int
    vmVersion: str
    def __init__(self, hostname: _Optional[str] = ..., ip: _Optional[str] = ..., ports: _Optional[str] = ..., serviceType: _Optional[int] = ..., pid: _Optional[int] = ..., agentVersion: _Optional[str] = ..., vmVersion: _Optional[str] = ..., endTimestamp: _Optional[int] = ..., endStatus: _Optional[int] = ..., serverMetaData: _Optional[_Union[PServerMetaData, _Mapping]] = ..., jvmInfo: _Optional[_Union[PJvmInfo, _Mapping]] = ..., container: bool = ...) -> None: ...

class PAgentStat(_message.Message):
    __slots__ = ["activeTrace", "collectInterval", "cpuLoad", "dataSourceList", "deadlock", "directBuffer", "fileDescriptor", "gc", "loadedClass", "metadata", "responseTime", "timestamp", "totalThread", "transaction"]
    ACTIVETRACE_FIELD_NUMBER: _ClassVar[int]
    COLLECTINTERVAL_FIELD_NUMBER: _ClassVar[int]
    CPULOAD_FIELD_NUMBER: _ClassVar[int]
    DATASOURCELIST_FIELD_NUMBER: _ClassVar[int]
    DEADLOCK_FIELD_NUMBER: _ClassVar[int]
    DIRECTBUFFER_FIELD_NUMBER: _ClassVar[int]
    FILEDESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
    GC_FIELD_NUMBER: _ClassVar[int]
    LOADEDCLASS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RESPONSETIME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TOTALTHREAD_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    activeTrace: PActiveTrace
    collectInterval: int
    cpuLoad: PCpuLoad
    dataSourceList: PDataSourceList
    deadlock: PDeadlock
    directBuffer: PDirectBuffer
    fileDescriptor: PFileDescriptor
    gc: PJvmGc
    loadedClass: PLoadedClass
    metadata: str
    responseTime: PResponseTime
    timestamp: int
    totalThread: PTotalThread
    transaction: PTransaction
    def __init__(self, timestamp: _Optional[int] = ..., collectInterval: _Optional[int] = ..., gc: _Optional[_Union[PJvmGc, _Mapping]] = ..., cpuLoad: _Optional[_Union[PCpuLoad, _Mapping]] = ..., transaction: _Optional[_Union[PTransaction, _Mapping]] = ..., activeTrace: _Optional[_Union[PActiveTrace, _Mapping]] = ..., dataSourceList: _Optional[_Union[PDataSourceList, _Mapping]] = ..., responseTime: _Optional[_Union[PResponseTime, _Mapping]] = ..., deadlock: _Optional[_Union[PDeadlock, _Mapping]] = ..., fileDescriptor: _Optional[_Union[PFileDescriptor, _Mapping]] = ..., directBuffer: _Optional[_Union[PDirectBuffer, _Mapping]] = ..., metadata: _Optional[str] = ..., totalThread: _Optional[_Union[PTotalThread, _Mapping]] = ..., loadedClass: _Optional[_Union[PLoadedClass, _Mapping]] = ...) -> None: ...

class PAgentStatBatch(_message.Message):
    __slots__ = ["agentStat"]
    AGENTSTAT_FIELD_NUMBER: _ClassVar[int]
    agentStat: _containers.RepeatedCompositeFieldContainer[PAgentStat]
    def __init__(self, agentStat: _Optional[_Iterable[_Union[PAgentStat, _Mapping]]] = ...) -> None: ...

class PAgentUriStat(_message.Message):
    __slots__ = ["bucketVersion", "eachUriStat", "timestamp"]
    BUCKETVERSION_FIELD_NUMBER: _ClassVar[int]
    EACHURISTAT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    bucketVersion: int
    eachUriStat: _containers.RepeatedCompositeFieldContainer[PEachUriStat]
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ..., bucketVersion: _Optional[int] = ..., eachUriStat: _Optional[_Iterable[_Union[PEachUriStat, _Mapping]]] = ...) -> None: ...

class PCpuLoad(_message.Message):
    __slots__ = ["jvmCpuLoad", "systemCpuLoad"]
    JVMCPULOAD_FIELD_NUMBER: _ClassVar[int]
    SYSTEMCPULOAD_FIELD_NUMBER: _ClassVar[int]
    jvmCpuLoad: float
    systemCpuLoad: float
    def __init__(self, jvmCpuLoad: _Optional[float] = ..., systemCpuLoad: _Optional[float] = ...) -> None: ...

class PDataSource(_message.Message):
    __slots__ = ["activeConnectionSize", "databaseName", "id", "maxConnectionSize", "serviceTypeCode", "url"]
    ACTIVECONNECTIONSIZE_FIELD_NUMBER: _ClassVar[int]
    DATABASENAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MAXCONNECTIONSIZE_FIELD_NUMBER: _ClassVar[int]
    SERVICETYPECODE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    activeConnectionSize: int
    databaseName: str
    id: int
    maxConnectionSize: int
    serviceTypeCode: int
    url: str
    def __init__(self, id: _Optional[int] = ..., serviceTypeCode: _Optional[int] = ..., databaseName: _Optional[str] = ..., url: _Optional[str] = ..., activeConnectionSize: _Optional[int] = ..., maxConnectionSize: _Optional[int] = ...) -> None: ...

class PDataSourceList(_message.Message):
    __slots__ = ["dataSource"]
    DATASOURCE_FIELD_NUMBER: _ClassVar[int]
    dataSource: _containers.RepeatedCompositeFieldContainer[PDataSource]
    def __init__(self, dataSource: _Optional[_Iterable[_Union[PDataSource, _Mapping]]] = ...) -> None: ...

class PDeadlock(_message.Message):
    __slots__ = ["count", "threadDump"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    THREADDUMP_FIELD_NUMBER: _ClassVar[int]
    count: int
    threadDump: _containers.RepeatedCompositeFieldContainer[_ThreadDump_pb2.PThreadDump]
    def __init__(self, count: _Optional[int] = ..., threadDump: _Optional[_Iterable[_Union[_ThreadDump_pb2.PThreadDump, _Mapping]]] = ...) -> None: ...

class PDirectBuffer(_message.Message):
    __slots__ = ["directCount", "directMemoryUsed", "mappedCount", "mappedMemoryUsed"]
    DIRECTCOUNT_FIELD_NUMBER: _ClassVar[int]
    DIRECTMEMORYUSED_FIELD_NUMBER: _ClassVar[int]
    MAPPEDCOUNT_FIELD_NUMBER: _ClassVar[int]
    MAPPEDMEMORYUSED_FIELD_NUMBER: _ClassVar[int]
    directCount: int
    directMemoryUsed: int
    mappedCount: int
    mappedMemoryUsed: int
    def __init__(self, directCount: _Optional[int] = ..., directMemoryUsed: _Optional[int] = ..., mappedCount: _Optional[int] = ..., mappedMemoryUsed: _Optional[int] = ...) -> None: ...

class PEachUriStat(_message.Message):
    __slots__ = ["failedHistogram", "totalHistogram", "uri"]
    FAILEDHISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    TOTALHISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    failedHistogram: PUriHistogram
    totalHistogram: PUriHistogram
    uri: str
    def __init__(self, uri: _Optional[str] = ..., totalHistogram: _Optional[_Union[PUriHistogram, _Mapping]] = ..., failedHistogram: _Optional[_Union[PUriHistogram, _Mapping]] = ...) -> None: ...

class PFileDescriptor(_message.Message):
    __slots__ = ["openFileDescriptorCount"]
    OPENFILEDESCRIPTORCOUNT_FIELD_NUMBER: _ClassVar[int]
    openFileDescriptorCount: int
    def __init__(self, openFileDescriptorCount: _Optional[int] = ...) -> None: ...

class PJvmGc(_message.Message):
    __slots__ = ["jvmGcDetailed", "jvmGcOldCount", "jvmGcOldTime", "jvmMemoryHeapMax", "jvmMemoryHeapUsed", "jvmMemoryNonHeapMax", "jvmMemoryNonHeapUsed", "type"]
    JVMGCDETAILED_FIELD_NUMBER: _ClassVar[int]
    JVMGCOLDCOUNT_FIELD_NUMBER: _ClassVar[int]
    JVMGCOLDTIME_FIELD_NUMBER: _ClassVar[int]
    JVMMEMORYHEAPMAX_FIELD_NUMBER: _ClassVar[int]
    JVMMEMORYHEAPUSED_FIELD_NUMBER: _ClassVar[int]
    JVMMEMORYNONHEAPMAX_FIELD_NUMBER: _ClassVar[int]
    JVMMEMORYNONHEAPUSED_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    jvmGcDetailed: PJvmGcDetailed
    jvmGcOldCount: int
    jvmGcOldTime: int
    jvmMemoryHeapMax: int
    jvmMemoryHeapUsed: int
    jvmMemoryNonHeapMax: int
    jvmMemoryNonHeapUsed: int
    type: PJvmGcType
    def __init__(self, type: _Optional[_Union[PJvmGcType, str]] = ..., jvmMemoryHeapUsed: _Optional[int] = ..., jvmMemoryHeapMax: _Optional[int] = ..., jvmMemoryNonHeapUsed: _Optional[int] = ..., jvmMemoryNonHeapMax: _Optional[int] = ..., jvmGcOldCount: _Optional[int] = ..., jvmGcOldTime: _Optional[int] = ..., jvmGcDetailed: _Optional[_Union[PJvmGcDetailed, _Mapping]] = ...) -> None: ...

class PJvmGcDetailed(_message.Message):
    __slots__ = ["jvmGcNewCount", "jvmGcNewTime", "jvmPoolCodeCacheUsed", "jvmPoolMetaspaceUsed", "jvmPoolNewGenUsed", "jvmPoolOldGenUsed", "jvmPoolPermGenUsed", "jvmPoolSurvivorSpaceUsed"]
    JVMGCNEWCOUNT_FIELD_NUMBER: _ClassVar[int]
    JVMGCNEWTIME_FIELD_NUMBER: _ClassVar[int]
    JVMPOOLCODECACHEUSED_FIELD_NUMBER: _ClassVar[int]
    JVMPOOLMETASPACEUSED_FIELD_NUMBER: _ClassVar[int]
    JVMPOOLNEWGENUSED_FIELD_NUMBER: _ClassVar[int]
    JVMPOOLOLDGENUSED_FIELD_NUMBER: _ClassVar[int]
    JVMPOOLPERMGENUSED_FIELD_NUMBER: _ClassVar[int]
    JVMPOOLSURVIVORSPACEUSED_FIELD_NUMBER: _ClassVar[int]
    jvmGcNewCount: int
    jvmGcNewTime: int
    jvmPoolCodeCacheUsed: float
    jvmPoolMetaspaceUsed: float
    jvmPoolNewGenUsed: float
    jvmPoolOldGenUsed: float
    jvmPoolPermGenUsed: float
    jvmPoolSurvivorSpaceUsed: float
    def __init__(self, jvmGcNewCount: _Optional[int] = ..., jvmGcNewTime: _Optional[int] = ..., jvmPoolCodeCacheUsed: _Optional[float] = ..., jvmPoolNewGenUsed: _Optional[float] = ..., jvmPoolOldGenUsed: _Optional[float] = ..., jvmPoolSurvivorSpaceUsed: _Optional[float] = ..., jvmPoolPermGenUsed: _Optional[float] = ..., jvmPoolMetaspaceUsed: _Optional[float] = ...) -> None: ...

class PJvmInfo(_message.Message):
    __slots__ = ["gcType", "version", "vmVersion"]
    GCTYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VMVERSION_FIELD_NUMBER: _ClassVar[int]
    gcType: PJvmGcType
    version: int
    vmVersion: str
    def __init__(self, version: _Optional[int] = ..., vmVersion: _Optional[str] = ..., gcType: _Optional[_Union[PJvmGcType, str]] = ...) -> None: ...

class PLoadedClass(_message.Message):
    __slots__ = ["loadedClassCount", "unloadedClassCount"]
    LOADEDCLASSCOUNT_FIELD_NUMBER: _ClassVar[int]
    UNLOADEDCLASSCOUNT_FIELD_NUMBER: _ClassVar[int]
    loadedClassCount: int
    unloadedClassCount: int
    def __init__(self, loadedClassCount: _Optional[int] = ..., unloadedClassCount: _Optional[int] = ...) -> None: ...

class PPing(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PResponseTime(_message.Message):
    __slots__ = ["avg", "max"]
    AVG_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    avg: int
    max: int
    def __init__(self, avg: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...

class PServerMetaData(_message.Message):
    __slots__ = ["serverInfo", "serviceInfo", "vmArg"]
    SERVERINFO_FIELD_NUMBER: _ClassVar[int]
    SERVICEINFO_FIELD_NUMBER: _ClassVar[int]
    VMARG_FIELD_NUMBER: _ClassVar[int]
    serverInfo: str
    serviceInfo: _containers.RepeatedCompositeFieldContainer[PServiceInfo]
    vmArg: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, serverInfo: _Optional[str] = ..., vmArg: _Optional[_Iterable[str]] = ..., serviceInfo: _Optional[_Iterable[_Union[PServiceInfo, _Mapping]]] = ...) -> None: ...

class PServiceInfo(_message.Message):
    __slots__ = ["serviceLib", "serviceName"]
    SERVICELIB_FIELD_NUMBER: _ClassVar[int]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    serviceLib: _containers.RepeatedScalarFieldContainer[str]
    serviceName: str
    def __init__(self, serviceName: _Optional[str] = ..., serviceLib: _Optional[_Iterable[str]] = ...) -> None: ...

class PStatMessage(_message.Message):
    __slots__ = ["agentStat", "agentStatBatch", "agentUriStat"]
    AGENTSTATBATCH_FIELD_NUMBER: _ClassVar[int]
    AGENTSTAT_FIELD_NUMBER: _ClassVar[int]
    AGENTURISTAT_FIELD_NUMBER: _ClassVar[int]
    agentStat: PAgentStat
    agentStatBatch: PAgentStatBatch
    agentUriStat: PAgentUriStat
    def __init__(self, agentStat: _Optional[_Union[PAgentStat, _Mapping]] = ..., agentStatBatch: _Optional[_Union[PAgentStatBatch, _Mapping]] = ..., agentUriStat: _Optional[_Union[PAgentUriStat, _Mapping]] = ...) -> None: ...

class PTotalThread(_message.Message):
    __slots__ = ["totalThreadCount"]
    TOTALTHREADCOUNT_FIELD_NUMBER: _ClassVar[int]
    totalThreadCount: int
    def __init__(self, totalThreadCount: _Optional[int] = ...) -> None: ...

class PTransaction(_message.Message):
    __slots__ = ["sampledContinuationCount", "sampledNewCount", "skippedContinuationCount", "skippedNewCount", "unsampledContinuationCount", "unsampledNewCount"]
    SAMPLEDCONTINUATIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLEDNEWCOUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPEDCONTINUATIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPEDNEWCOUNT_FIELD_NUMBER: _ClassVar[int]
    UNSAMPLEDCONTINUATIONCOUNT_FIELD_NUMBER: _ClassVar[int]
    UNSAMPLEDNEWCOUNT_FIELD_NUMBER: _ClassVar[int]
    sampledContinuationCount: int
    sampledNewCount: int
    skippedContinuationCount: int
    skippedNewCount: int
    unsampledContinuationCount: int
    unsampledNewCount: int
    def __init__(self, sampledNewCount: _Optional[int] = ..., sampledContinuationCount: _Optional[int] = ..., unsampledNewCount: _Optional[int] = ..., unsampledContinuationCount: _Optional[int] = ..., skippedNewCount: _Optional[int] = ..., skippedContinuationCount: _Optional[int] = ...) -> None: ...

class PUriHistogram(_message.Message):
    __slots__ = ["avg", "count", "histogram", "max"]
    AVG_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    avg: float
    count: int
    histogram: _containers.RepeatedScalarFieldContainer[int]
    max: int
    def __init__(self, count: _Optional[int] = ..., avg: _Optional[float] = ..., max: _Optional[int] = ..., histogram: _Optional[_Iterable[int]] = ...) -> None: ...

class PJvmGcType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
