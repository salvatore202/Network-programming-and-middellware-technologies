# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: productManager.proto
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
    'productManager.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14productManager.proto\"\x19\n\x0bsellRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x1f\n\x0csellResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x07\n\x05\x45mpty\"\x19\n\x0b\x62uyResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x32R\n\x0eProductManager\x12#\n\x04sell\x12\x0c.sellRequest\x1a\r.sellResponse\x12\x1b\n\x03\x62uy\x12\x06.Empty\x1a\x0c.buyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'productManager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SELLREQUEST']._serialized_start=24
  _globals['_SELLREQUEST']._serialized_end=49
  _globals['_SELLRESPONSE']._serialized_start=51
  _globals['_SELLRESPONSE']._serialized_end=82
  _globals['_EMPTY']._serialized_start=84
  _globals['_EMPTY']._serialized_end=91
  _globals['_BUYRESPONSE']._serialized_start=93
  _globals['_BUYRESPONSE']._serialized_end=118
  _globals['_PRODUCTMANAGER']._serialized_start=120
  _globals['_PRODUCTMANAGER']._serialized_end=202
# @@protoc_insertion_point(module_scope)
