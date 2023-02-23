import random
import enum

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


class Caste(enum.Enum):
    crab = "crab"
    crane = "crane"
    lion = "lion"
    scorpion = "scorpion"
    unicorn = "unicorn"
    dragon = "dragon"
    phoenix = "phoenix"


class TokenType(enum.Enum):
    army = "army"
    fleet = "fleet"
    shinobi = "shinobi"
    blessing = "blessing"
    diplomacy = "diplomacy"
    pogrom = "pogrom"
    empty = "empty"


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

    def get_free_caste(self):
        free_castes = []
        for watching_caste in Caste:
            used_caste = False
            for player in self.players:
                if player.caste == watching_caste:
                    used_caste = True
            if not used_caste:
                free_castes.append(watching_caste)
        return free_castes


class BattleToken:  # and here initialization

    def __init__(self, caste: Caste, power: int, token_type: TokenType):
        self.caste = caste
        self.power = power
        self.type = token_type
        self.on_board = False
        self.in_reset = False
        self.in_active = False
        self.visible = False

    def put_on_board(self, my_board: Board, ind_start: int, ind_finish: int):
        self.on_board = True
        if ind_start == ind_finish:
            for province in my_board.all_provinces:
                if province.ind == ind_start:
                    province.items_inside.append(self)
        else:
            my_board.all_provinces[ind_start].battle_outside.append(ind_start)
            my_board.all_provinces[ind_finish].battle_inside.append(ind_finish)
            if my_board.can_put_army_token[ind_start][ind_finish] == 0:
                return False
            my_board.can_put_army_token[ind_start][ind_finish] = 0

    def make_visible(self):
        self.visible = True


class ControlToken:  # and here initialization
    def __init__(self, caste: Caste, power: int):
        self.visible = False
        self.on_board = False
        self.power = power
        self.caste = caste

    def put_on_board(self, my_board: Board, ind: int):
        self.on_board = True
        for item in my_board.all_provinces[ind].items_inside:
            if type(item) == ControlToken and item.caste == self.caste:
                self.visible = True

    def make_visible(self):
        self.visible = True


class Player:
    def __init__(self, id_player: int, my_board: Board):
        self.caste = None
        self.battle_token = []
        self.active = []
        self.id_player = id_player
        self.my_board = my_board

    def put_caste(self, caste_name):
        self.caste = caste_name

    def take_battle_token(self):
        power_army = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
        for power in power_army:
            self.battle_token.append(BattleToken(self.caste, power, TokenType.army))
        for power in [1, 1, 2]:
            self.battle_token.append(BattleToken(self.caste, power, TokenType.fleet))
        for power in [1, 2]:
            self.battle_token.append(BattleToken(self.caste, power, TokenType.shinobi))
        for power in [2, 2]:
            self.battle_token.append(BattleToken(self.caste, power, TokenType.blessing))
        self.battle_token.append(BattleToken(self.caste, 0, TokenType.diplomacy))
        self.battle_token.append(BattleToken(self.caste, 0, TokenType.pogrom))
        self.battle_token.append(BattleToken(self.caste, 0, TokenType.empty))
        random.shuffle(self.battle_token)

    def make_active(self):
        for token in self.active:
            if token.type == TokenType.empty and not token.in_active:
                token.in_active = True
                self.active.append(token)
                break
        while len(self.active) < 6:
            for token in self.battle_token:
                if not token.in_active and not token.on_board and not token.in_reset:
                    self.active.append(token)
                    token.in_active = True
                    break
        random.shuffle(self.battle_token)

    def put_battle_token_on_board(self, battle_token: BattleToken, ind_start: int, ind_finish: int):
        battle_token.put_on_board(self.my_board, ind_start, ind_finish)

    def put_control_token_on_board(self, control_token: ControlToken, ind: int):
        control_token.put_on_board(self.my_board, ind)


class Province:

    def __init__(self, ind: int):
        self.capital = False
        self.coastal = False  # прибержная
        self.mainland = False  # материковая
        self.caste = None
        self.shadow = False
        self.owning_caste = None
        self.ind = ind
        self.items_inside = []

        self.battle_inside = []
        self.battle_outside = []
        self.control_token = []

        self.glory_points = 0
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
    board.add_player(1)
    board.add_player(2)
