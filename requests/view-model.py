from all_include import *
from main_client import Client


class BattleToken:

    def __init__(self, bt_ind: int, prov_from: int, prov_to: int, visible: bool, caste: Caste):
        self.ind = bt_ind
        self.prov_from = prov_from
        self.prov_to = prov_to
        self.visible = visible
        self.caste = Caste

    def change_all_val(self, bt_ind: int, prov_from: int, prov_to: int, visible: bool, caste: Caste):
        self.ind = bt_ind
        self.prov_from = prov_from
        self.prov_to = prov_to
        self.visible = visible
        self.caste = Caste


class ControlToken:

    def __init__(self, t_ind: int, prov: int, visible: bool, caste: Caste):
        self.ind = t_ind
        self.prov = prov
        self.visible = visible
        self.caste = Caste

    def change_all_val(self, t_ind: int, prov: int, visible: bool, caste: Caste):
        self.ind = t_ind
        self.prov = prov
        self.visible = visible
        self.caste = Caste


class Player:  # info, for client

    def __init__(self, player_ind: int,  name: str):
        self.caste = Caste.none
        self.battle_tokens = dict()  # id -> Class BattleToken
        self.control_tokens = dict()  # id -> Class ControlToken
        self.my_ind = player_ind
        self.name = name


class Game:

    def __init__(self, game_ind: int):
        self.ind = game_ind
        self.players = dict()  # id -> Class Player
        self.round = 0
        self.battle_tokens = dict()  # id -> Class BattleToken
        self.control_tokens = dict()  # id -> Class ControlTokens

    def add_player(self, player_ind: int, name: str):
        self.players[player_ind] = Player(player_ind, name)


if __name__ == '__main__':
    client = Client()

    ind = client.create_new_game_session().game_id
    gm = Game(ind)
    # gm = Game(Pupa)
    players = []
    while not client.should_start_game(gm.ind).key:  # for i in range(3):  # while Starter Facade
        ind = client.get_unique_id(gm.ind).player_id
        if client.add_player(ind, gm.ind).key:
            gm.add_player(ind, "Kam" + str(ind))

        client.swap_player_readiness_value(ind, gm.ind)
        players = client.get_players_ids(gm.ind).int
    print(players)
    for i in players:
        print(client.get_free_caste(gm.ind).caste)
        client.set_caste(i, client.get_free_caste(gm.ind).caste[0], gm.ind)
        tokens = client.get_all_control_token(gm.ind).token
        for token in tokens:
            print(token.id, token.caste)
    print(client.round_count(gm.ind).round)
    while client.round_count(gm.ind).round != 1:
        print(client.round_count(gm.ind).round)
        was = False
        for i in range(1000):
            for id_player in players:
                if client.put_control_token(id_player, i, i % 30, gm.ind):
                    print("OK", str(id_player), i)
                    was = True
                    break
            if was:
                break
    print(client.round_count().round)
    while True:
        control_tokens = []  # client.get_all_control_token()
        for token in control_tokens:
            if token.id not in gm.control_tokens:
                gm.control_tokens[token.id] = ControlToken(token.id, token.province_id, token.visible, token.caste)
            else:
                gm.control_tokens[token.id].change_all_val(token.id, token.province_id, token.visible, token.caste)
        battle_tokens = []  # client.get_all_battle_token()
        for token in battle_tokens:
            if token.id not in gm.control_tokens:
                gm.battle_tokens[token.id] = ControlToken(token.id, token.province_id, token.visible, token.caste)
            else:
                gm.battle_tokens[token.id].change_all_val(token.id, token.province_id, token.visible, token.caste)
        # gm.round = client.round_count().round

        break
