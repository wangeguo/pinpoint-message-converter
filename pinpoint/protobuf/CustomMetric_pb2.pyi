from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PCustomMetric(_message.Message):
    __slots__ = ["doubleGaugeMetric", "intCountMetric", "intGaugeMetric", "longCountMetric", "longGaugeMetric"]
    DOUBLEGAUGEMETRIC_FIELD_NUMBER: _ClassVar[int]
    INTCOUNTMETRIC_FIELD_NUMBER: _ClassVar[int]
    INTGAUGEMETRIC_FIELD_NUMBER: _ClassVar[int]
    LONGCOUNTMETRIC_FIELD_NUMBER: _ClassVar[int]
    LONGGAUGEMETRIC_FIELD_NUMBER: _ClassVar[int]
    doubleGaugeMetric: PDouleGaugeMetric
    intCountMetric: PIntCountMetric
    intGaugeMetric: PIntGaugeMetric
    longCountMetric: PLongCountMetric
    longGaugeMetric: PLongGaugeMetric
    def __init__(self, intCountMetric: _Optional[_Union[PIntCountMetric, _Mapping]] = ..., longCountMetric: _Optional[_Union[PLongCountMetric, _Mapping]] = ..., intGaugeMetric: _Optional[_Union[PIntGaugeMetric, _Mapping]] = ..., longGaugeMetric: _Optional[_Union[PLongGaugeMetric, _Mapping]] = ..., doubleGaugeMetric: _Optional[_Union[PDouleGaugeMetric, _Mapping]] = ...) -> None: ...

class PCustomMetricMessage(_message.Message):
    __slots__ = ["collectInterval", "customMetrics", "timestamp"]
    COLLECTINTERVAL_FIELD_NUMBER: _ClassVar[int]
    CUSTOMMETRICS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    collectInterval: _containers.RepeatedScalarFieldContainer[int]
    customMetrics: _containers.RepeatedCompositeFieldContainer[PCustomMetric]
    timestamp: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, timestamp: _Optional[_Iterable[int]] = ..., collectInterval: _Optional[_Iterable[int]] = ..., customMetrics: _Optional[_Iterable[_Union[PCustomMetric, _Mapping]]] = ...) -> None: ...

class PDoubleValue(_message.Message):
    __slots__ = ["isNotSet", "value"]
    ISNOTSET_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    isNotSet: bool
    value: float
    def __init__(self, value: _Optional[float] = ..., isNotSet: bool = ...) -> None: ...

class PDouleGaugeMetric(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedCompositeFieldContainer[PDoubleValue]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[PDoubleValue, _Mapping]]] = ...) -> None: ...

class PIntCountMetric(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedCompositeFieldContainer[PIntValue]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[PIntValue, _Mapping]]] = ...) -> None: ...

class PIntGaugeMetric(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedCompositeFieldContainer[PIntValue]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[PIntValue, _Mapping]]] = ...) -> None: ...

class PIntValue(_message.Message):
    __slots__ = ["isNotSet", "value"]
    ISNOTSET_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    isNotSet: bool
    value: int
    def __init__(self, value: _Optional[int] = ..., isNotSet: bool = ...) -> None: ...

class PLongCountMetric(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedCompositeFieldContainer[PLongValue]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[PLongValue, _Mapping]]] = ...) -> None: ...

class PLongGaugeMetric(_message.Message):
    __slots__ = ["name", "values"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedCompositeFieldContainer[PLongValue]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[PLongValue, _Mapping]]] = ...) -> None: ...

class PLongValue(_message.Message):
    __slots__ = ["isNotSet", "value"]
    ISNOTSET_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    isNotSet: bool
    value: int
    def __init__(self, value: _Optional[int] = ..., isNotSet: bool = ...) -> None: ...
