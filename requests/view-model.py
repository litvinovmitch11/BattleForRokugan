from all_include import *
from main_client import Client
import random


class BattleToken:

    def __init__(self, bt_ind: int, prov_from: int, prov_to: int, visible: bool, new_caste: Caste, in_reset: bool,
                 in_active: bool, my_type: int, power: int):
        self.ind = bt_ind
        self.prov_from = prov_from
        self.prov_to = prov_to
        self.visible = visible
        self.caste = Caste(new_caste)
        self.in_reset = in_reset
        self.in_active = in_active
        self.type = TokenType(my_type)
        self.power = power

    def change_all_val(self, bt_ind: int, prov_from: int, prov_to: int, visible: bool, new_caste: Caste, in_reset: bool,
                       in_active: bool, my_type: int, power: int):
        self.ind = bt_ind
        self.prov_from = prov_from
        self.prov_to = prov_to
        self.visible = visible
        self.caste = Caste(new_caste)
        self.in_reset = in_reset
        self.in_active = in_active
        self.type = TokenType(my_type)
        self.power = power


class ControlToken:

    def __init__(self, t_ind: int, prov: int, visible: bool, new_caste: Caste):
        self.ind = t_ind
        self.prov = prov
        self.visible = visible
        self.caste = Caste(new_caste)

    def change_all_val(self, t_ind: int, prov: int, visible: bool, new_caste: Caste):
        self.ind = t_ind
        self.prov = prov
        self.visible = visible
        self.caste = Caste(new_caste)


class Player:  # info, for client

    def __init__(self, player_ind: int, name: str):
        self.caste = Caste.none
        self.battle_tokens = dict()  # id -> Class BattleToken
        self.control_tokens = dict()  # id -> Class ControlToken
        self.my_ind = player_ind
        self.name = name

    def set_caste(self, new_caste: Caste):
        self.caste = new_caste


class Game:

    def __init__(self, game_ind: int):
        self.ind = game_ind
        self.players = dict()  # id -> Class Player
        self.round = 0
        self.battle_tokens = dict()  # id -> Class BattleToken
        self.control_tokens = dict()  # id -> Class ControlTokens

        self.whose_move = -1  # WARNING

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
        my_caste = client.get_free_caste(gm.ind).caste[0]
        if client.set_caste(i, my_caste, gm.ind):
            caste = Caste(my_caste)
            gm.players[i].set_caste(caste)

    print(client.round_count(gm.ind).round)
    tokens = client.get_all_battle_token(gm.ind).token
    for token in tokens:
        print(token.id)

    while client.round_count(gm.ind).round != 1:
        print(client.round_count(gm.ind).round)
        was = False
        for i in range(1000):
            for id_player in players:
                if client.put_control_token(id_player, i, i % 30, gm.ind).key:
                    print("OK", str(id_player), i)
                    was = True
                    break
            if was:
                break
    print(client.round_count(gm.ind).round)

    while True:
        control_tokens = client.get_all_control_token(gm.ind).token
        for token in control_tokens:
            if token.id not in gm.control_tokens:
                gm.control_tokens[token.id] = ControlToken(token.id, token.province_id, token.visible, token.caste)
            else:
                gm.control_tokens[token.id].change_all_val(token.id, token.province_id, token.visible, token.caste)
        battle_tokens = client.get_all_battle_token(gm.ind).token
        for token in battle_tokens:
            if token.id not in gm.battle_tokens:
                gm.battle_tokens[token.id] = BattleToken(token.id, token.on_board_first, token.on_board_second,
                                                         token.visible, token.caste, token.in_reset, token.in_active,
                                                         token.type, token.power)
            else:
                gm.battle_tokens[token.id].change_all_val(token.id, token.on_board_first, token.on_board_second,
                                                          token.visible, token.caste, token.in_reset, token.in_active,
                                                          token.type, token.power)
        gm.round = client.round_count(gm.ind).round
        print(gm.round)
        break

    for q in range(5):
        print(client.round_count().round)
        for i in range(10):
            for id_player in players:
                client.unused_card(id_player, gm.ind)
        while client.get_phase(gm.ind).round == 2:
            f = random.randint(0, 29)
            t = random.randint(0, 29)
            was = False
            for id_player in players:
                active = []
                # for token in gm.battle_tokens:
                #     if token.caste == gm.players[id_player].caste:
