# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import basic_pb2 as basic__pb2


class BasicStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Echo = channel.unary_unary(
                '/basic.Basic/Echo',
                request_serializer=basic__pb2.Message.SerializeToString,
                response_deserializer=basic__pb2.Message.FromString,
                )


class BasicServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Echo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BasicServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Echo': grpc.unary_unary_rpc_method_handler(
                    servicer.Echo,
                    request_deserializer=basic__pb2.Message.FromString,
                    response_serializer=basic__pb2.Message.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'basic.Basic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Basic(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Echo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/basic.Basic/Echo',
            basic__pb2.Message.SerializeToString,
            basic__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
