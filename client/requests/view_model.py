from facade_client import Client
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
        self.phase = None
        self.free_casts = None

    def update(self):
        self.round = self.client.get_round(game_id=self.game_id).round
        self.players = self.client.get_players(game_id=self.game_id).name
        self.players_count = len(self.players)
        self.whose_move = self.client.whose_move(game_id=self.game_id).player_id
        self.phase = self.client.get_phase(game_id=self.game_id).round
        self.free_casts = self.client.get_free_caste(game_id=self.game_id).caste

    def swap_player_readiness_value(self):
        return self.client.swap_player_readiness_value(player_id=self.player_id, game_id=self.game_id).key

    def set_caste(self, caste):
        return self.client.set_caste(player_id=self.player_id, game_id=self.game_id, caste=caste).key

    def get_winner(self):
        return self.client.get_winner(game_id=self.game_id).player


class ViewModelHand(ViewModel):
    def __init__(self, game_id, player_id, client_object: Client):
        super().__init__(game_id, player_id, client_object)
        self.active = None
        self.cards = None

    def update(self):
        self.active = self.client.get_player_active(player_id=self.player_id, game_id=self.game_id).token
        self.cards = self.client.get_all_cards(game_id=self.game_id).card

    def use_card(self, card_id, values):
        return self.client.use_card(game_id=self.game_id, player_id=self.player_id, card_id=card_id, values=values).key

    def unused_card(self):
        return self.client.unused_card(game_id=self.game_id, player_id=self.player_id).key

    def get_someone_reset(self, someone_player_id):
        return self.client.get_someone_reset(player_id=someone_player_id, game_id=self.game_id).token

    def put_control_token(self, province_id):
        return self.client.put_control_token(player_id=self.player_id, game_id=self.game_id,
                                             province_id=province_id).key

    def put_battle_token(self, my_token_id, province_from_id, province_to_id):
        return self.client.put_battle_token(player_id=self.player_id, game_id=self.game_id, my_token_id=my_token_id,
                                            province_from_id=province_from_id, province_to_id=province_to_id).key


class ViewModelBoard(ViewModel):
    def __init__(self, game_id, player_id, client_object: Client):
        super().__init__(game_id, player_id, client_object)
        self.control_tokens = None
        self.battle_tokens = None
        self.special_tokens = None
        self.possible_position_battle_token = None
        self.possible_position_control_token = None

    def update(self):
        self.control_tokens = self.client.get_all_control_token(game_id=self.game_id).token
        self.battle_tokens = self.client.get_all_battle_token(game_id=self.game_id).token
        self.special_tokens = self.client.get_all_special_tokens(game_id=self.game_id).token
        self.possible_position_battle_token = self.client.get_possible_positions_battle_token(game_id=self.game_id).line
        self.possible_position_control_token = self.client.get_possible_positions_control_token(
            game_id=self.game_id).position
