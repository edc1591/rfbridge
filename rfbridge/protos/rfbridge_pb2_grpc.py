# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import rfbridge_pb2 as rfbridge__pb2


class RFBridgeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SendCommand = channel.unary_unary(
        '/rfbridge.RFBridge/SendCommand',
        request_serializer=rfbridge__pb2.CommandRequest.SerializeToString,
        response_deserializer=rfbridge__pb2.CommandResponse.FromString,
        )


class RFBridgeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SendCommand(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RFBridgeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SendCommand': grpc.unary_unary_rpc_method_handler(
          servicer.SendCommand,
          request_deserializer=rfbridge__pb2.CommandRequest.FromString,
          response_serializer=rfbridge__pb2.CommandResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rfbridge.RFBridge', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
