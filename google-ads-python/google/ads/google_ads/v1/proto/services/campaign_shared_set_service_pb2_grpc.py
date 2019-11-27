# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import campaign_shared_set_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__shared__set__pb2
from google.ads.google_ads.v1.proto.services import campaign_shared_set_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__shared__set__service__pb2


class CampaignSharedSetServiceStub(object):
  """Service to manage campaign shared sets.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCampaignSharedSet = channel.unary_unary(
        '/google.ads.googleads.v1.services.CampaignSharedSetService/GetCampaignSharedSet',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__shared__set__service__pb2.GetCampaignSharedSetRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__shared__set__pb2.CampaignSharedSet.FromString,
        )
    self.MutateCampaignSharedSets = channel.unary_unary(
        '/google.ads.googleads.v1.services.CampaignSharedSetService/MutateCampaignSharedSets',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__shared__set__service__pb2.MutateCampaignSharedSetsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__shared__set__service__pb2.MutateCampaignSharedSetsResponse.FromString,
        )


class CampaignSharedSetServiceServicer(object):
  """Service to manage campaign shared sets.
  """

  def GetCampaignSharedSet(self, request, context):
    """Returns the requested campaign shared set in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCampaignSharedSets(self, request, context):
    """Creates or removes campaign shared sets. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CampaignSharedSetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCampaignSharedSet': grpc.unary_unary_rpc_method_handler(
          servicer.GetCampaignSharedSet,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__shared__set__service__pb2.GetCampaignSharedSetRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__shared__set__pb2.CampaignSharedSet.SerializeToString,
      ),
      'MutateCampaignSharedSets': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCampaignSharedSets,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__shared__set__service__pb2.MutateCampaignSharedSetsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__shared__set__service__pb2.MutateCampaignSharedSetsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.CampaignSharedSetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
