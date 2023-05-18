import facade_pb2 as pb2
import facade_pb2_grpc as pb2_grpc
from facade import GameFacade


class FacadeService(pb2_grpc.FacadeServicer):

    def __init__(self, fd: GameFacade, *args, **kwargs):
        self.facade = fd

    def GetPossiblePositionsBattleToken(self, request, context):
        print("GetPossiblePositionsBattleToken")
        position = pb2.Map()
        for line in self.facade.get_possible_positions_battle_token():
            lst = pb2.List()
            lst.cell[:] = line
            position.line.append(lst)
        return position

    def PutBattleToken(self, request, context):
        print("PutBattleToken")
        result = {"key": self.facade.put_battle_token(request.player_id, request.my_token_id, request.province_from_id,
                                                      request.province_to_id)}
        return pb2.Key(**result)

    def ShowSomeoneReset(self, request, context):
        print("ShowSomeoneReset")
        list_tokens = pb2.ListBattleTokens(
            token=[
                pb2.BattleToken(caste=token.visible,
                                power=token.power,
                                type=token.type,
                                on_board_first=token.on_board[0],
                                on_board_second=token.on_board[1],
                                in_reset=token.in_reset,
                                in_active=token.in_active,
                                visible=token.visible,
                                id=token.id)
                for token in self.facade.show_someone_reset(request.player_id)]
        )
        return list_tokens

    def ShowActive(self, request, context):
        print("ShowActive")
        list_tokens = pb2.ListBattleTokens(
            token=[
                pb2.BattleToken(caste=token.visible,
                                power=token.power,
                                type=token.type,
                                on_board_first=token.on_board[0],
                                on_board_second=token.on_board[1],
                                in_reset=token.in_reset,
                                in_active=token.in_active,
                                visible=token.visible,
                                id=token.id)
                for token in self.facade.show_active(request.player_id)]
        )
        return list_tokens

    def RoundCount(self, request, context):
        print("RoundCount")
        result = {"round": self.facade.round_count()}
        return pb2.Round(**result)

    def WhoseMove(self, request, context):
        print("WhoseMove")
        result = {"player_id": self.facade.whose_move()}
        return pb2.Player(**result)

    def ShowBattleToken(self, request, context):
        print("ShowBattleToken")
        token = self.facade.show_battle_token(request.player_id, request.my_token_id)
        result = {"caste": token.visible,
                  "power": token.power,
                  "type": token.type,
                  "on_board_first": token.on_board[0],
                  "on_board_second": token.on_board[1],
                  "in_reset": token.in_reset,
                  "in_active": token.in_active,
                  "visible": token.visible,
                  "id": token.id}
        return pb2.BattleToken(**result)

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

    def GetAllBattleToken(self, request, context):
        print("GetAllBattleToken")
        list_tokens = pb2.ListBattleTokens(
            token=[
                pb2.BattleToken(caste=token.visible,
                                power=token.power,
                                type=token.type,
                                on_board_first=token.on_board[0],
                                on_board_second=token.on_board[1],
                                in_reset=token.in_reset,
                                in_active=token.in_active,
                                visible=token.visible,
                                id=token.id)
                for token in self.facade.get_all_battle_token()]
        )
        return list_tokens

    def UseCard(self, request, context):
        print("UseCard")
        result = {"key": self.facade.use_card(request.player_id, request.card_id)}
        return pb2.Key(**result)

    def UnusedCard(self, request, context):
        print("UnusedCard")
        result = {"key": self.facade.unused_card(request.player_id)}
        return pb2.Key(**result)

    def GetAllMyCards(self, request, context):  # Not soon
        print("GetAllMyCards")
        return pb2.Empty()

    def DoExecutionPhase(self, request, context):
        print("DoExecutionPhase")
        self.facade.do_execution_phase()
        return pb2.Empty()

    def GetWinner(self, request, context):
        print("GetWinner")
        self.facade.get_winner()
        return pb2.Empty()
