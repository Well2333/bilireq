# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilireq.grpc.protos.bilibili.app.dynamic.v2 import opus_pb2 as bilibili_dot_app_dot_dynamic_dot_v2_dot_opus__pb2


class OpusStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OpusDetail = channel.unary_unary(
                '/bilibili.app.dynamic.v2.Opus/OpusDetail',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v2_dot_opus__pb2.OpusDetailReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v2_dot_opus__pb2.OpusDetailResp.FromString,
                )


class OpusServicer(object):
    """Missing associated documentation comment in .proto file."""

    def OpusDetail(self, request, context):
        """
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OpusServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OpusDetail': grpc.unary_unary_rpc_method_handler(
                    servicer.OpusDetail,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v2_dot_opus__pb2.OpusDetailReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v2_dot_opus__pb2.OpusDetailResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.app.dynamic.v2.Opus', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Opus(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def OpusDetail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v2.Opus/OpusDetail',
            bilibili_dot_app_dot_dynamic_dot_v2_dot_opus__pb2.OpusDetailReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v2_dot_opus__pb2.OpusDetailResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)