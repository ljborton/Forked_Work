# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v0.proto.resources import hotel_group_view_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_hotel__group__view__pb2
from google.ads.google_ads.v0.proto.services import hotel_group_view_service_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_hotel__group__view__service__pb2


class HotelGroupViewServiceStub(object):
  """Service to manage Hotel Group Views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetHotelGroupView = channel.unary_unary(
        '/google.ads.googleads.v0.services.HotelGroupViewService/GetHotelGroupView',
        request_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_hotel__group__view__service__pb2.GetHotelGroupViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_hotel__group__view__pb2.HotelGroupView.FromString,
        )


class HotelGroupViewServiceServicer(object):
  """Service to manage Hotel Group Views.
  """

  def GetHotelGroupView(self, request, context):
    """Returns the requested Hotel Group View in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HotelGroupViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetHotelGroupView': grpc.unary_unary_rpc_method_handler(
          servicer.GetHotelGroupView,
          request_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_hotel__group__view__service__pb2.GetHotelGroupViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_hotel__group__view__pb2.HotelGroupView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v0.services.HotelGroupViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
