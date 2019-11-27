# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/services/feed_item_target_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.resources import feed_item_target_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_feed__item__target__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/services/feed_item_target_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v1.servicesB\032FeedItemTargetServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v1/proto/services/feed_item_target_service.proto\x12 google.ads.googleads.v1.services\x1a>google/ads/googleads_v1/proto/resources/feed_item_target.proto\x1a\x1cgoogle/api/annotations.proto\"1\n\x18GetFeedItemTargetRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x82\x01\n\x1cMutateFeedItemTargetsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12M\n\noperations\x18\x02 \x03(\x0b\x32\x39.google.ads.googleads.v1.services.FeedItemTargetOperation\"}\n\x17\x46\x65\x65\x64ItemTargetOperation\x12\x43\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x31.google.ads.googleads.v1.resources.FeedItemTargetH\x00\x12\x10\n\x06remove\x18\x02 \x01(\tH\x00\x42\x0b\n\toperation\"n\n\x1dMutateFeedItemTargetsResponse\x12M\n\x07results\x18\x02 \x03(\x0b\x32<.google.ads.googleads.v1.services.MutateFeedItemTargetResult\"3\n\x1aMutateFeedItemTargetResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xb3\x03\n\x15\x46\x65\x65\x64ItemTargetService\x12\xbd\x01\n\x11GetFeedItemTarget\x12:.google.ads.googleads.v1.services.GetFeedItemTargetRequest\x1a\x31.google.ads.googleads.v1.resources.FeedItemTarget\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/v1/{resource_name=customers/*/feedItemTargets/*}\x12\xd9\x01\n\x15MutateFeedItemTargets\x12>.google.ads.googleads.v1.services.MutateFeedItemTargetsRequest\x1a?.google.ads.googleads.v1.services.MutateFeedItemTargetsResponse\"?\x82\xd3\xe4\x93\x02\x39\"4/v1/customers/{customer_id=*}/feedItemTargets:mutate:\x01*B\x81\x02\n$com.google.ads.googleads.v1.servicesB\x1a\x46\x65\x65\x64ItemTargetServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_feed__item__target__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETFEEDITEMTARGETREQUEST = _descriptor.Descriptor(
  name='GetFeedItemTargetRequest',
  full_name='google.ads.googleads.v1.services.GetFeedItemTargetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetFeedItemTargetRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=201,
  serialized_end=250,
)


_MUTATEFEEDITEMTARGETSREQUEST = _descriptor.Descriptor(
  name='MutateFeedItemTargetsRequest',
  full_name='google.ads.googleads.v1.services.MutateFeedItemTargetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v1.services.MutateFeedItemTargetsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v1.services.MutateFeedItemTargetsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=253,
  serialized_end=383,
)


_FEEDITEMTARGETOPERATION = _descriptor.Descriptor(
  name='FeedItemTargetOperation',
  full_name='google.ads.googleads.v1.services.FeedItemTargetOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v1.services.FeedItemTargetOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v1.services.FeedItemTargetOperation.remove', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v1.services.FeedItemTargetOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=385,
  serialized_end=510,
)


_MUTATEFEEDITEMTARGETSRESPONSE = _descriptor.Descriptor(
  name='MutateFeedItemTargetsResponse',
  full_name='google.ads.googleads.v1.services.MutateFeedItemTargetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v1.services.MutateFeedItemTargetsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=512,
  serialized_end=622,
)


_MUTATEFEEDITEMTARGETRESULT = _descriptor.Descriptor(
  name='MutateFeedItemTargetResult',
  full_name='google.ads.googleads.v1.services.MutateFeedItemTargetResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.MutateFeedItemTargetResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=624,
  serialized_end=675,
)

_MUTATEFEEDITEMTARGETSREQUEST.fields_by_name['operations'].message_type = _FEEDITEMTARGETOPERATION
_FEEDITEMTARGETOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_feed__item__target__pb2._FEEDITEMTARGET
_FEEDITEMTARGETOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDITEMTARGETOPERATION.fields_by_name['create'])
_FEEDITEMTARGETOPERATION.fields_by_name['create'].containing_oneof = _FEEDITEMTARGETOPERATION.oneofs_by_name['operation']
_FEEDITEMTARGETOPERATION.oneofs_by_name['operation'].fields.append(
  _FEEDITEMTARGETOPERATION.fields_by_name['remove'])
_FEEDITEMTARGETOPERATION.fields_by_name['remove'].containing_oneof = _FEEDITEMTARGETOPERATION.oneofs_by_name['operation']
_MUTATEFEEDITEMTARGETSRESPONSE.fields_by_name['results'].message_type = _MUTATEFEEDITEMTARGETRESULT
DESCRIPTOR.message_types_by_name['GetFeedItemTargetRequest'] = _GETFEEDITEMTARGETREQUEST
DESCRIPTOR.message_types_by_name['MutateFeedItemTargetsRequest'] = _MUTATEFEEDITEMTARGETSREQUEST
DESCRIPTOR.message_types_by_name['FeedItemTargetOperation'] = _FEEDITEMTARGETOPERATION
DESCRIPTOR.message_types_by_name['MutateFeedItemTargetsResponse'] = _MUTATEFEEDITEMTARGETSRESPONSE
DESCRIPTOR.message_types_by_name['MutateFeedItemTargetResult'] = _MUTATEFEEDITEMTARGETRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetFeedItemTargetRequest = _reflection.GeneratedProtocolMessageType('GetFeedItemTargetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETFEEDITEMTARGETREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.feed_item_target_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedItemTargetService.GetFeedItemTarget][google.ads.googleads.v1.services.FeedItemTargetService.GetFeedItemTarget].
  
  
  Attributes:
      resource_name:
          The resource name of the feed item targets to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetFeedItemTargetRequest)
  ))
_sym_db.RegisterMessage(GetFeedItemTargetRequest)

MutateFeedItemTargetsRequest = _reflection.GeneratedProtocolMessageType('MutateFeedItemTargetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDITEMTARGETSREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.feed_item_target_service_pb2'
  ,
  __doc__ = """Request message for
  [FeedItemTargetService.MutateFeedItemTargets][google.ads.googleads.v1.services.FeedItemTargetService.MutateFeedItemTargets].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose feed item targets are being
          modified.
      operations:
          The list of operations to perform on individual feed item
          targets.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateFeedItemTargetsRequest)
  ))
_sym_db.RegisterMessage(MutateFeedItemTargetsRequest)

FeedItemTargetOperation = _reflection.GeneratedProtocolMessageType('FeedItemTargetOperation', (_message.Message,), dict(
  DESCRIPTOR = _FEEDITEMTARGETOPERATION,
  __module__ = 'google.ads.googleads_v1.proto.services.feed_item_target_service_pb2'
  ,
  __doc__ = """A single operation (create, remove) on an feed item target.
  
  
  Attributes:
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          feed item target.
      remove:
          Remove operation: A resource name for the removed feed item
          target is expected, in this format:  ``customers/{customer_id}
          /feedItemTargets/{feed_id}~{feed_item_id}~{feed_item_target_ty
          pe}~{feed_item_target_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.FeedItemTargetOperation)
  ))
_sym_db.RegisterMessage(FeedItemTargetOperation)

MutateFeedItemTargetsResponse = _reflection.GeneratedProtocolMessageType('MutateFeedItemTargetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDITEMTARGETSRESPONSE,
  __module__ = 'google.ads.googleads_v1.proto.services.feed_item_target_service_pb2'
  ,
  __doc__ = """Response message for an feed item target mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateFeedItemTargetsResponse)
  ))
_sym_db.RegisterMessage(MutateFeedItemTargetsResponse)

MutateFeedItemTargetResult = _reflection.GeneratedProtocolMessageType('MutateFeedItemTargetResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEFEEDITEMTARGETRESULT,
  __module__ = 'google.ads.googleads_v1.proto.services.feed_item_target_service_pb2'
  ,
  __doc__ = """The result for the feed item target mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateFeedItemTargetResult)
  ))
_sym_db.RegisterMessage(MutateFeedItemTargetResult)


DESCRIPTOR._options = None

_FEEDITEMTARGETSERVICE = _descriptor.ServiceDescriptor(
  name='FeedItemTargetService',
  full_name='google.ads.googleads.v1.services.FeedItemTargetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=678,
  serialized_end=1113,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeedItemTarget',
    full_name='google.ads.googleads.v1.services.FeedItemTargetService.GetFeedItemTarget',
    index=0,
    containing_service=None,
    input_type=_GETFEEDITEMTARGETREQUEST,
    output_type=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_feed__item__target__pb2._FEEDITEMTARGET,
    serialized_options=_b('\202\323\344\223\0023\0221/v1/{resource_name=customers/*/feedItemTargets/*}'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateFeedItemTargets',
    full_name='google.ads.googleads.v1.services.FeedItemTargetService.MutateFeedItemTargets',
    index=1,
    containing_service=None,
    input_type=_MUTATEFEEDITEMTARGETSREQUEST,
    output_type=_MUTATEFEEDITEMTARGETSRESPONSE,
    serialized_options=_b('\202\323\344\223\0029\"4/v1/customers/{customer_id=*}/feedItemTargets:mutate:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_FEEDITEMTARGETSERVICE)

DESCRIPTOR.services_by_name['FeedItemTargetService'] = _FEEDITEMTARGETSERVICE

# @@protoc_insertion_point(module_scope)
