import grpc
import starter_pb2
import starter_pb2_grpc
import facade_pb2
import facade_pb2_grpc


class Client(object):

    def __init__(self, host='localhost', port='8888'):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.starter_stub = starter_pb2_grpc.StarterStub(self.channel)
        self.game_stub = facade_pb2_grpc.FacadeStub(self.channel)

    # ------------- Starter part -------------
    def create_new_game_session(self, game_id=0):
        print("CreateNewGameSession")
        return self.starter_stub.CreateNewGameSession(starter_pb2.Empty(game_id=game_id))

    def get_unique_id(self, game_id=0):
        print("GetUniqueId")
        return self.starter_stub.GetUniqueId(starter_pb2.Empty(game_id=game_id))

    def add_player(self, player_id, game_id=0):
        print("AddPlayer")
        return self.starter_stub.AddPlayer(starter_pb2.PlayerId(game_id=game_id, player_id=player_id))

    def swap_player_readiness_value(self, player_id, game_id=0):
        print("SwapPlayerReadinessValue")
        return self.starter_stub.SwapPlayerReadinessValue(starter_pb2.PlayerId(game_id=game_id, player_id=player_id))

    def should_start_game(self, game_id=0):
        print("ShouldStartGame")
        return self.starter_stub.ShouldStartGame(starter_pb2.Empty(game_id=game_id))

    def get_players_ids(self, game_id=0):
        print("GetPlayersIds")
        return self.starter_stub.GetPlayersIds(starter_pb2.Empty(game_id=game_id))

    # ------------- Game part -------------
    def get_possible_positions_battle_token(self, game_id=0):
        print("GetPossiblePositionsBattleToken")
        return self.game_stub.GetPossiblePositionsBattleToken(facade_pb2.Empty(game_id=game_id))

    def put_battle_token(self, player_id, my_token_id, province_from_id, province_to_id, game_id=0):
        print("PutBattleToken")
        return self.game_stub.PutBattleToken(
            facade_pb2.Attack(game_id=game_id, player_id=player_id, my_token_id=my_token_id,
                              province_from_id=province_from_id,
                              province_to_id=province_to_id))

    def show_someone_reset(self, player_id, game_id=0):
        print("ShowSomeoneReset")
        return self.game_stub.ShowSomeoneReset(facade_pb2.Player(game_id=game_id, player_id=player_id))

    def show_active(self, player_id, game_id=0):
        print("ShowActive")
        return self.game_stub.ShowActive(facade_pb2.Player(game_id=game_id, player_id=player_id))

    def round_count(self, game_id=0):
        print("RoundCountGame")
        return self.game_stub.RoundCount(facade_pb2.Empty(game_id=game_id))

    def whose_move(self, game_id=0):
        print("WhoseMove")
        return self.game_stub.WhoseMove(facade_pb2.Empty(game_id=game_id))

    def show_battle_token(self, player_id, my_token_id, game_id=0):
        print("ShowBattleToken")
        return self.game_stub.ShowBattleToken(game_id=game_id, player_id=player_id, my_token_id=my_token_id)

    def get_all_control_token(self, game_id=0):
        print("GetAllControlToken")
        return self.game_stub.GetAllControlToken(facade_pb2.Empty(game_id=game_id))

    def get_all_battle_token(self, game_id=0):
        print("GetAllBattleToken")
        return self.game_stub.GetAllBattleToken(facade_pb2.Empty(game_id=game_id))

    def use_card(self, player_id, card_id, game_id=0):
        print("UseCard")
        return self.game_stub.UseCard(facade_pb2.Card(game_id=game_id, player_id=player_id, card_id=card_id))

    def unused_card(self, player_id, game_id=0):
        print("UnusedCard")
        return self.game_stub.UnusedCard(facade_pb2.Player(game_id=game_id, player_id=player_id))

    def get_all_my_cards(self, player_id, game_id=0):
        print("GetAllMyCards")
        return self.game_stub.GetAllMyCards(facade_pb2.Player(game_id=game_id, player_id=player_id))

    def do_execution_phase(self, game_id=0):
        print("DoExecutionPhase")
        return self.game_stub.DoExecutionPhase(facade_pb2.Empty(game_id=game_id))

    def get_winner(self, game_id=0):
        print("GetWinner")
        return self.game_stub.GetWinner(facade_pb2.Empty(game_id=game_id))

    def get_free_caste(self, game_id=0):
        print("GetFreeCaste")
        return self.game_stub.GetFreeCaste(facade_pb2.Empty(game_id=game_id))

    def set_caste(self, player_id, caste, game_id=0):
        print("SetCaste")
        return self.game_stub.SetCaste(facade_pb2.Caste(game_id=game_id, player_id=player_id, caste=caste))

    def get_possible_positions_control_token(self, game_id=0):
        print("GetPossiblePositionsControlToken")
        return self.game_stub.GetPossiblePositionsControlToken(facade_pb2.Empty(game_id=game_id))

    def put_control_token(self, player_id, token_id, province_id, game_id=0):
        print("PutControlToken")
        return self.game_stub.PutControlToken(
            facade_pb2.Token(game_id=game_id, player_id=player_id, token_id=token_id, province_id=province_id))


if __name__ == '__main__':
    client = Client()

    # Debug client...
    # cmd - number of command from starter facade (or command name)
    # If you want to break client write -1

    your_id = -1
    cmd = input()
    while cmd != '-1':
        if cmd == '1' or cmd == 'get_unique_id':
            your_id = client.get_unique_id().player_id
            print(f'Your id: {your_id}')
        elif (cmd == '2' or cmd == 'add_player') and your_id != -1:
            key = client.add_player(your_id).key
            print(f'Add player with id {your_id}\nIs ok? {key}')
        elif (cmd == '3' or cmd == "swap_player_readiness_value") and your_id != -1:
            key = client.swap_player_readiness_value(your_id).key
            print(f'Correct? {key}')
        elif cmd == '4' or cmd == "get_free_caste":
            free_caste = client.get_free_caste().caste
            print(f'Free caste: {free_caste}')
        elif (cmd == '5' or cmd == 'set_caste') and your_id != -1:
            your_caste = input("Enter caste: ")
            key = client.set_caste(your_id, your_caste).key
            print(f'Correct? {key}')
        elif cmd == '6' or cmd == "get_possible_positions_control_token":
            list_token = client.get_possible_positions_control_token().position
            print(f'List of possible position control tokens: {list_token}')
        elif (cmd == '7' or cmd == "put_control_token") and your_id != -1:
            your_control_token_id = int(input("Enter control token id: "))
            your_province_id = int(input("Enter province id: "))
            key = client.put_control_token(your_id, your_control_token_id, your_province_id).key
            print(f'Is correct? {key}')
        elif cmd == '8' or cmd == "round_count_starter":
            print(f'Current round is {client.round_count().round}')
        elif cmd == '9' or cmd == "get_all_control_token_starter":
            all_control_tokens = client.get_all_control_token()
            print(f'All control tokens for player with id {your_id}: {all_control_tokens.token}')
        cmd = input()
