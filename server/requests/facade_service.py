import facade_pb2 as pb2
import facade_pb2_grpc as pb2_grpc
from all_include import Caste
from facade import GameFacade


class FacadeService(pb2_grpc.FacadeServicer):
    def __init__(self, games, *args, **kwargs):
        self.games = games
        self.ind = -1

    def CreateNewGameSession(self, request, context):
        self.ind += 1
        self.games[self.ind] = GameFacade()
        result = {"game_id": self.ind}
        return pb2.Empty(**result)

    def GetUniqueId(self, request, context):
        result = {"player_id": self.games[request.game_id].get_unique_id()}
        return pb2.PlayerId(**result)

    def AddPlayer(self, request, context):
        result = {"key": self.games[request.game_id].add_player(request.player_id, request.name)}
        return pb2.Key(**result)

    def SwapPlayerReadinessValue(self, request, context):
        result = {"key": self.games[request.game_id].swap_player_readiness_value(request.player_id)}
        return pb2.Key(**result)

    def GetPlayers(self, request, context):
        list_int = pb2.ListName(
            name=[pb2.Name(player_id=item.player_id, name=item.name, readiness=item.ready_to_play) for item in
                  self.games[request.game_id].get_players()])
        return list_int

    def GetPossiblePositionsBattleToken(self, request, context):
        position = pb2.Map()
        for line in self.games[request.game_id].get_possible_positions_battle_token():
            lst = pb2.List()
            lst.cell[:] = line
            position.line.append(lst)
        return position

    def PutBattleToken(self, request, context):
        result = {"key": self.games[request.game_id].put_battle_token(request.player_id, request.my_token_id,
                                                                      request.province_from_id,
                                                                      request.province_to_id)}
        return pb2.Key(**result)

    def GetSomeoneReset(self, request, context):
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
                for token in self.games[request.game_id].get_someone_reset(request.player_id)]
        )
        return list_tokens

    def GetPlayerActive(self, request, context):
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
                for token in self.games[request.game_id].get_player_active(request.player_id)]
        )
        return list_tokens

    def GetRound(self, request, context):
        result = {"round": self.games[request.game_id].get_round()}
        return pb2.Round(**result)

    def WhoseMove(self, request, context):
        result = {"player_id": self.games[request.game_id].whose_move()}
        return pb2.Player(**result)

    def GetAllControlToken(self, request, context):
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
        result = {"key": self.games[request.game_id].use_card(request.player_id, request.card_id, *request.values)}
        return pb2.Key(**result)

    def UnusedCard(self, request, context):
        result = {"key": self.games[request.game_id].unused_card(request.player_id)}
        return pb2.Key(**result)

    def GetAllCards(self, request, context):
        list_cards = pb2.ListCards(
            token=[
                pb2.Card(player_id=card.owner,
                         card_id=card.ind,
                         caste=card.caste.value,
                         data=[pb2.Data(data=item.value) for item in card.data],
                         used=card.used)
                for card in self.games[request.game_id].get_all_card()])
        return list_cards

    def DoExecutionPhase(self, request, context):
        self.games[request.game_id].do_execution_phase()
        return pb2.Empty()

    def GetWinner(self, request, context):
        self.games[request.game_id].get_winner()
        return pb2.Empty()

    def GetFreeCaste(self, request, context):
        list_caste = pb2.ListCaste()
        list_caste.caste[:] = [caste.value for caste in self.games[request.game_id].get_free_caste()]
        return list_caste

    def SetCaste(self, request, context):
        result = {"key": self.games[request.game_id].set_caste(request.player_id, Caste(request.caste))}
        return pb2.Key(**result)

    def GetPossiblePositionsControlToken(self, request, context):
        list_pos_tokens = pb2.ListPositionsControlTokens(
            position=self.games[request.game_id].get_possible_positions_control_token())
        return list_pos_tokens

    def PutControlToken(self, request, context):
        result = {"key": self.games[request.game_id].put_control_token(request.player_id, request.province_id)}
        return pb2.Key(**result)

    def GetPhase(self, request, context):
        result = {"round": self.games[request.game_id].get_phase()}
        return pb2.Round(**result)

    def GetAllSpecialToken(self, request, context):
        list_tokens = pb2.ListBattleTokens(
            token=[
                pb2.SpecialToken(token=token[1].value,
                                 province_id=tokens[0])
                for tokens in self.games[request.game_id].get_all_special_tokens()]
        )
        return list_tokens
