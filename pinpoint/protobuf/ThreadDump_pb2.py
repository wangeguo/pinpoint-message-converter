# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/ThreadDump.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13v1/ThreadDump.proto\x12\x02v1\"6\n\x0cPMonitorInfo\x12\x12\n\nstackDepth\x18\x01 \x01(\x05\x12\x12\n\nstackFrame\x18\x02 \x01(\t\"\xea\x02\n\x0bPThreadDump\x12\x12\n\nthreadName\x18\x01 \x01(\t\x12\x10\n\x08threadId\x18\x02 \x01(\x03\x12\x13\n\x0b\x62lockedTime\x18\x03 \x01(\x03\x12\x14\n\x0c\x62lockedCount\x18\x04 \x01(\x03\x12\x12\n\nwaitedTime\x18\x05 \x01(\x03\x12\x13\n\x0bwaitedCount\x18\x06 \x01(\x03\x12\x10\n\x08lockName\x18\x07 \x01(\t\x12\x13\n\x0blockOwnerId\x18\x08 \x01(\x03\x12\x15\n\rlockOwnerName\x18\t \x01(\t\x12\x10\n\x08inNative\x18\n \x01(\x08\x12\x11\n\tsuspended\x18\x0b \x01(\x08\x12%\n\x0bthreadState\x18\x0c \x01(\x0e\x32\x10.v1.PThreadState\x12\x12\n\nstackTrace\x18\r \x03(\t\x12\'\n\rlockedMonitor\x18\x0e \x03(\x0b\x32\x10.v1.PMonitorInfo\x12\x1a\n\x12lockedSynchronizer\x18\x0f \x03(\t\"_\n\x10PThreadLightDump\x12\x12\n\nthreadName\x18\x01 \x01(\t\x12\x10\n\x08threadId\x18\x02 \x01(\x03\x12%\n\x0bthreadState\x18\x03 \x01(\x0e\x32\x10.v1.PThreadState\"\x9d\x01\n\x11PActiveThreadDump\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\x14\n\x0clocalTraceId\x18\x02 \x01(\x03\x12#\n\nthreadDump\x18\x03 \x01(\x0b\x32\x0f.v1.PThreadDump\x12\x0f\n\x07sampled\x18\x04 \x01(\x08\x12\x15\n\rtransactionId\x18\x05 \x01(\t\x12\x12\n\nentryPoint\x18\x06 \x01(\t\"\xa7\x01\n\x16PActiveThreadLightDump\x12\x11\n\tstartTime\x18\x01 \x01(\x03\x12\x14\n\x0clocalTraceId\x18\x02 \x01(\x03\x12(\n\nthreadDump\x18\x03 \x01(\x0b\x32\x14.v1.PThreadLightDump\x12\x0f\n\x07sampled\x18\x04 \x01(\x08\x12\x15\n\rtransactionId\x18\x05 \x01(\t\x12\x12\n\nentryPoint\x18\x06 \x01(\t*\xca\x01\n\x0cPThreadState\x12\x14\n\x10THREAD_STATE_NEW\x10\x00\x12\x19\n\x15THREAD_STATE_RUNNABLE\x10\x01\x12\x18\n\x14THREAD_STATE_BLOCKED\x10\x02\x12\x18\n\x14THREAD_STATE_WAITING\x10\x03\x12\x1e\n\x1aTHREAD_STATE_TIMED_WAITING\x10\x04\x12\x1b\n\x17THREAD_STATE_TERMINATED\x10\x05\x12\x18\n\x14THREAD_STATE_UNKNOWN\x10\x06**\n\x0fPThreadDumpType\x12\n\n\x06TARGET\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x42\x88\x01\n!com.navercorp.pinpoint.grpc.traceB\x0fThreadDumpProtoP\x01ZPgitlab.jiagouyun.com/cloudcare-tools/datakit/plugins/inputs/pinpoint/compiled/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.ThreadDump_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.navercorp.pinpoint.grpc.traceB\017ThreadDumpProtoP\001ZPgitlab.jiagouyun.com/cloudcare-tools/datakit/plugins/inputs/pinpoint/compiled/v1'
  _PTHREADSTATE._serialized_start=876
  _PTHREADSTATE._serialized_end=1078
  _PTHREADDUMPTYPE._serialized_start=1080
  _PTHREADDUMPTYPE._serialized_end=1122
  _PMONITORINFO._serialized_start=27
  _PMONITORINFO._serialized_end=81
  _PTHREADDUMP._serialized_start=84
  _PTHREADDUMP._serialized_end=446
  _PTHREADLIGHTDUMP._serialized_start=448
  _PTHREADLIGHTDUMP._serialized_end=543
  _PACTIVETHREADDUMP._serialized_start=546
  _PACTIVETHREADDUMP._serialized_end=703
  _PACTIVETHREADLIGHTDUMP._serialized_start=706
  _PACTIVETHREADLIGHTDUMP._serialized_end=873
# @@protoc_insertion_point(module_scope)