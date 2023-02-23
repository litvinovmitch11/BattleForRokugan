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


class BattleToken:  # should be incomplete type
    pass


class ControlToken:
    pass


class Board:

    def __init__(self):
        self.round = 0
        self.players = []
        self.all_provinces = []
        self.putted_battle_tokens = []  # should be inside province
        self.putted_control_tokens = []  # should be inside province
        self.can_put_army_token = have_land_way
        for i in range(30):
            self.all_provinces.append(Province(i))

    def put_battle_token(self, battle_token: BattleToken, ind_start: int, ind_finish: int):
        # incomplete type for this line
        self.putted_battle_tokens.append(battle_token)
        if ind_start == ind_finish:
            for province in self.all_provinces:
                if province.ind == ind_start:
                    province.items_inside.append(battle_token)
        else:
            if self.can_put_army_token[ind_start][ind_finish] == 0:
                return False
            self.can_put_army_token[ind_start][ind_finish] = 0

    def put_control_token(self, control_token: ControlToken, ind: int):
        # incomplete type for this line
        self.putted_control_tokens.append(control_token)
        for item in self.all_provinces[ind].items_inside:
            if type(item) == ControlToken and item.caste == control_token.caste:
                control_token.visible = True

    def add_player(self, id_player: int):
        self.players.append(Player(id_player))


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
        my_board.put_battle_token(self, ind_start, ind_finish)

    def make_visible(self):
        self.visible = True


class ControlToken:  # and here initialization
    def __init__(self, caste: Caste):
        self.visible = False
        self.on_board = False
        self.caste = caste

    def put_on_board(self, my_board: Board, ind: int):
        self.on_board = True
        my_board.put_control_token(self, ind)


class Player:
    def __init__(self, id_player: int):
        self.caste = None
        self.battle_token = []
        self.active = []
        self.id_player = id_player

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
