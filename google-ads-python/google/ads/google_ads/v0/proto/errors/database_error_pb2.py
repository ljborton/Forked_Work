# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/database_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/database_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v0.errorsB\022DatabaseErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors\352\002\"Google::Ads::GoogleAds::V0::Errors'),
  serialized_pb=_b('\n9google/ads/googleads_v0/proto/errors/database_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"_\n\x11\x44\x61tabaseErrorEnum\"J\n\rDatabaseError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1b\n\x17\x43ONCURRENT_MODIFICATION\x10\x02\x42\xed\x01\n\"com.google.ads.googleads.v0.errorsB\x12\x44\x61tabaseErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errors\xea\x02\"Google::Ads::GoogleAds::V0::Errorsb\x06proto3')
)



_DATABASEERRORENUM_DATABASEERROR = _descriptor.EnumDescriptor(
  name='DatabaseError',
  full_name='google.ads.googleads.v0.errors.DatabaseErrorEnum.DatabaseError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONCURRENT_MODIFICATION', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=114,
  serialized_end=188,
)
_sym_db.RegisterEnumDescriptor(_DATABASEERRORENUM_DATABASEERROR)


_DATABASEERRORENUM = _descriptor.Descriptor(
  name='DatabaseErrorEnum',
  full_name='google.ads.googleads.v0.errors.DatabaseErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATABASEERRORENUM_DATABASEERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=188,
)

_DATABASEERRORENUM_DATABASEERROR.containing_type = _DATABASEERRORENUM
DESCRIPTOR.message_types_by_name['DatabaseErrorEnum'] = _DATABASEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DatabaseErrorEnum = _reflection.GeneratedProtocolMessageType('DatabaseErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _DATABASEERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.database_error_pb2'
  ,
  __doc__ = """Container for enum describing possible database errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.DatabaseErrorEnum)
  ))
_sym_db.RegisterMessage(DatabaseErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
