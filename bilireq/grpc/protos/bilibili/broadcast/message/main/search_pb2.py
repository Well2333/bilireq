# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/broadcast/message/main/search.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from bilireq.grpc.protos.bilibili.app.dynamic.v2 import dynamic_pb2 as bilibili_dot_app_dot_dynamic_dot_v2_dot_dynamic__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,bilibili/broadcast/message/main/search.proto\x12\x1f\x62ilibili.broadcast.message.main\x1a\x1bgoogle/protobuf/empty.proto\x1a%bilibili/app/dynamic/v2/dynamic.proto\"@\n\x06\x42ubble\x12\x36\n\nparagraphs\x18\x01 \x03(\x0b\x32\".bilibili.app.dynamic.v2.Paragraph\"\x8c\x01\n\nChatResult\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x37\n\x06\x62ubble\x18\x03 \x03(\x0b\x32\'.bilibili.broadcast.message.main.Bubble\x12\x14\n\x0crewrite_word\x18\x04 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t2a\n\x06Search\x12W\n\x0e\x43hatResultPush\x12\x16.google.protobuf.Empty\x1a+.bilibili.broadcast.message.main.ChatResult0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.broadcast.message.main.search_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BUBBLE']._serialized_start=149
  _globals['_BUBBLE']._serialized_end=213
  _globals['_CHATRESULT']._serialized_start=216
  _globals['_CHATRESULT']._serialized_end=356
  _globals['_SEARCH']._serialized_start=358
  _globals['_SEARCH']._serialized_end=455
# @@protoc_insertion_point(module_scope)