# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/metadata/restriction/restriction.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/bilibili/metadata/restriction/restriction.proto\x12\x1d\x62ilibili.metadata.restriction\"\x98\x01\n\x0bRestriction\x12\x16\n\x0eteenagers_mode\x18\x01 \x01(\x08\x12\x14\n\x0clessons_mode\x18\x02 \x01(\x08\x12\x35\n\x04mode\x18\x03 \x01(\x0e\x32\'.bilibili.metadata.restriction.ModeType\x12\x0e\n\x06review\x18\x04 \x01(\x08\x12\x14\n\x0c\x64isable_rcmd\x18\x05 \x01(\x08*2\n\x08ModeType\x12\n\n\x06NORMAL\x10\x00\x12\r\n\tTEENAGERS\x10\x01\x12\x0b\n\x07LESSONS\x10\x02\x62\x06proto3')

_MODETYPE = DESCRIPTOR.enum_types_by_name['ModeType']
ModeType = enum_type_wrapper.EnumTypeWrapper(_MODETYPE)
NORMAL = 0
TEENAGERS = 1
LESSONS = 2


_RESTRICTION = DESCRIPTOR.message_types_by_name['Restriction']
Restriction = _reflection.GeneratedProtocolMessageType('Restriction', (_message.Message,), {
  'DESCRIPTOR' : _RESTRICTION,
  '__module__' : 'bilibili.metadata.restriction.restriction_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.metadata.restriction.Restriction)
  })
_sym_db.RegisterMessage(Restriction)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MODETYPE._serialized_start=237
  _MODETYPE._serialized_end=287
  _RESTRICTION._serialized_start=83
  _RESTRICTION._serialized_end=235
# @@protoc_insertion_point(module_scope)