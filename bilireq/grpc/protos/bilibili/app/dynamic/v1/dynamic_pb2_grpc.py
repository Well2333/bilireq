# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bilibili.app.dynamic.v1 import dynamic_pb2 as bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2


class DynamicStub(object):
    """v1动态
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DynVideo = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynVideo',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoReqReply.FromString,
                )
        self.DynDetails = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynDetails',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynDetailsReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynDetailsReply.FromString,
                )
        self.SVideo = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/SVideo',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.SVideoReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.SVideoReply.FromString,
                )
        self.DynTab = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynTab',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynTabReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynTabReply.FromString,
                )
        self.DynOurCitySwitch = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynOurCitySwitch',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCitySwitchReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReply.FromString,
                )
        self.DynOurCity = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynOurCity',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCityReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCityReply.FromString,
                )
        self.DynVideoPersonal = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynVideoPersonal',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoPersonalReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoPersonalReply.FromString,
                )
        self.DynUpdOffset = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynUpdOffset',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynUpdOffsetReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReply.FromString,
                )
        self.DynRed = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynRed',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynRedReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynRedReply.FromString,
                )
        self.DynMixUpListViewMore = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynMixUpListViewMore',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListViewMoreReply.FromString,
                )
        self.DynMixUpListSearch = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/DynMixUpListSearch',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListSearchReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListSearchReply.FromString,
                )
        self.OurCityClickReport = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/OurCityClickReport',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.OurCityClickReportReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.OurCityClickReportReply.FromString,
                )
        self.GeoCoder = channel.unary_unary(
                '/bilibili.app.dynamic.v1.Dynamic/GeoCoder',
                request_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.GeoCoderReq.SerializeToString,
                response_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.GeoCoderReply.FromString,
                )


class DynamicServicer(object):
    """v1动态
    """

    def DynVideo(self, request, context):
        """动态视频页
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynDetails(self, request, context):
        """批量动态id获取动态详情
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SVideo(self, request, context):
        """小视频连播页
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynTab(self, request, context):
        """动态tab页
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynOurCitySwitch(self, request, context):
        """同城接口开关
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynOurCity(self, request, context):
        """动态同城页
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynVideoPersonal(self, request, context):
        """最近访问-个人视频feed流
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynUpdOffset(self, request, context):
        """最近访问-标记已读
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynRed(self, request, context):
        """动态红点接口
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynMixUpListViewMore(self, request, context):
        """查看更多-列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DynMixUpListSearch(self, request, context):
        """查看更多-搜索
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OurCityClickReport(self, request, context):
        """同城点击上报
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GeoCoder(self, request, context):
        """位置定位
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DynamicServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DynVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.DynVideo,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoReqReply.SerializeToString,
            ),
            'DynDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.DynDetails,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynDetailsReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynDetailsReply.SerializeToString,
            ),
            'SVideo': grpc.unary_unary_rpc_method_handler(
                    servicer.SVideo,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.SVideoReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.SVideoReply.SerializeToString,
            ),
            'DynTab': grpc.unary_unary_rpc_method_handler(
                    servicer.DynTab,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynTabReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynTabReply.SerializeToString,
            ),
            'DynOurCitySwitch': grpc.unary_unary_rpc_method_handler(
                    servicer.DynOurCitySwitch,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCitySwitchReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReply.SerializeToString,
            ),
            'DynOurCity': grpc.unary_unary_rpc_method_handler(
                    servicer.DynOurCity,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCityReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCityReply.SerializeToString,
            ),
            'DynVideoPersonal': grpc.unary_unary_rpc_method_handler(
                    servicer.DynVideoPersonal,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoPersonalReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoPersonalReply.SerializeToString,
            ),
            'DynUpdOffset': grpc.unary_unary_rpc_method_handler(
                    servicer.DynUpdOffset,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynUpdOffsetReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReply.SerializeToString,
            ),
            'DynRed': grpc.unary_unary_rpc_method_handler(
                    servicer.DynRed,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynRedReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynRedReply.SerializeToString,
            ),
            'DynMixUpListViewMore': grpc.unary_unary_rpc_method_handler(
                    servicer.DynMixUpListViewMore,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListViewMoreReply.SerializeToString,
            ),
            'DynMixUpListSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.DynMixUpListSearch,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListSearchReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListSearchReply.SerializeToString,
            ),
            'OurCityClickReport': grpc.unary_unary_rpc_method_handler(
                    servicer.OurCityClickReport,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.OurCityClickReportReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.OurCityClickReportReply.SerializeToString,
            ),
            'GeoCoder': grpc.unary_unary_rpc_method_handler(
                    servicer.GeoCoder,
                    request_deserializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.GeoCoderReq.FromString,
                    response_serializer=bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.GeoCoderReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.app.dynamic.v1.Dynamic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Dynamic(object):
    """v1动态
    """

    @staticmethod
    def DynVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynVideo',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoReqReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynDetails',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynDetailsReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynDetailsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SVideo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/SVideo',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.SVideoReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.SVideoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynTab(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynTab',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynTabReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynTabReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynOurCitySwitch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynOurCitySwitch',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCitySwitchReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynOurCity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynOurCity',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCityReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynOurCityReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynVideoPersonal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynVideoPersonal',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoPersonalReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynVideoPersonalReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynUpdOffset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynUpdOffset',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynUpdOffsetReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynRed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynRed',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynRedReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynRedReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynMixUpListViewMore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynMixUpListViewMore',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.NoReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListViewMoreReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DynMixUpListSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/DynMixUpListSearch',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListSearchReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.DynMixUpListSearchReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OurCityClickReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/OurCityClickReport',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.OurCityClickReportReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.OurCityClickReportReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GeoCoder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.app.dynamic.v1.Dynamic/GeoCoder',
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.GeoCoderReq.SerializeToString,
            bilibili_dot_app_dot_dynamic_dot_v1_dot_dynamic__pb2.GeoCoderReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)