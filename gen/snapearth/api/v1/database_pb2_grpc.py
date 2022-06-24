# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from snapearth.api.v1 import database_pb2 as snapearth_dot_api_dot_v1_dot_database__pb2


class DatabaseProductServiceStub(object):
    """Service that exposes the EarthSignature database.
    The service exposes two endpoints for its consumers
    - ListSegmentation to query a list of segmentation responses
    - CreateProduct to add a new product in the database
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListSegmentation = channel.unary_stream(
                '/snapearth.api.v1.database.DatabaseProductService/ListSegmentation',
                request_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.ListSegmentationRequest.SerializeToString,
                response_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.SegmentationResponse.FromString,
                )
        self.CreateProduct = channel.unary_unary(
                '/snapearth.api.v1.database.DatabaseProductService/CreateProduct',
                request_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.CreateProductRequest.SerializeToString,
                response_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.CreateProductResponse.FromString,
                )
        self.SearchSegmentation = channel.unary_stream(
                '/snapearth.api.v1.database.DatabaseProductService/SearchSegmentation',
                request_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.SearchSegmentationRequest.SerializeToString,
                response_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.SegmentationResponse.FromString,
                )
        self.ListProductIds = channel.unary_stream(
                '/snapearth.api.v1.database.DatabaseProductService/ListProductIds',
                request_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.ListProductIdsRequest.SerializeToString,
                response_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.ProductId.FromString,
                )


class DatabaseProductServiceServicer(object):
    """Service that exposes the EarthSignature database.
    The service exposes two endpoints for its consumers
    - ListSegmentation to query a list of segmentation responses
    - CreateProduct to add a new product in the database
    """

    def ListSegmentation(self, request, context):
        """Query the database and returns a list of SegmentationResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProduct(self, request, context):
        """Add a new product in the database
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchSegmentation(self, request, context):
        """Method to search a list of segmentation with textual query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProductIds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatabaseProductServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListSegmentation': grpc.unary_stream_rpc_method_handler(
                    servicer.ListSegmentation,
                    request_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.ListSegmentationRequest.FromString,
                    response_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.SegmentationResponse.SerializeToString,
            ),
            'CreateProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProduct,
                    request_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.CreateProductRequest.FromString,
                    response_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.CreateProductResponse.SerializeToString,
            ),
            'SearchSegmentation': grpc.unary_stream_rpc_method_handler(
                    servicer.SearchSegmentation,
                    request_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.SearchSegmentationRequest.FromString,
                    response_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.SegmentationResponse.SerializeToString,
            ),
            'ListProductIds': grpc.unary_stream_rpc_method_handler(
                    servicer.ListProductIds,
                    request_deserializer=snapearth_dot_api_dot_v1_dot_database__pb2.ListProductIdsRequest.FromString,
                    response_serializer=snapearth_dot_api_dot_v1_dot_database__pb2.ProductId.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'snapearth.api.v1.database.DatabaseProductService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatabaseProductService(object):
    """Service that exposes the EarthSignature database.
    The service exposes two endpoints for its consumers
    - ListSegmentation to query a list of segmentation responses
    - CreateProduct to add a new product in the database
    """

    @staticmethod
    def ListSegmentation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/snapearth.api.v1.database.DatabaseProductService/ListSegmentation',
            snapearth_dot_api_dot_v1_dot_database__pb2.ListSegmentationRequest.SerializeToString,
            snapearth_dot_api_dot_v1_dot_database__pb2.SegmentationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/snapearth.api.v1.database.DatabaseProductService/CreateProduct',
            snapearth_dot_api_dot_v1_dot_database__pb2.CreateProductRequest.SerializeToString,
            snapearth_dot_api_dot_v1_dot_database__pb2.CreateProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchSegmentation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/snapearth.api.v1.database.DatabaseProductService/SearchSegmentation',
            snapearth_dot_api_dot_v1_dot_database__pb2.SearchSegmentationRequest.SerializeToString,
            snapearth_dot_api_dot_v1_dot_database__pb2.SegmentationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProductIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/snapearth.api.v1.database.DatabaseProductService/ListProductIds',
            snapearth_dot_api_dot_v1_dot_database__pb2.ListProductIdsRequest.SerializeToString,
            snapearth_dot_api_dot_v1_dot_database__pb2.ProductId.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)