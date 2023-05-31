from all_include import *
from main_client import Client


class BattleToken:

    def __init__(self, ind: int, prov_from: int, prov_to: int, visible: bool, caste: Caste):
        self.ind = ind
        self.prov_from = prov_from
        self.prov_to = prov_to
        self.visible = visible
        self.caste = Caste

    def change_all_val(self, ind: int, prov_from: int, prov_to: int, visible: bool, caste: Caste):
        self.ind = ind
        self.prov_from = prov_from
        self.prov_to = prov_to
        self.visible = visible
        self.caste = Caste


class ControlToken:

    def __init__(self, ind: int, prov: int, visible: bool, caste: Caste):
        self.ind = ind
        self.prov = prov
        self.visible = visible
        self.caste = Caste

    def change_all_val(self, ind: int, prov: int, visible: bool, caste: Caste):
        self.ind = ind
        self.prov = prov
        self.visible = visible
        self.caste = Caste


class Player:  # info, for client

    def __init__(self, ind: int, name: str):
        self.caste = Caste.none
        self.battle_tokens = dict()  # id -> Class BattleToken
        self.control_tokens = dict()  # id -> Class ControlToken
        self.ind = ind
        self.name = name


class Game:

    def __init__(self, ind: int):
        self.ind = ind
        self.players = dict()  # id -> name of players
        self.round = 0
        self.battle_tokens = dict()  # id -> Class BattleToken
        self.control_tokens = dict()  # id -> Class ControlTokens

    def add_player(self, ind: int, name: str):
        self.players[ind] = Player(ind, name)


if __name__ == '__main__':
    client = Client()

    ind = client.create_new_game_session().game_id
    gm = Game(0)
    # gm = Game(Pupa)
    # players = []
    for i in range(2):  # while Starter Facade
        ind = client.get_unique_id(gm.ind).player_id
        if client.add_player(ind, gm.ind).key:
            print("LOL\n")
            gm.add_player(ind, "Kam" + str(ind))
        client.swap_player_readiness_value(ind, gm.ind)
    players = client.get_players_ids(gm.ind).int
    print(players, client.should_start_game(gm.ind).key)
    for i in players:
        print(client.get_free_caste().caste)
        client.set_caste(i, client.get_free_caste().caste[0], gm.ind)
    print(client.get_free_caste().caste[0])

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

