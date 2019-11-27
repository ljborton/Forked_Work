# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/campaign_criterion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.common import criteria_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2
from google.ads.google_ads.v0.proto.enums import criterion_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_criterion__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/resources/campaign_criterion.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v0.resourcesB\026CampaignCriterionProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources\352\002%Google::Ads::GoogleAds::V0::Resources'),
  serialized_pb=_b('\n@google/ads/googleads_v0/proto/resources/campaign_criterion.proto\x12!google.ads.googleads.v0.resources\x1a\x33google/ads/googleads_v0/proto/common/criteria.proto\x1a\x38google/ads/googleads_v0/proto/enums/criterion_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa4\x0f\n\x11\x43\x61mpaignCriterion\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12.\n\x08\x63\x61mpaign\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0c\x63riterion_id\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0c\x62id_modifier\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12,\n\x08negative\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12L\n\x04type\x18\x06 \x01(\x0e\x32>.google.ads.googleads.v0.enums.CriterionTypeEnum.CriterionType\x12>\n\x07keyword\x18\x08 \x01(\x0b\x32+.google.ads.googleads.v0.common.KeywordInfoH\x00\x12\x42\n\tplacement\x18\t \x01(\x0b\x32-.google.ads.googleads.v0.common.PlacementInfoH\x00\x12T\n\x13mobile_app_category\x18\n \x01(\x0b\x32\x35.google.ads.googleads.v0.common.MobileAppCategoryInfoH\x00\x12@\n\x08location\x18\x0c \x01(\x0b\x32,.google.ads.googleads.v0.common.LocationInfoH\x00\x12<\n\x06\x64\x65vice\x18\r \x01(\x0b\x32*.google.ads.googleads.v0.common.DeviceInfoH\x00\x12\x45\n\x0b\x61\x64_schedule\x18\x0f \x01(\x0b\x32..google.ads.googleads.v0.common.AdScheduleInfoH\x00\x12\x41\n\tage_range\x18\x10 \x01(\x0b\x32,.google.ads.googleads.v0.common.AgeRangeInfoH\x00\x12<\n\x06gender\x18\x11 \x01(\x0b\x32*.google.ads.googleads.v0.common.GenderInfoH\x00\x12G\n\x0cincome_range\x18\x12 \x01(\x0b\x32/.google.ads.googleads.v0.common.IncomeRangeInfoH\x00\x12M\n\x0fparental_status\x18\x13 \x01(\x0b\x32\x32.google.ads.googleads.v0.common.ParentalStatusInfoH\x00\x12\x41\n\tuser_list\x18\x16 \x01(\x0b\x32,.google.ads.googleads.v0.common.UserListInfoH\x00\x12I\n\ryoutube_video\x18\x14 \x01(\x0b\x32\x30.google.ads.googleads.v0.common.YouTubeVideoInfoH\x00\x12M\n\x0fyoutube_channel\x18\x15 \x01(\x0b\x32\x32.google.ads.googleads.v0.common.YouTubeChannelInfoH\x00\x12\x42\n\tproximity\x18\x17 \x01(\x0b\x32-.google.ads.googleads.v0.common.ProximityInfoH\x00\x12:\n\x05topic\x18\x18 \x01(\x0b\x32).google.ads.googleads.v0.common.TopicInfoH\x00\x12I\n\rlisting_scope\x18\x19 \x01(\x0b\x32\x30.google.ads.googleads.v0.common.ListingScopeInfoH\x00\x12@\n\x08language\x18\x1a \x01(\x0b\x32,.google.ads.googleads.v0.common.LanguageInfoH\x00\x12?\n\x08ip_block\x18\x1b \x01(\x0b\x32+.google.ads.googleads.v0.common.IpBlockInfoH\x00\x12I\n\rcontent_label\x18\x1c \x01(\x0b\x32\x30.google.ads.googleads.v0.common.ContentLabelInfoH\x00\x12>\n\x07\x63\x61rrier\x18\x1d \x01(\x0b\x32+.google.ads.googleads.v0.common.CarrierInfoH\x00\x12I\n\ruser_interest\x18\x1e \x01(\x0b\x32\x30.google.ads.googleads.v0.common.UserInterestInfoH\x00\x12>\n\x07webpage\x18\x1f \x01(\x0b\x32+.google.ads.googleads.v0.common.WebpageInfoH\x00\x12^\n\x18operating_system_version\x18  \x01(\x0b\x32:.google.ads.googleads.v0.common.OperatingSystemVersionInfoH\x00\x42\x0b\n\tcriterionB\x83\x02\n%com.google.ads.googleads.v0.resourcesB\x16\x43\x61mpaignCriterionProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resources\xea\x02%Google::Ads::GoogleAds::V0::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_criterion__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_CAMPAIGNCRITERION = _descriptor.Descriptor(
  name='CampaignCriterion',
  full_name='google.ads.googleads.v0.resources.CampaignCriterion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.CampaignCriterion.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v0.resources.CampaignCriterion.campaign', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='criterion_id', full_name='google.ads.googleads.v0.resources.CampaignCriterion.criterion_id', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_modifier', full_name='google.ads.googleads.v0.resources.CampaignCriterion.bid_modifier', index=3,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='negative', full_name='google.ads.googleads.v0.resources.CampaignCriterion.negative', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v0.resources.CampaignCriterion.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyword', full_name='google.ads.googleads.v0.resources.CampaignCriterion.keyword', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placement', full_name='google.ads.googleads.v0.resources.CampaignCriterion.placement', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile_app_category', full_name='google.ads.googleads.v0.resources.CampaignCriterion.mobile_app_category', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='google.ads.googleads.v0.resources.CampaignCriterion.location', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v0.resources.CampaignCriterion.device', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_schedule', full_name='google.ads.googleads.v0.resources.CampaignCriterion.ad_schedule', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age_range', full_name='google.ads.googleads.v0.resources.CampaignCriterion.age_range', index=12,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='google.ads.googleads.v0.resources.CampaignCriterion.gender', index=13,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='income_range', full_name='google.ads.googleads.v0.resources.CampaignCriterion.income_range', index=14,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parental_status', full_name='google.ads.googleads.v0.resources.CampaignCriterion.parental_status', index=15,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_list', full_name='google.ads.googleads.v0.resources.CampaignCriterion.user_list', index=16,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='youtube_video', full_name='google.ads.googleads.v0.resources.CampaignCriterion.youtube_video', index=17,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='youtube_channel', full_name='google.ads.googleads.v0.resources.CampaignCriterion.youtube_channel', index=18,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proximity', full_name='google.ads.googleads.v0.resources.CampaignCriterion.proximity', index=19,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic', full_name='google.ads.googleads.v0.resources.CampaignCriterion.topic', index=20,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listing_scope', full_name='google.ads.googleads.v0.resources.CampaignCriterion.listing_scope', index=21,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='google.ads.googleads.v0.resources.CampaignCriterion.language', index=22,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_block', full_name='google.ads.googleads.v0.resources.CampaignCriterion.ip_block', index=23,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_label', full_name='google.ads.googleads.v0.resources.CampaignCriterion.content_label', index=24,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='carrier', full_name='google.ads.googleads.v0.resources.CampaignCriterion.carrier', index=25,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_interest', full_name='google.ads.googleads.v0.resources.CampaignCriterion.user_interest', index=26,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='webpage', full_name='google.ads.googleads.v0.resources.CampaignCriterion.webpage', index=27,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operating_system_version', full_name='google.ads.googleads.v0.resources.CampaignCriterion.operating_system_version', index=28,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
      name='criterion', full_name='google.ads.googleads.v0.resources.CampaignCriterion.criterion',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=247,
  serialized_end=2203,
)

_CAMPAIGNCRITERION.fields_by_name['campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNCRITERION.fields_by_name['criterion_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNCRITERION.fields_by_name['bid_modifier'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_CAMPAIGNCRITERION.fields_by_name['negative'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CAMPAIGNCRITERION.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_criterion__type__pb2._CRITERIONTYPEENUM_CRITERIONTYPE
_CAMPAIGNCRITERION.fields_by_name['keyword'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._KEYWORDINFO
_CAMPAIGNCRITERION.fields_by_name['placement'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._PLACEMENTINFO
_CAMPAIGNCRITERION.fields_by_name['mobile_app_category'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._MOBILEAPPCATEGORYINFO
_CAMPAIGNCRITERION.fields_by_name['location'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._LOCATIONINFO
_CAMPAIGNCRITERION.fields_by_name['device'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._DEVICEINFO
_CAMPAIGNCRITERION.fields_by_name['ad_schedule'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._ADSCHEDULEINFO
_CAMPAIGNCRITERION.fields_by_name['age_range'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._AGERANGEINFO
_CAMPAIGNCRITERION.fields_by_name['gender'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._GENDERINFO
_CAMPAIGNCRITERION.fields_by_name['income_range'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._INCOMERANGEINFO
_CAMPAIGNCRITERION.fields_by_name['parental_status'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._PARENTALSTATUSINFO
_CAMPAIGNCRITERION.fields_by_name['user_list'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._USERLISTINFO
_CAMPAIGNCRITERION.fields_by_name['youtube_video'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._YOUTUBEVIDEOINFO
_CAMPAIGNCRITERION.fields_by_name['youtube_channel'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._YOUTUBECHANNELINFO
_CAMPAIGNCRITERION.fields_by_name['proximity'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._PROXIMITYINFO
_CAMPAIGNCRITERION.fields_by_name['topic'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._TOPICINFO
_CAMPAIGNCRITERION.fields_by_name['listing_scope'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._LISTINGSCOPEINFO
_CAMPAIGNCRITERION.fields_by_name['language'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._LANGUAGEINFO
_CAMPAIGNCRITERION.fields_by_name['ip_block'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._IPBLOCKINFO
_CAMPAIGNCRITERION.fields_by_name['content_label'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._CONTENTLABELINFO
_CAMPAIGNCRITERION.fields_by_name['carrier'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._CARRIERINFO
_CAMPAIGNCRITERION.fields_by_name['user_interest'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._USERINTERESTINFO
_CAMPAIGNCRITERION.fields_by_name['webpage'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._WEBPAGEINFO
_CAMPAIGNCRITERION.fields_by_name['operating_system_version'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_criteria__pb2._OPERATINGSYSTEMVERSIONINFO
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['keyword'])
_CAMPAIGNCRITERION.fields_by_name['keyword'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['placement'])
_CAMPAIGNCRITERION.fields_by_name['placement'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['mobile_app_category'])
_CAMPAIGNCRITERION.fields_by_name['mobile_app_category'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['location'])
_CAMPAIGNCRITERION.fields_by_name['location'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['device'])
_CAMPAIGNCRITERION.fields_by_name['device'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['ad_schedule'])
_CAMPAIGNCRITERION.fields_by_name['ad_schedule'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['age_range'])
_CAMPAIGNCRITERION.fields_by_name['age_range'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['gender'])
_CAMPAIGNCRITERION.fields_by_name['gender'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['income_range'])
_CAMPAIGNCRITERION.fields_by_name['income_range'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['parental_status'])
_CAMPAIGNCRITERION.fields_by_name['parental_status'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['user_list'])
_CAMPAIGNCRITERION.fields_by_name['user_list'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['youtube_video'])
_CAMPAIGNCRITERION.fields_by_name['youtube_video'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['youtube_channel'])
_CAMPAIGNCRITERION.fields_by_name['youtube_channel'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['proximity'])
_CAMPAIGNCRITERION.fields_by_name['proximity'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['topic'])
_CAMPAIGNCRITERION.fields_by_name['topic'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['listing_scope'])
_CAMPAIGNCRITERION.fields_by_name['listing_scope'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['language'])
_CAMPAIGNCRITERION.fields_by_name['language'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['ip_block'])
_CAMPAIGNCRITERION.fields_by_name['ip_block'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['content_label'])
_CAMPAIGNCRITERION.fields_by_name['content_label'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['carrier'])
_CAMPAIGNCRITERION.fields_by_name['carrier'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['user_interest'])
_CAMPAIGNCRITERION.fields_by_name['user_interest'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['webpage'])
_CAMPAIGNCRITERION.fields_by_name['webpage'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
_CAMPAIGNCRITERION.oneofs_by_name['criterion'].fields.append(
  _CAMPAIGNCRITERION.fields_by_name['operating_system_version'])
_CAMPAIGNCRITERION.fields_by_name['operating_system_version'].containing_oneof = _CAMPAIGNCRITERION.oneofs_by_name['criterion']
DESCRIPTOR.message_types_by_name['CampaignCriterion'] = _CAMPAIGNCRITERION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignCriterion = _reflection.GeneratedProtocolMessageType('CampaignCriterion', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNCRITERION,
  __module__ = 'google.ads.googleads_v0.proto.resources.campaign_criterion_pb2'
  ,
  __doc__ = """A campaign criterion.
  
  
  Attributes:
      resource_name:
          The resource name of the campaign criterion. Campaign
          criterion resource names have the form:  ``customers/{customer
          _id}/campaignCriteria/{campaign_id}_{criterion_id}``
      campaign:
          The campaign to which the criterion belongs.
      criterion_id:
          The ID of the criterion.  This field is ignored during mutate.
      bid_modifier:
          The modifier for the bids when the criterion matches. The
          modifier must be in the range: 0.1 - 10.0. Most targetable
          criteria types support modifiers. Use 0 to opt out of a Device
          type.
      negative:
          Whether to target (``false``) or exclude (``true``) the
          criterion.
      type:
          The type of the criterion.
      criterion:
          The campaign criterion.  Exactly one must be set.
      keyword:
          Keyword.
      placement:
          Placement.
      mobile_app_category:
          Mobile app category.
      location:
          Location.
      device:
          Device.
      ad_schedule:
          Ad Schedule.
      age_range:
          Age range.
      gender:
          Gender.
      income_range:
          Income range.
      parental_status:
          Parental status.
      user_list:
          User List.
      youtube_video:
          YouTube Video.
      youtube_channel:
          YouTube Channel.
      proximity:
          Proximity.
      topic:
          Topic.
      listing_scope:
          Listing scope.
      language:
          Language.
      ip_block:
          IpBlock.
      content_label:
          ContentLabel.
      carrier:
          Carrier.
      user_interest:
          User Interest.
      webpage:
          Webpage.
      operating_system_version:
          Operating system version.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.CampaignCriterion)
  ))
_sym_db.RegisterMessage(CampaignCriterion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
