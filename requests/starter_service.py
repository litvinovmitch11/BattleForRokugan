import starter_pb2 as pb2
import starter_pb2_grpc as pb2_grpc
import facade


class StarterService(pb2_grpc.StarterServicer):

    def __init__(self, fd: facade.StarterFacade, *args, **kwargs):
        self.facade = fd

    def add_player(self, request, context):
        print("AddPlayer")
        result = {"key": self.facade.add_player(request.PlayerId)}
        return pb2.Key(**result)

    def get_unique_id(self, request, context):
        print("GetUniqueId")
        result = {"PlayerId": self.facade.get_unique_id()}
        return pb2.PlayerId(**result)
