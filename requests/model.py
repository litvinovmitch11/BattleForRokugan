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


class BattleToken:
    def __init__(self, caste: Caste, power: int, token_type: TokenType):
        self.caste = caste
        self.power = power
        self.type = token_type
        self.on_board = False
        self.in_reset = False
        self.in_active = False
        self.visible = token_type == TokenType.blessing

    def make_visible(self):
        self.visible = True


class ControlToken:
    def __init__(self, caste: Caste, power: int):
        self.visible = False
        self.on_board = False
        self.power = power
        self.caste = caste

    def make_visible(self):
        self.visible = True


class Player:
    def __init__(self, player_id: int):
        self.caste = None
        self.battle_tokens = []
        self.control_tokens = []
        self.active = []
        self.player_id = player_id

    def set_clan(self, my_caste: Caste) -> bool:
        self.caste = my_caste
        self.take_battle_token()
        self.take_control_token()
        return True

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
        for token in self.battle_tokens:
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

    def get_reset(self) -> list[BattleToken]:
        ans = []
        for my_battle_token in self.battle_tokens:
            if my_battle_token.in_reset:
                ans.append(my_battle_token)
        return ans

    def get_active(self) -> list[BattleToken]:
        return self.active


class GameState:

    def __init__(self):
        self.id_move = 0  # 1st player start all time?
        self.move_queue = []  # player_ids
        self.round = 0
        self.move_to_next_round = 100

    def correct_move(self, player_id: int) -> bool:
        return self.move_queue[self.id_move % len(self.move_queue)] == player_id

    def make_move(self) -> bool:  # !!! SHIT !!!
        # return true, if next round
        self.move_to_next_round -= 1
        self.id_move += 1
        if self.move_to_next_round == 0:
            self.round += 1
        return True

    def add_player(self, my_player: Player) -> bool:
        if len(self.move_queue) <= 4:
            self.move_queue.append(my_player)
            return True
        self.move_to_next_round = len(self.move_queue)
        return False


# нужен ли порядок

# Новый ход

# раунд и чей ход.

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

    def set_control_token(self, my_control_token: ControlToken):
        self.control_tokens.append(my_control_token)

    def set_battle_token(self, my_battle_token: BattleToken, inside: bool):
        if inside:
            self.battle_inside.append(my_battle_token)
        else:
            self.battle_outside.append(my_battle_token)


class Board:
    def __init__(self):
        self.players = dict()  # id -> Class Player
        self.state = GameState()

        self.all_provinces = []
        self.can_put_army_token = have_land_way
        self.move_queue = []  # player_id whose move
        for i in range(30):
            self.all_provinces.append(Province(i))

    def add_player(self, my_player: Player):
        self.players[my_player.player_id] = my_player
        self.state.add_player(my_player)

    def get_free_caste(self) -> list[Caste]:
        free_castes = []
        for watching_caste in Caste:
            used_caste = False
            for player in self.players.values():
                if player.caste == watching_caste:
                    used_caste = True
            if not used_caste:
                free_castes.append(watching_caste)
        return free_castes

    def make_all_battle_token_visible(self):
        for player in self.players.values():
            for my_battle_token in player.battle_tokens:
                my_battle_token.make_visible()

    def get_all_provinces_without_control_token(self) -> list[int]:
        ans = []
        for province in self.all_provinces:
            if province.owning_caste is None:
                ans.append(province.ind)
        return ans

    def get_possible_position_to_put_battle_token(self) -> list[tuple[int, int]]:  # (from, to)
        ans = []
        for i in range(len(self.can_put_army_token)):
            for j in range(len(self.can_put_army_token[i])):
                if self.can_put_army_token[i][j] == 1:
                    ans.append((i, j))
        return ans

    def get_possible_position_to_put_control_token(self) -> list[int]:
        ans = []
        for province in self.all_provinces:
            if len(province.control_tokens) == 0:
                ans.append(province.ind)
        return ans

    def put_on_board_battle_token(self, player_id: int, my_battle_token: BattleToken, ind_start: int,
                                  ind_finish: int) -> bool:
        if self.can_put_army_token[ind_start][ind_finish] == 0:
            return False
        # тут ещё надо удалить из актива и поставить на доску
        my_battle_token.on_board = True
        if ind_start == ind_finish:
            self.all_provinces[ind_start].protection_battle_token.append(my_battle_token)
        else:
            self.all_provinces[ind_start].battle_outside.append(my_battle_token)
            self.all_provinces[ind_finish].battle_inside.append(my_battle_token)
            self.can_put_army_token[ind_start][ind_finish] = 0
        return True

    def put_on_board_control_token(self, player_id: int, my_control_token: ControlToken, province_id: int) -> bool:
        my_control_token.on_board = True
        for item in self.all_provinces[province_id].control_tokens:
            if item.caste == my_control_token.caste:
                my_control_token.visible = True
        return True

    def set_control_token_to_capital(self, my_caste: Caste, my_control_token: ControlToken):
        for province in self.all_provinces:
            if province.capital and province.caste == my_caste:
                province.control_tokens.append(my_control_token)


if __name__ == "__main__":
    player1 = Player(1)
    board = Board()
    board.add_player(player1)
    player1.set_clan(Caste.crab)
    player1.make_active()
    for battle_token in player1.active:
        print(battle_token.type, battle_token.power)
    print()
    print(*board.get_free_caste())
