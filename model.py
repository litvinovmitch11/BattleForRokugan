import random
from all_include import *

have_land_way = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]


class Board:
    def __init__(self):
        self.round = 0
        self.players = []
        self.all_provinces = []
        self.can_put_army_token = have_land_way
        for i in range(30):
            self.all_provinces.append(Province(i))

    def add_player(self, id_player: int):
        self.players.append(Player(id_player, self))

    def get_free_caste(self) -> list[Caste]:
        free_castes = []
        for watching_caste in Caste:
            used_caste = False
            for player in self.players:
                if player.caste == watching_caste:
                    used_caste = True
            if not used_caste:
                free_castes.append(watching_caste)
        return free_castes

    def make_all_battle_token_visible(self):
        for player in self.players:
            for battle_token in player.battle_tokens:
                battle_token.make_visible()


class BattleToken:
    def __init__(self, caste: Caste, power: int, token_type: TokenType):
        self.caste = caste
        self.power = power
        self.type = token_type
        self.on_board = False
        self.in_reset = False
        self.in_active = False
        self.visible = token_type == TokenType.blessing

    def put_on_board(self, my_board: Board, ind_start: int, ind_finish: int):
        self.on_board = True
        if ind_start == ind_finish:
            my_board.all_provinces[ind_start].protection_battle_token.append(self)
        else:
            my_board.all_provinces[ind_start].battle_outside.append(ind_start)
            my_board.all_provinces[ind_finish].battle_inside.append(ind_finish)
            if my_board.can_put_army_token[ind_start][ind_finish] == 0:
                return False
            my_board.can_put_army_token[ind_start][ind_finish] = 0

    def make_visible(self):
        self.visible = True


class ControlToken:
    def __init__(self, caste: Caste, power: int):
        self.visible = False
        self.on_board = False
        self.power = power
        self.caste = caste

    def put_on_board(self, my_board: Board, ind: int):
        self.on_board = True
        for item in my_board.all_provinces[ind].control_tokens:
            if item.caste == self.caste:
                self.visible = True

    def make_visible(self):
        self.visible = True


class Player:
    def __init__(self, id_player: int, my_board: Board):
        self.caste = None
        self.battle_tokens = []
        self.control_tokens = []
        self.active = []
        self.id_player = id_player
        self.my_board = my_board

    def choose_caste(self, caste: Caste):
        self.caste = caste
        self.take_battle_token()
        self.take_control_token()
        for province in self.my_board.all_provinces:
            if province.caste == caste and province.capital:
                province.control_tokens.append(self.control_tokens[0])
                self.control_tokens[0].on_board = True
                break

    def take_battle_token(self):
        power_army = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
        for power in power_army:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.army))
        for power in [1, 1, 2]:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.fleet))
        for power in [1, 2]:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.shinobi))
        for power in [2, 2]:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.blessing))
        self.battle_tokens.append(BattleToken(self.caste, 0, TokenType.diplomacy))
        self.battle_tokens.append(BattleToken(self.caste, 0, TokenType.pogrom))
        self.battle_tokens.append(BattleToken(self.caste, 0, TokenType.empty))
        random.shuffle(self.battle_tokens)

    def take_control_token(self):
        power = 2 if self.caste == Caste.crab else 1
        for i in range(30):
            self.control_tokens.append(ControlToken(self.caste, power))

    def make_active(self):
        for token in self.active:
            if token.type == TokenType.empty and not token.in_active:
                token.in_active = True
                self.active.append(token)
                break
        while len(self.active) < 6:
            for token in self.battle_tokens:
                if not token.in_active and not token.on_board and not token.in_reset:
                    self.active.append(token)
                    token.in_active = True
                    break
        random.shuffle(self.battle_tokens)

    def put_battle_token_on_board(self, battle_token: BattleToken, ind_start: int, ind_finish: int):
        battle_token.put_on_board(self.my_board, ind_start, ind_finish)

    def put_control_token_on_board(self, control_token: ControlToken, ind: int):
        control_token.put_on_board(self.my_board, ind)


class Province:

    def __init__(self, ind: int):
        self.capital = False
        self.coastal = False  # прибержная
        self.mainland = False  # материковая
        self.shadow = False
        self.caste = None
        self.owning_caste = None

        self.battle_inside = []
        self.battle_outside = []
        self.protection_battle_token = []
        self.control_tokens = []

        self.ind = ind
        self.glory_points = 0

        self.set_correct_field_value(ind)

    def set_correct_field_value(self, ind):
        if ind in [27, 25, 23, 18, 16, 14, 5]:
            self.capital = True
        if ind in [3, 4]:
            self.shadow = True
        if ind in [0, 1, 2, 3, 5, 9, 11, 12, 13, 14, 15, 29]:
            self.coastal = True
        else:
            self.mainland = True
        if ind in [5, 6, 7, 8]:
            self.caste = Caste.crab
        if ind in [12, 13, 14]:
            self.caste = Caste.crane
        if ind in [15, 16, 17]:
            self.caste = Caste.lion
        if ind in [18, 19, 20]:
            self.caste = Caste.scorpion
        if ind in [21, 22, 23]:
            self.caste = Caste.unicorn
        if ind in [24, 25, 26]:
            self.caste = Caste.dragon
        if ind in [27, 28, 29]:
            self.caste = Caste.phoenix
        if ind in [0, 1, 7, 20, 21, 24, 29]:
            self.glory_points = 1
        elif ind in [2, 5, 6, 11, 13, 14, 15, 16, 17, 18, 23, 25, 27, 28]:
            self.glory_points = 2
        elif not self.shadow:
            self.glory_points = 3


if __name__ == "__main__":
    board = Board()
