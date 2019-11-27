# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/shared_criterion_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import shared_criterion_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/shared_criterion_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v0.servicesB\033SharedCriterionServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services\352\002$Google::Ads::GoogleAds::V0::Services'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v0/proto/services/shared_criterion_service.proto\x12 google.ads.googleads.v0.services\x1a>google/ads/googleads_v0/proto/resources/shared_criterion.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\"2\n\x19GetSharedCriterionRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xb2\x01\n\x1bMutateSharedCriteriaRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12N\n\noperations\x18\x02 \x03(\x0b\x32:.google.ads.googleads.v0.services.SharedCriterionOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x7f\n\x18SharedCriterionOperation\x12\x44\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x32.google.ads.googleads.v0.resources.SharedCriterionH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\xa1\x01\n\x1cMutateSharedCriteriaResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12N\n\x07results\x18\x02 \x03(\x0b\x32=.google.ads.googleads.v0.services.MutateSharedCriterionResult\"4\n\x1bMutateSharedCriterionResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xb2\x03\n\x16SharedCriterionService\x12\xbf\x01\n\x12GetSharedCriterion\x12;.google.ads.googleads.v0.services.GetSharedCriterionRequest\x1a\x32.google.ads.googleads.v0.resources.SharedCriterion\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/v0/{resource_name=customers/*/sharedCriteria/*}\x12\xd5\x01\n\x14MutateSharedCriteria\x12=.google.ads.googleads.v0.services.MutateSharedCriteriaRequest\x1a>.google.ads.googleads.v0.services.MutateSharedCriteriaResponse\">\x82\xd3\xe4\x93\x02\x38\"3/v0/customers/{customer_id=*}/sharedCriteria:mutate:\x01*B\x82\x02\n$com.google.ads.googleads.v0.servicesB\x1bSharedCriterionServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Services\xea\x02$Google::Ads::GoogleAds::V0::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETSHAREDCRITERIONREQUEST = _descriptor.Descriptor(
  name='GetSharedCriterionRequest',
  full_name='google.ads.googleads.v0.services.GetSharedCriterionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetSharedCriterionRequest.resource_name', index=0,
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
  serialized_start=258,
  serialized_end=308,
)


_MUTATESHAREDCRITERIAREQUEST = _descriptor.Descriptor(
  name='MutateSharedCriteriaRequest',
  full_name='google.ads.googleads.v0.services.MutateSharedCriteriaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateSharedCriteriaRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateSharedCriteriaRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v0.services.MutateSharedCriteriaRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v0.services.MutateSharedCriteriaRequest.validate_only', index=3,
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
  serialized_start=311,
  serialized_end=489,
)


_SHAREDCRITERIONOPERATION = _descriptor.Descriptor(
  name='SharedCriterionOperation',
  full_name='google.ads.googleads.v0.services.SharedCriterionOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.SharedCriterionOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.SharedCriterionOperation.remove', index=1,
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
      name='operation', full_name='google.ads.googleads.v0.services.SharedCriterionOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=491,
  serialized_end=618,
)


_MUTATESHAREDCRITERIARESPONSE = _descriptor.Descriptor(
  name='MutateSharedCriteriaResponse',
  full_name='google.ads.googleads.v0.services.MutateSharedCriteriaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v0.services.MutateSharedCriteriaResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateSharedCriteriaResponse.results', index=1,
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
  serialized_start=621,
  serialized_end=782,
)


_MUTATESHAREDCRITERIONRESULT = _descriptor.Descriptor(
  name='MutateSharedCriterionResult',
  full_name='google.ads.googleads.v0.services.MutateSharedCriterionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateSharedCriterionResult.resource_name', index=0,
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
  serialized_start=784,
  serialized_end=836,
)

_MUTATESHAREDCRITERIAREQUEST.fields_by_name['operations'].message_type = _SHAREDCRITERIONOPERATION
_SHAREDCRITERIONOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2._SHAREDCRITERION
_SHAREDCRITERIONOPERATION.oneofs_by_name['operation'].fields.append(
  _SHAREDCRITERIONOPERATION.fields_by_name['create'])
_SHAREDCRITERIONOPERATION.fields_by_name['create'].containing_oneof = _SHAREDCRITERIONOPERATION.oneofs_by_name['operation']
_SHAREDCRITERIONOPERATION.oneofs_by_name['operation'].fields.append(
  _SHAREDCRITERIONOPERATION.fields_by_name['remove'])
_SHAREDCRITERIONOPERATION.fields_by_name['remove'].containing_oneof = _SHAREDCRITERIONOPERATION.oneofs_by_name['operation']
_MUTATESHAREDCRITERIARESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATESHAREDCRITERIARESPONSE.fields_by_name['results'].message_type = _MUTATESHAREDCRITERIONRESULT
DESCRIPTOR.message_types_by_name['GetSharedCriterionRequest'] = _GETSHAREDCRITERIONREQUEST
DESCRIPTOR.message_types_by_name['MutateSharedCriteriaRequest'] = _MUTATESHAREDCRITERIAREQUEST
DESCRIPTOR.message_types_by_name['SharedCriterionOperation'] = _SHAREDCRITERIONOPERATION
DESCRIPTOR.message_types_by_name['MutateSharedCriteriaResponse'] = _MUTATESHAREDCRITERIARESPONSE
DESCRIPTOR.message_types_by_name['MutateSharedCriterionResult'] = _MUTATESHAREDCRITERIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSharedCriterionRequest = _reflection.GeneratedProtocolMessageType('GetSharedCriterionRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSHAREDCRITERIONREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_criterion_service_pb2'
  ,
  __doc__ = """Request message for
  [SharedCriterionService.GetSharedCriterion][google.ads.googleads.v0.services.SharedCriterionService.GetSharedCriterion].
  
  
  Attributes:
      resource_name:
          The resource name of the shared criterion to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetSharedCriterionRequest)
  ))
_sym_db.RegisterMessage(GetSharedCriterionRequest)

MutateSharedCriteriaRequest = _reflection.GeneratedProtocolMessageType('MutateSharedCriteriaRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATESHAREDCRITERIAREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_criterion_service_pb2'
  ,
  __doc__ = """Request message for
  [SharedCriterionService.MutateSharedCriteria][google.ads.googleads.v0.services.SharedCriterionService.MutateSharedCriteria].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose shared criteria are being
          modified.
      operations:
          The list of operations to perform on individual shared
          criteria.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateSharedCriteriaRequest)
  ))
_sym_db.RegisterMessage(MutateSharedCriteriaRequest)

SharedCriterionOperation = _reflection.GeneratedProtocolMessageType('SharedCriterionOperation', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDCRITERIONOPERATION,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_criterion_service_pb2'
  ,
  __doc__ = """A single operation (create, remove) on an shared criterion.
  
  
  Attributes:
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          shared criterion.
      remove:
          Remove operation: A resource name for the removed shared
          criterion is expected, in this format:  ``customers/{customer_
          id}/sharedCriteria/{shared_set_id}_{criterion_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.SharedCriterionOperation)
  ))
_sym_db.RegisterMessage(SharedCriterionOperation)

MutateSharedCriteriaResponse = _reflection.GeneratedProtocolMessageType('MutateSharedCriteriaResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATESHAREDCRITERIARESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_criterion_service_pb2'
  ,
  __doc__ = """Response message for a shared criterion mutate.
  
  
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
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateSharedCriteriaResponse)
  ))
_sym_db.RegisterMessage(MutateSharedCriteriaResponse)

MutateSharedCriterionResult = _reflection.GeneratedProtocolMessageType('MutateSharedCriterionResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATESHAREDCRITERIONRESULT,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_criterion_service_pb2'
  ,
  __doc__ = """The result for the shared criterion mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateSharedCriterionResult)
  ))
_sym_db.RegisterMessage(MutateSharedCriterionResult)


DESCRIPTOR._options = None

_SHAREDCRITERIONSERVICE = _descriptor.ServiceDescriptor(
  name='SharedCriterionService',
  full_name='google.ads.googleads.v0.services.SharedCriterionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=839,
  serialized_end=1273,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSharedCriterion',
    full_name='google.ads.googleads.v0.services.SharedCriterionService.GetSharedCriterion',
    index=0,
    containing_service=None,
    input_type=_GETSHAREDCRITERIONREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2._SHAREDCRITERION,
    serialized_options=_b('\202\323\344\223\0022\0220/v0/{resource_name=customers/*/sharedCriteria/*}'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateSharedCriteria',
    full_name='google.ads.googleads.v0.services.SharedCriterionService.MutateSharedCriteria',
    index=1,
    containing_service=None,
    input_type=_MUTATESHAREDCRITERIAREQUEST,
    output_type=_MUTATESHAREDCRITERIARESPONSE,
    serialized_options=_b('\202\323\344\223\0028\"3/v0/customers/{customer_id=*}/sharedCriteria:mutate:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_SHAREDCRITERIONSERVICE)

DESCRIPTOR.services_by_name['SharedCriterionService'] = _SHAREDCRITERIONSERVICE

# @@protoc_insertion_point(module_scope)
