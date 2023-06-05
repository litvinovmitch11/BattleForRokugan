from main_client import Client
import time


class ViewModel:
    def __init__(self, game_id, player_id, client_object: Client):
        self.game_id = game_id
        self.player_id = player_id
        self.client = client_object

    def update(self):
        pass


class Register:
    def __init__(self, *args: ViewModel):
        self.list_models = list(args)

    def add(self, model: ViewModel):
        self.list_models.append(model)

    def run(self, delay):
        while True:
            for model in self.list_models:
                model.update()
            time.sleep(delay)


class ViewModelSystem(ViewModel):
    def __init__(self, game_id, player_id, client_object: Client):
        super().__init__(game_id, player_id, client_object)
        self.round = None
        self.players = None
        self.players_count = None
        self.whose_move = None

    def update(self):
        self.round = self.client.round_count(game_id=self.game_id).round
        self.players = self.client.get_players(game_id=self.game_id).name
        self.players_count = len(self.players)
        self.whose_move = self.client.whose_move(game_id=self.game_id).player_id


class ViewModelHand(ViewModel):
    def __init__(self, game_id, player_id, client_object: Client):
        super().__init__(game_id, player_id, client_object)
        self.active = None

    def update(self):
        self.active = self.client.show_active(player_id=self.player_id, game_id=self.game_id).token


class ViewModelBoard(ViewModel):
    def __init__(self, game_id, player_id, client_object: Client):
        super().__init__(game_id, player_id, client_object)
        self.control_tokens = None
        self.battle_tokens = None

    def update(self):
        self.control_tokens = self.client.get_all_control_token(game_id=self.game_id).token
        self.battle_tokens = self.client.get_all_battle_token(game_id=self.game_id).token
