import starter_pb2 as pb2
import starter_pb2_grpc as pb2_grpc
from facade import StarterFacade

from all_include import Caste


class StarterService(pb2_grpc.StarterServicer):

    def __init__(self, fd: StarterFacade, *args, **kwargs):
        self.facade = fd

    def GetUniqueId(self, request, context):
        print("GetUniqueId")
        result = {"player_id": self.facade.get_unique_id()}
        return pb2.PlayerId(**result)

    def AddPlayer(self, request, context):
        print("AddPlayer")
        result = {"key": self.facade.add_player(request.player_id)}
        return pb2.Key(**result)

    def SwapPlayerReadinessValue(self, request, context):
        print("SwapPlayerReadinessValue")
        result = {"key": self.facade.swap_player_readiness_value(request.player_id)}
        return pb2.Key(**result)

    def GetFreeCaste(self, request, context):
        print("GetFreeCaste")
        list_caste = pb2.ListCaste()
        list_caste.caste[:] = [caste.value for caste in self.facade.get_free_caste()]
        return list_caste

    def SetCaste(self, request, context):
        print("SetCaste")
        result = {"key": self.facade.set_caste(request.player_id, Caste(request.caste))}
        return pb2.Key(**result)

    def GetPossiblePositionsControlToken(self, request, context):
        print("GetPossiblePositionsControlToken")
        list_pos_tokens = pb2.ListPositionsControlTokens(position=self.facade.get_possible_positions_control_token())
        return list_pos_tokens

    def PutControlToken(self, request, context):
        print("PutControlToken")
        result = {"key": self.facade.put_control_token(request.player_id, request.token_id, request.province_id)}
        return pb2.Key(**result)

    def RoundCount(self, request, context):
        print("RoundCount")
        result = {"round": self.facade.round_count()}
        return pb2.Round(**result)

    def GetAllControlToken(self, request, context):
        print("GetAllControlToken")
        list_tokens = pb2.ListControlTokens(
            token=[
                pb2.ControlToken(visible=token.visible,
                                 province_id=token.province_id,
                                 power=token.power,
                                 caste=token.caste.value,
                                 id=token.id)
                for token in self.facade.get_all_control_token()]
        )
        return list_tokens
