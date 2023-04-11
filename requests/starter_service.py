import starter_pb2 as pb2
import starter_pb2_grpc as pb2_grpc
from facade import StarterFacade


class StarterService(pb2_grpc.StarterServicer):

    def __init__(self, fd: StarterFacade, *args, **kwargs):
        self.facade = fd

    def GetUniqueId(self, request, context):
        print("GetUniqueId")
        result = {"player_id": self.facade.get_unique_id()}
        return pb2.PlayerId(**result)

    def AddPlayer(self, request, context):
        print("AddPlayer")
        key = self.facade.add_player(request.player_id)
        result = {"key": key}
        return pb2.Key(**result)

    # def get_free_caste(self, request, context):
    #     print("GetFreeCaste")
    #     list_caste = pb2.ListCaste()
    #     list_caste.caste = list(map(str, self.facade.get_free_caste()))
    #     return list_caste
