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

    def __init__(self, game_ind: int, player_ind: int):
        self.ind = game_ind
        self.my_player_id = player_ind

        self.players = dict()  # id -> Class Player
        self.round = 0
        self.battle_tokens = dict()  # id -> Class BattleToken
        self.control_tokens = dict()  # id -> Class ControlTokens
        self.whose_move = -1  # id player, whose move we are waiting for

    def add_player(self, player_ind: int, name: str):
        self.players[player_ind] = Player(player_ind, name)

    def update_battle_tokens(self, new_battle_tokens):
        for bt in new_battle_tokens:
            if bt.id not in self.battle_tokens:
                self.battle_tokens[bt.id] = BattleToken(bt.id, bt.on_board_first, bt.on_board_second, bt.visible,
                                                        bt.caste, bt.in_reset, bt.in_active, bt.type, bt.power)
            else:
                self.battle_tokens[bt.id].change_all_val(bt.id, bt.on_board_first, bt.on_board_second, bt.visible,
                                                         bt.caste, bt.in_reset, bt.in_active, bt.type, bt.power)

    def update_control_tokens(self, new_control_tokens):
        for ct in new_control_tokens:
            if ct.id not in self.control_tokens:
                self.control_tokens[ct.id] = ControlToken(ct.id, ct.province_id, ct.visible, ct.caste)
            else:
                self.control_tokens[ct.id].change_all_val(ct.id, ct.province_id, ct.visible, ct.caste)

    def update_players(self, new_players):
        for player_ind in new_players:
            if player_ind not in gm.players:
                self.players[player_ind] = Player(ind, "KAM" + str(ind))


if __name__ == '__main__':
    client = Client()

    ind = client.create_new_game_session().game_id
    gm = Game(ind, 0)
    # gm = Game(Pupa)
    players = []
    while not client.should_start_game(gm.ind).key:  # for i in range(3):  # while Starter Facade
        ind = client.get_unique_id(gm.ind).player_id
        client.add_player(ind, gm.ind)
        client.swap_player_readiness_value(ind, gm.ind)
        gm.update_players(client.get_players_ids(gm.ind).int)
        players = list(gm.players.keys())

    print(players)
    for i in players:
        my_caste = client.get_free_caste(gm.ind).caste[0]
        if client.set_caste(i, my_caste, gm.ind):
            caste = Caste(my_caste)
            gm.players[i].set_caste(caste)

    # print(client.round_count(gm.ind).round)
    # tokens = client.get_all_battle_token(gm.ind).token
    # for token in tokens:
    #     print(token.id)

    while client.round_count(gm.ind).round != 1:
        was = False
        for i in range(1000):
            for id_player in players:
                if client.put_control_token(id_player, i, i % 30, gm.ind).key:
                    # print("OK", str(id_player), i)
                    was = True
                    break
            if was:
                break
    # print(client.round_count(gm.ind).round)

    while True:
        gm.update_control_tokens(client.get_all_control_token(gm.ind).token)
        gm.update_battle_tokens(client.get_all_battle_token(gm.ind).token)
        gm.round = client.round_count(gm.ind).round
        gm.whose_move = client.whose_move(gm.ind).player_id
        break

    for q in range(5):
        print(client.round_count(gm.ind).round, client.get_phase(gm.ind).round)
        for i in range(1):
            for id_player in players:
                client.unused_card(id_player, gm.ind)
        print(client.round_count(gm.ind).round, client.get_phase(gm.ind).round)

        while client.get_phase(gm.ind).round == 2:
            f = random.randint(0, 29)
            t = random.randint(0, 29)
            was = False
            for id_player in players:
                active = []
                for token in gm.battle_tokens.values():
                    if token.caste == gm.players[id_player].caste and token.in_active:
                        active.append(token)
                        # print(token.caste, token.ind, id_player, gm.players[id_player].caste)
                # print(active)
                for token in active:
                    # print(token.ind, token.caste, gm.players[id_player].caste, token.prov_from, token.prov_to)
                    ind = token.ind
                    if client.put_battle_token(id_player, ind, f, t, gm.ind).key:
                        print("OK", id_player, ind)
                        was = True
                        break
                if was:
                    break
            # gm.update_battle_tokens(client.get_all_battle_token(gm.ind).token)
        client.do_execution_phase(gm.ind)
        # gm.update_battle_tokens(client.get_all_battle_token(gm.ind).token)
    print(client.get_winner(gm.ind).player)
