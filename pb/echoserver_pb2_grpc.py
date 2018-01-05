# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import echoserver_pb2 as echoserver__pb2


class EchoerStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Echo = channel.unary_unary(
        '/pb.Echoer/Echo',
        request_serializer=echoserver__pb2.Request.SerializeToString,
        response_deserializer=echoserver__pb2.Response.FromString,
        )


class EchoerServicer(object):

  def Echo(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Echo': grpc.unary_unary_rpc_method_handler(
          servicer.Echo,
          request_deserializer=echoserver__pb2.Request.FromString,
          response_serializer=echoserver__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pb.Echoer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))