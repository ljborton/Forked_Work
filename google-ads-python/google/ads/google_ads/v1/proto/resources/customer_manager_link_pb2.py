# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/customer_manager_link.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.enums import manager_link_status_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_manager__link__status__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/customer_manager_link.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\030CustomerManagerLinkProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\nCgoogle/ads/googleads_v1/proto/resources/customer_manager_link.proto\x12!google.ads.googleads.v1.resources\x1a=google/ads/googleads_v1/proto/enums/manager_link_status.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xf2\x01\n\x13\x43ustomerManagerLink\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x36\n\x10manager_customer\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0fmanager_link_id\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12V\n\x06status\x18\x05 \x01(\x0e\x32\x46.google.ads.googleads.v1.enums.ManagerLinkStatusEnum.ManagerLinkStatusB\x85\x02\n%com.google.ads.googleads.v1.resourcesB\x18\x43ustomerManagerLinkProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_manager__link__status__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CUSTOMERMANAGERLINK = _descriptor.Descriptor(
  name='CustomerManagerLink',
  full_name='google.ads.googleads.v1.resources.CustomerManagerLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.CustomerManagerLink.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager_customer', full_name='google.ads.googleads.v1.resources.CustomerManagerLink.manager_customer', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manager_link_id', full_name='google.ads.googleads.v1.resources.CustomerManagerLink.manager_link_id', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v1.resources.CustomerManagerLink.status', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=474,
)

_CUSTOMERMANAGERLINK.fields_by_name['manager_customer'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CUSTOMERMANAGERLINK.fields_by_name['manager_link_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CUSTOMERMANAGERLINK.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_manager__link__status__pb2._MANAGERLINKSTATUSENUM_MANAGERLINKSTATUS
DESCRIPTOR.message_types_by_name['CustomerManagerLink'] = _CUSTOMERMANAGERLINK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerManagerLink = _reflection.GeneratedProtocolMessageType('CustomerManagerLink', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERMANAGERLINK,
  __module__ = 'google.ads.googleads_v1.proto.resources.customer_manager_link_pb2'
  ,
  __doc__ = """Represents customer-manager link relationship.
  
  
  Attributes:
      resource_name:
          Name of the resource. CustomerManagerLink resource names have
          the form:  ``customers/{customer_id}/customerManagerLinks/{man
          ager_customer_id}~{manager_link_id}``
      manager_customer:
          The manager customer linked to the customer.
      manager_link_id:
          ID of the customer-manager link. This field is read only.
      status:
          Status of the link between the customer and the manager.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.CustomerManagerLink)
  ))
_sym_db.RegisterMessage(CustomerManagerLink)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
