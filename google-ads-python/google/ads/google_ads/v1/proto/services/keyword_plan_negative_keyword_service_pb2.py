# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/services/keyword_plan_negative_keyword_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.resources import keyword_plan_negative_keyword_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/services/keyword_plan_negative_keyword_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v1.servicesB&KeywordPlanNegativeKeywordServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services'),
  serialized_pb=_b('\nRgoogle/ads/googleads_v1/proto/services/keyword_plan_negative_keyword_service.proto\x12 google.ads.googleads.v1.services\x1aKgoogle/ads/googleads_v1/proto/resources/keyword_plan_negative_keyword.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"=\n$GetKeywordPlanNegativeKeywordRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xca\x01\n(MutateKeywordPlanNegativeKeywordsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12Y\n\noperations\x18\x02 \x03(\x0b\x32\x45.google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x97\x02\n#KeywordPlanNegativeKeywordOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12O\n\x06\x63reate\x18\x01 \x01(\x0b\x32=.google.ads.googleads.v1.resources.KeywordPlanNegativeKeywordH\x00\x12O\n\x06update\x18\x02 \x01(\x0b\x32=.google.ads.googleads.v1.resources.KeywordPlanNegativeKeywordH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\xb9\x01\n)MutateKeywordPlanNegativeKeywordsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12Y\n\x07results\x18\x02 \x03(\x0b\x32H.google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordResult\"?\n&MutateKeywordPlanNegativeKeywordResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x9f\x04\n!KeywordPlanNegativeKeywordService\x12\xed\x01\n\x1dGetKeywordPlanNegativeKeyword\x12\x46.google.ads.googleads.v1.services.GetKeywordPlanNegativeKeywordRequest\x1a=.google.ads.googleads.v1.resources.KeywordPlanNegativeKeyword\"E\x82\xd3\xe4\x93\x02?\x12=/v1/{resource_name=customers/*/keywordPlanNegativeKeywords/*}\x12\x89\x02\n!MutateKeywordPlanNegativeKeywords\x12J.google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsRequest\x1aK.google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsResponse\"K\x82\xd3\xe4\x93\x02\x45\"@/v1/customers/{customer_id=*}/keywordPlanNegativeKeywords:mutate:\x01*B\x8d\x02\n$com.google.ads.googleads.v1.servicesB&KeywordPlanNegativeKeywordServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETKEYWORDPLANNEGATIVEKEYWORDREQUEST = _descriptor.Descriptor(
  name='GetKeywordPlanNegativeKeywordRequest',
  full_name='google.ads.googleads.v1.services.GetKeywordPlanNegativeKeywordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetKeywordPlanNegativeKeywordRequest.resource_name', index=0,
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
  serialized_start=318,
  serialized_end=379,
)


_MUTATEKEYWORDPLANNEGATIVEKEYWORDSREQUEST = _descriptor.Descriptor(
  name='MutateKeywordPlanNegativeKeywordsRequest',
  full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=382,
  serialized_end=584,
)


_KEYWORDPLANNEGATIVEKEYWORDOPERATION = _descriptor.Descriptor(
  name='KeywordPlanNegativeKeywordOperation',
  full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
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
      name='operation', full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=587,
  serialized_end=866,
)


_MUTATEKEYWORDPLANNEGATIVEKEYWORDSRESPONSE = _descriptor.Descriptor(
  name='MutateKeywordPlanNegativeKeywordsResponse',
  full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsResponse.results', index=1,
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
  serialized_start=869,
  serialized_end=1054,
)


_MUTATEKEYWORDPLANNEGATIVEKEYWORDRESULT = _descriptor.Descriptor(
  name='MutateKeywordPlanNegativeKeywordResult',
  full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordResult.resource_name', index=0,
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
  serialized_start=1056,
  serialized_end=1119,
)

_MUTATEKEYWORDPLANNEGATIVEKEYWORDSREQUEST.fields_by_name['operations'].message_type = _KEYWORDPLANNEGATIVEKEYWORDOPERATION
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2._KEYWORDPLANNEGATIVEKEYWORD
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2._KEYWORDPLANNEGATIVEKEYWORD
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['create'])
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['create'].containing_oneof = _KEYWORDPLANNEGATIVEKEYWORDOPERATION.oneofs_by_name['operation']
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['update'])
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['update'].containing_oneof = _KEYWORDPLANNEGATIVEKEYWORDOPERATION.oneofs_by_name['operation']
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['remove'])
_KEYWORDPLANNEGATIVEKEYWORDOPERATION.fields_by_name['remove'].containing_oneof = _KEYWORDPLANNEGATIVEKEYWORDOPERATION.oneofs_by_name['operation']
_MUTATEKEYWORDPLANNEGATIVEKEYWORDSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEKEYWORDPLANNEGATIVEKEYWORDSRESPONSE.fields_by_name['results'].message_type = _MUTATEKEYWORDPLANNEGATIVEKEYWORDRESULT
DESCRIPTOR.message_types_by_name['GetKeywordPlanNegativeKeywordRequest'] = _GETKEYWORDPLANNEGATIVEKEYWORDREQUEST
DESCRIPTOR.message_types_by_name['MutateKeywordPlanNegativeKeywordsRequest'] = _MUTATEKEYWORDPLANNEGATIVEKEYWORDSREQUEST
DESCRIPTOR.message_types_by_name['KeywordPlanNegativeKeywordOperation'] = _KEYWORDPLANNEGATIVEKEYWORDOPERATION
DESCRIPTOR.message_types_by_name['MutateKeywordPlanNegativeKeywordsResponse'] = _MUTATEKEYWORDPLANNEGATIVEKEYWORDSRESPONSE
DESCRIPTOR.message_types_by_name['MutateKeywordPlanNegativeKeywordResult'] = _MUTATEKEYWORDPLANNEGATIVEKEYWORDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetKeywordPlanNegativeKeywordRequest = _reflection.GeneratedProtocolMessageType('GetKeywordPlanNegativeKeywordRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETKEYWORDPLANNEGATIVEKEYWORDREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.keyword_plan_negative_keyword_service_pb2'
  ,
  __doc__ = """Request message for
  [KeywordPlanNegativeKeywordService.GetKeywordPlanNegativeKeyword][google.ads.googleads.v1.services.KeywordPlanNegativeKeywordService.GetKeywordPlanNegativeKeyword].
  
  
  Attributes:
      resource_name:
          The resource name of the plan to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetKeywordPlanNegativeKeywordRequest)
  ))
_sym_db.RegisterMessage(GetKeywordPlanNegativeKeywordRequest)

MutateKeywordPlanNegativeKeywordsRequest = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanNegativeKeywordsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANNEGATIVEKEYWORDSREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.keyword_plan_negative_keyword_service_pb2'
  ,
  __doc__ = """Request message for
  [KeywordPlanNegativeKeywordService.MutateKeywordPlanNegativeKeywords][google.ads.googleads.v1.services.KeywordPlanNegativeKeywordService.MutateKeywordPlanNegativeKeywords].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose negative keywords are being
          modified.
      operations:
          The list of operations to perform on individual Keyword Plan
          negative keywords.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsRequest)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanNegativeKeywordsRequest)

KeywordPlanNegativeKeywordOperation = _reflection.GeneratedProtocolMessageType('KeywordPlanNegativeKeywordOperation', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANNEGATIVEKEYWORDOPERATION,
  __module__ = 'google.ads.googleads_v1.proto.services.keyword_plan_negative_keyword_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on a Keyword Plan negative
  keyword.
  
  
  Attributes:
      update_mask:
          The FieldMask that determines which resource fields are
          modified in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          Keyword Plan negative keyword.
      update:
          Update operation: The Keyword Plan negative keyword expected
          to have a valid resource name.
      remove:
          Remove operation: A resource name for the removed Keyword Plan
          negative keywords expected in this format:  ``customers/{custo
          mer_id}/keywordPlanNegativeKeywords/{kp_negative_keyword_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.KeywordPlanNegativeKeywordOperation)
  ))
_sym_db.RegisterMessage(KeywordPlanNegativeKeywordOperation)

MutateKeywordPlanNegativeKeywordsResponse = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanNegativeKeywordsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANNEGATIVEKEYWORDSRESPONSE,
  __module__ = 'google.ads.googleads_v1.proto.services.keyword_plan_negative_keyword_service_pb2'
  ,
  __doc__ = """Response message for a Keyword Plan negative keyword mutate.
  
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordsResponse)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanNegativeKeywordsResponse)

MutateKeywordPlanNegativeKeywordResult = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanNegativeKeywordResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANNEGATIVEKEYWORDRESULT,
  __module__ = 'google.ads.googleads_v1.proto.services.keyword_plan_negative_keyword_service_pb2'
  ,
  __doc__ = """The result for the Keyword Plan negative keyword mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.MutateKeywordPlanNegativeKeywordResult)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanNegativeKeywordResult)


DESCRIPTOR._options = None

_KEYWORDPLANNEGATIVEKEYWORDSERVICE = _descriptor.ServiceDescriptor(
  name='KeywordPlanNegativeKeywordService',
  full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1122,
  serialized_end=1665,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetKeywordPlanNegativeKeyword',
    full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordService.GetKeywordPlanNegativeKeyword',
    index=0,
    containing_service=None,
    input_type=_GETKEYWORDPLANNEGATIVEKEYWORDREQUEST,
    output_type=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_keyword__plan__negative__keyword__pb2._KEYWORDPLANNEGATIVEKEYWORD,
    serialized_options=_b('\202\323\344\223\002?\022=/v1/{resource_name=customers/*/keywordPlanNegativeKeywords/*}'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateKeywordPlanNegativeKeywords',
    full_name='google.ads.googleads.v1.services.KeywordPlanNegativeKeywordService.MutateKeywordPlanNegativeKeywords',
    index=1,
    containing_service=None,
    input_type=_MUTATEKEYWORDPLANNEGATIVEKEYWORDSREQUEST,
    output_type=_MUTATEKEYWORDPLANNEGATIVEKEYWORDSRESPONSE,
    serialized_options=_b('\202\323\344\223\002E\"@/v1/customers/{customer_id=*}/keywordPlanNegativeKeywords:mutate:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYWORDPLANNEGATIVEKEYWORDSERVICE)

DESCRIPTOR.services_by_name['KeywordPlanNegativeKeywordService'] = _KEYWORDPLANNEGATIVEKEYWORDSERVICE

# @@protoc_insertion_point(module_scope)
