import facade_pb2 as pb2
import facade_pb2_grpc as pb2_grpc

from facade import GameFacade
from all_include import Caste


class FacadeService(pb2_grpc.FacadeServicer):

    def __init__(self, games, *args, **kwargs):
        self.games = games
        self.ind = -1

    def CreateNewGameSession(self, request, context):
        print("CreateNewGameSession")
        self.ind += 1
        self.games[self.ind] = GameFacade()
        result = {"game_id": self.ind}
        return pb2.Empty(**result)

    def GetUniqueId(self, request, context):
        print("GetUniqueId")
        result = {"player_id": self.games[request.game_id].get_unique_id()}
        return pb2.PlayerId(**result)

    def AddPlayer(self, request, context):
        print("AddPlayer")
        result = {"key": self.games[request.game_id].add_player(request.player_id, request.name)}
        return pb2.Key(**result)

    def SwapPlayerReadinessValue(self, request, context):
        print("SwapPlayerReadinessValue")
        result = {"key": self.games[request.game_id].swap_player_readiness_value(request.player_id)}
        return pb2.Key(**result)

    def GetPlayers(self, request, context):
        print("GetPlayersIds")
        list_int = pb2.ListName(
            name=[pb2.Name(player_id=item[0], name=item[1]) for item in self.games[request.game_id].get_players()])
        return list_int

    def GetPossiblePositionsBattleToken(self, request, context):
        print("GetPossiblePositionsBattleToken")
        position = pb2.Map()
        for line in self.games[request.game_id].get_possible_positions_battle_token():
            lst = pb2.List()
            lst.cell[:] = line
            position.line.append(lst)
        return position

    def PutBattleToken(self, request, context):
        print("PutBattleToken")
        result = {"key": self.games[request.game_id].put_battle_token(request.player_id, request.my_token_id,
                                                                      request.province_from_id,
                                                                      request.province_to_id)}
        return pb2.Key(**result)

    def ShowSomeoneReset(self, request, context):
        print("ShowSomeoneReset")
        list_tokens = pb2.ListBattleTokens(
            token=[
                pb2.BattleToken(caste=token.caste.value,
                                power=token.power,
                                type=token.type.value,
                                on_board_first=token.on_board[0],
                                on_board_second=token.on_board[1],
                                in_reset=token.in_reset,
                                in_active=token.in_active,
                                visible=token.visible,
                                id=token.id)
                for token in self.games[request.game_id].show_someone_reset(request.player_id)]
        )
        return list_tokens

    def ShowActive(self, request, context):
        print("ShowActive")
        list_tokens = pb2.ListBattleTokens(
            token=[
                pb2.BattleToken(caste=token.caste.value,
                                power=token.power,
                                type=token.type.value,
                                on_board_first=token.on_board[0],
                                on_board_second=token.on_board[1],
                                in_reset=token.in_reset,
                                in_active=token.in_active,
                                visible=token.visible,
                                id=token.id)
                for token in self.games[request.game_id].show_active(request.player_id)]
        )
        return list_tokens

    def RoundCount(self, request, context):
        print("RoundCount")
        result = {"round": self.games[request.game_id].round_count()}
        return pb2.Round(**result)

    def WhoseMove(self, request, context):
        print("WhoseMove")
        result = {"player_id": self.games[request.game_id].whose_move()}
        return pb2.Player(**result)

    def ShowBattleToken(self, request, context):
        print("ShowBattleToken")
        token = self.games[request.game_id].show_battle_token(request.player_id, request.my_token_id)
        result = {"caste": token.caste.value,
                  "power": token.power,
                  "type": token.type.value,
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
                for token in self.games[request.game_id].get_all_control_token()]
        )
        return list_tokens

    def GetAllBattleToken(self, request, context):
        print("GetAllBattleToken")
        list_tokens = pb2.ListBattleTokens(
            token=[
                pb2.BattleToken(caste=token.caste.value,
                                power=token.power,
                                type=token.type.value,
                                on_board_first=token.on_board[0],
                                on_board_second=token.on_board[1],
                                in_reset=token.in_reset,
                                in_active=token.in_active,
                                visible=token.visible,
                                id=token.id)
                for token in self.games[request.game_id].get_all_battle_token()]
        )
        return list_tokens

    def UseCard(self, request, context):
        print("UseCard")
        result = {"key": self.games[request.game_id].use_card(request.player_id, request.card_id)}
        return pb2.Key(**result)

    def UnusedCard(self, request, context):
        print("UnusedCard")
        result = {"key": self.games[request.game_id].unused_card(request.player_id)}
        return pb2.Key(**result)

    def GetAllMyCards(self, request, context):  # Not soon
        print("GetAllMyCards")
        return pb2.Empty()

    def DoExecutionPhase(self, request, context):
        print("DoExecutionPhase")
        self.games[request.game_id].do_execution_phase()
        return pb2.Empty()

    def GetWinner(self, request, context):
        print("GetWinner")
        self.games[request.game_id].get_winner()
        return pb2.Empty()

    def GetFreeCaste(self, request, context):
        print("GetFreeCaste")
        list_caste = pb2.ListCaste()
        list_caste.caste[:] = [caste.value for caste in self.games[request.game_id].get_free_caste()]
        return list_caste

    def SetCaste(self, request, context):
        print("SetCaste")
        result = {"key": self.games[request.game_id].set_caste(request.player_id, Caste(request.caste))}
        return pb2.Key(**result)

    def GetPossiblePositionsControlToken(self, request, context):
        print("GetPossiblePositionsControlToken")
        list_pos_tokens = pb2.ListPositionsControlTokens(
            position=self.games[request.game_id].get_possible_positions_control_token())
        return list_pos_tokens

    def PutControlToken(self, request, context):
        print("PutControlToken")
        result = {"key": self.games[request.game_id].put_control_token(request.player_id, request.token_id,
                                                                       request.province_id)}
        return pb2.Key(**result)

    def GetPhase(self, request, context):
        print("GetPhase")
        result = {"round": self.games[request.game_id].get_phase()}
        return pb2.Round(**result)
