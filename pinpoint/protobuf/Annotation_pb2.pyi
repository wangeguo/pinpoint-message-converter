from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PAnnotation(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: int
    value: PAnnotationValue
    def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PAnnotationValue, _Mapping]] = ...) -> None: ...

class PAnnotationValue(_message.Message):
    __slots__ = ["binaryValue", "boolValue", "byteValue", "doubleValue", "intBooleanIntBooleanValue", "intStringStringValue", "intStringValue", "intValue", "longIntIntByteByteStringValue", "longValue", "shortValue", "stringStringValue", "stringValue"]
    BINARYVALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLVALUE_FIELD_NUMBER: _ClassVar[int]
    BYTEVALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLEVALUE_FIELD_NUMBER: _ClassVar[int]
    INTBOOLEANINTBOOLEANVALUE_FIELD_NUMBER: _ClassVar[int]
    INTSTRINGSTRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    INTSTRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGINTINTBYTEBYTESTRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    SHORTVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGSTRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    binaryValue: bytes
    boolValue: bool
    byteValue: int
    doubleValue: float
    intBooleanIntBooleanValue: PIntBooleanIntBooleanValue
    intStringStringValue: PIntStringStringValue
    intStringValue: PIntStringValue
    intValue: int
    longIntIntByteByteStringValue: PLongIntIntByteByteStringValue
    longValue: int
    shortValue: int
    stringStringValue: PStringStringValue
    stringValue: str
    def __init__(self, stringValue: _Optional[str] = ..., boolValue: bool = ..., intValue: _Optional[int] = ..., longValue: _Optional[int] = ..., shortValue: _Optional[int] = ..., doubleValue: _Optional[float] = ..., binaryValue: _Optional[bytes] = ..., byteValue: _Optional[int] = ..., intStringValue: _Optional[_Union[PIntStringValue, _Mapping]] = ..., stringStringValue: _Optional[_Union[PStringStringValue, _Mapping]] = ..., intStringStringValue: _Optional[_Union[PIntStringStringValue, _Mapping]] = ..., longIntIntByteByteStringValue: _Optional[_Union[PLongIntIntByteByteStringValue, _Mapping]] = ..., intBooleanIntBooleanValue: _Optional[_Union[PIntBooleanIntBooleanValue, _Mapping]] = ...) -> None: ...

class PIntBooleanIntBooleanValue(_message.Message):
    __slots__ = ["boolValue1", "boolValue2", "intValue1", "intValue2"]
    BOOLVALUE1_FIELD_NUMBER: _ClassVar[int]
    BOOLVALUE2_FIELD_NUMBER: _ClassVar[int]
    INTVALUE1_FIELD_NUMBER: _ClassVar[int]
    INTVALUE2_FIELD_NUMBER: _ClassVar[int]
    boolValue1: bool
    boolValue2: bool
    intValue1: int
    intValue2: int
    def __init__(self, intValue1: _Optional[int] = ..., boolValue1: bool = ..., intValue2: _Optional[int] = ..., boolValue2: bool = ...) -> None: ...

class PIntStringStringValue(_message.Message):
    __slots__ = ["intValue", "stringValue1", "stringValue2"]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE1_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE2_FIELD_NUMBER: _ClassVar[int]
    intValue: int
    stringValue1: _wrappers_pb2.StringValue
    stringValue2: _wrappers_pb2.StringValue
    def __init__(self, intValue: _Optional[int] = ..., stringValue1: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., stringValue2: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PIntStringValue(_message.Message):
    __slots__ = ["intValue", "stringValue"]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    intValue: int
    stringValue: _wrappers_pb2.StringValue
    def __init__(self, intValue: _Optional[int] = ..., stringValue: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PLongIntIntByteByteStringValue(_message.Message):
    __slots__ = ["byteValue1", "byteValue2", "intValue1", "intValue2", "longValue", "stringValue"]
    BYTEVALUE1_FIELD_NUMBER: _ClassVar[int]
    BYTEVALUE2_FIELD_NUMBER: _ClassVar[int]
    INTVALUE1_FIELD_NUMBER: _ClassVar[int]
    INTVALUE2_FIELD_NUMBER: _ClassVar[int]
    LONGVALUE_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE_FIELD_NUMBER: _ClassVar[int]
    byteValue1: int
    byteValue2: int
    intValue1: int
    intValue2: int
    longValue: int
    stringValue: _wrappers_pb2.StringValue
    def __init__(self, longValue: _Optional[int] = ..., intValue1: _Optional[int] = ..., intValue2: _Optional[int] = ..., byteValue1: _Optional[int] = ..., byteValue2: _Optional[int] = ..., stringValue: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PStringStringValue(_message.Message):
    __slots__ = ["stringValue1", "stringValue2"]
    STRINGVALUE1_FIELD_NUMBER: _ClassVar[int]
    STRINGVALUE2_FIELD_NUMBER: _ClassVar[int]
    stringValue1: _wrappers_pb2.StringValue
    stringValue2: _wrappers_pb2.StringValue
    def __init__(self, stringValue1: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., stringValue2: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
