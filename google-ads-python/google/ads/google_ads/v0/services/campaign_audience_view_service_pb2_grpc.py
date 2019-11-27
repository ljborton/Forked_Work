# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v0.proto.resources import campaign_audience_view_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__audience__view__pb2
from google.ads.google_ads.v0.proto.services import campaign_audience_view_service_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_campaign__audience__view__service__pb2


class CampaignAudienceViewServiceStub(object):
  """Service to manage campaign audience views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCampaignAudienceView = channel.unary_unary(
        '/google.ads.googleads.v0.services.CampaignAudienceViewService/GetCampaignAudienceView',
        request_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_campaign__audience__view__service__pb2.GetCampaignAudienceViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__audience__view__pb2.CampaignAudienceView.FromString,
        )


class CampaignAudienceViewServiceServicer(object):
  """Service to manage campaign audience views.
  """

  def GetCampaignAudienceView(self, request, context):
    """Returns the requested campaign audience view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CampaignAudienceViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCampaignAudienceView': grpc.unary_unary_rpc_method_handler(
          servicer.GetCampaignAudienceView,
          request_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_campaign__audience__view__service__pb2.GetCampaignAudienceViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_campaign__audience__view__pb2.CampaignAudienceView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v0.services.CampaignAudienceViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
