import grpc

import facade_pb2 as pb2
import facade_pb2_grpc as pb2_grpc


class Client:
    def __init__(self, host='localhost', port='8888'):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.game_stub = pb2_grpc.FacadeStub(self.channel)

    def create_new_game_session(self):
        return self.game_stub.CreateNewGameSession(pb2.SuperEmpty())

    def get_unique_id(self, game_id):
        return self.game_stub.GetUniqueId(pb2.Empty(game_id=game_id))

    def add_player(self, player_id, name, game_id, login, password):
        return self.game_stub.AddPlayer(
            pb2.NameLogin(game_id=game_id, player_id=player_id, name=name, login=login, password=password))

    def swap_player_readiness_value(self, player_id, game_id):
        return self.game_stub.SwapPlayerReadinessValue(pb2.PlayerId(game_id=game_id, player_id=player_id))

    def get_players(self, game_id):
        return self.game_stub.GetPlayers(pb2.Empty(game_id=game_id))

    def get_possible_positions_battle_token(self, game_id):
        return self.game_stub.GetPossiblePositionsBattleToken(pb2.Empty(game_id=game_id))

    def put_battle_token(self, player_id, my_token_id, province_from_id, province_to_id, game_id):
        return self.game_stub.PutBattleToken(
            pb2.Attack(game_id=game_id, player_id=player_id, my_token_id=my_token_id,
                       province_from_id=province_from_id,
                       province_to_id=province_to_id))

    def get_someone_reset(self, player_id, game_id):
        return self.game_stub.GetSomeoneReset(pb2.Player(game_id=game_id, player_id=player_id))

    def get_player_active(self, player_id, game_id):
        return self.game_stub.GetPlayerActive(pb2.Player(game_id=game_id, player_id=player_id))

    def get_round(self, game_id):
        return self.game_stub.GetRound(pb2.Empty(game_id=game_id))

    def whose_move(self, game_id):
        return self.game_stub.WhoseMove(pb2.Empty(game_id=game_id))

    def get_all_control_token(self, game_id):
        return self.game_stub.GetAllControlToken(pb2.Empty(game_id=game_id))

    def get_all_battle_token(self, game_id):
        return self.game_stub.GetAllBattleToken(pb2.Empty(game_id=game_id))

    def use_card(self, player_id, card_id, game_id, values):
        data = pb2.CardForUse(game_id=game_id, player_id=player_id, card_id=card_id)
        data.values.extend(values)
        return self.game_stub.UseCard(data)

    def unused_card(self, player_id, game_id):
        return self.game_stub.UnusedCard(pb2.Player(game_id=game_id, player_id=player_id))

    def get_all_cards(self, game_id):
        return self.game_stub.GetAllCards(pb2.Empty(game_id=game_id))

    def get_winner(self, game_id):
        return self.game_stub.GetWinner(pb2.Empty(game_id=game_id))

    def get_free_caste(self, game_id):
        return self.game_stub.GetFreeCaste(pb2.Empty(game_id=game_id))

    def set_caste(self, player_id, caste, game_id):
        return self.game_stub.SetCaste(pb2.Caste(game_id=game_id, player_id=player_id, caste=caste))

    def get_possible_positions_control_token(self, game_id):
        return self.game_stub.GetPossiblePositionsControlToken(pb2.Empty(game_id=game_id))

    def put_control_token(self, player_id, province_id, game_id):
        return self.game_stub.PutControlToken(
            pb2.Put(game_id=game_id, player_id=player_id, province_id=province_id))

    def get_phase(self, game_id):
        return self.game_stub.GetPhase(pb2.Empty(game_id=game_id))

    def get_all_special_tokens(self, game_id):
        return self.game_stub.GetAllSpecialToken(pb2.Empty(game_id=game_id))

    def get_score(self, game_id):
        return self.game_stub.GetScore(pb2.Empty(game_id=game_id))
