# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: statistics.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'statistics.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10statistics.proto\x12\nstatistics\".\n\x06Sensor\x12\x11\n\tsensor_id\x18\x01 \x01(\x03\x12\x11\n\tdata_type\x18\x02 \x01(\t\"3\n\x0bMeanRequest\x12\x11\n\tsensor_id\x18\x01 \x01(\x03\x12\x11\n\tdata_type\x18\x02 \x01(\t\"\x1e\n\rStringMessage\x12\r\n\x05value\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\x89\x01\n\x11StatisticsManager\x12\x35\n\ngetSensors\x12\x11.statistics.Empty\x1a\x12.statistics.Sensor0\x01\x12=\n\x07getMean\x12\x17.statistics.MeanRequest\x1a\x19.statistics.StringMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'statistics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SENSOR']._serialized_start=32
  _globals['_SENSOR']._serialized_end=78
  _globals['_MEANREQUEST']._serialized_start=80
  _globals['_MEANREQUEST']._serialized_end=131
  _globals['_STRINGMESSAGE']._serialized_start=133
  _globals['_STRINGMESSAGE']._serialized_end=163
  _globals['_EMPTY']._serialized_start=165
  _globals['_EMPTY']._serialized_end=172
  _globals['_STATISTICSMANAGER']._serialized_start=175
  _globals['_STATISTICSMANAGER']._serialized_end=312
# @@protoc_insertion_point(module_scope)
