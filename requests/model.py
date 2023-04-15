import random
from all_include import *

token_id = 0
have_land_way = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


class BattleToken:
    def __init__(self, caste: Caste, power: int, token_type: TokenType, ind: int):
        self.caste = caste
        self.power = power
        self.type = token_type
        self.on_board = (-1, -1)
        self.in_reset = False
        self.in_active = False
        self.visible = token_type == TokenType.blessing
        self.id = ind

    def make_visible(self):
        self.visible = True


class ControlToken:
    def __init__(self, caste: Caste, power: int, ind: int):
        self.visible = False
        self.province_id = -1
        self.power = power
        self.caste = caste
        self.id = ind

    def make_visible(self):
        self.visible = True


class Player:
    def __init__(self, player_id: int):
        self.caste = None
        self.battle_tokens = []
        self.control_tokens = []
        self.active = []
        self.player_id = player_id
        self.ready_to_play = False

    def set_clan(self, my_caste: Caste) -> bool:
        if self.caste is not None:
            return False
        self.caste = my_caste
        self.take_battle_token()
        self.take_control_token()
        return True

    def take_battle_token(self):
        global token_id
        power_army = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]
        for power in power_army:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.army, token_id))
            token_id += 1
        for power in [1, 1, 2]:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.fleet, token_id))
            token_id += 1
        for power in [1, 2]:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.shinobi, token_id))
            token_id += 1
        for power in [2, 2]:
            self.battle_tokens.append(BattleToken(self.caste, power, TokenType.blessing, token_id))
            token_id += 1
        self.battle_tokens.append(BattleToken(self.caste, 0, TokenType.diplomacy, token_id))
        self.battle_tokens.append(BattleToken(self.caste, 0, TokenType.pogrom, token_id + 1))
        self.battle_tokens.append(BattleToken(self.caste, 0, TokenType.empty, token_id + 2))
        token_id += 3
        random.shuffle(self.battle_tokens)

    def take_control_token(self):
        global token_id
        power = 2 if self.caste == Caste.crab else 1
        for i in range(30):
            self.control_tokens.append(ControlToken(self.caste, power, token_id))
            token_id += 1

    def make_active(self):
        for token in self.battle_tokens:
            if token.type == TokenType.empty and not token.in_active:
                token.in_active = True
                self.active.append(token)
                break
        while len(self.active) < 6:
            for token in self.battle_tokens:
                if not token.in_active and token.on_board == (-1, -1) and not token.in_reset:
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
        self.round = -1  # -1 -> adding player. 0 -> putting control_tokens/choose caste 1-5 -> round of game
        self.move_to_next_round = 0
        self.phase = -1  # in range [1, 3]
        self.cnt_ready = 0

    def this_player_move(self, player_id: int) -> bool:
        return self.move_queue[self.id_move] == player_id

    def make_move(self) -> bool:
        self.move_to_next_round -= 1
        self.id_move = (self.id_move + 1) % len(self.move_queue)
        if self.move_to_next_round == 0:
            if self.round == 0:
                # use card instead random in future
                self.id_move = random.randrange(len(self.move_queue))
                self.phase = 1
                self.round = 1
            else:
                if self.phase == 1:
                    # Make active!
                    self.phase = 2
                    self.move_to_next_round = len(self.move_queue) * 5
                else:
                    # !!! do execution phase. IMPORTANT !!!
                    self.phase = 1
                    self.round += 1
                    self.move_to_next_round = len(self.move_queue)
        return True

    def add_player(self, my_player: Player) -> bool:
        if len(self.move_queue) <= 4 and self.round == -1:
            self.move_queue.append(my_player.player_id)
            return True
        return False


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

        self.control_tokens = dict()  # id -> Class ControlToken
        self.battle_tokens = dict()  # id -> Class BattleToken

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

    def set_caste_to_player(self, player_id: int, my_caste: Caste) -> bool:
        if not self.players[player_id].set_clan(my_caste):
            return False
        for control_token in self.players[player_id].control_tokens:
            self.control_tokens[control_token.id] = control_token
        for battle_token in self.players[player_id].battle_tokens:
            self.battle_tokens[battle_token.id] = battle_token
        return True

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

    def get_possible_position_to_put_battle_token(self) -> list[list[int]]:  # (from, to)
        return self.can_put_army_token

    def get_possible_position_to_put_control_token(self) -> list[int]:
        ans = []
        for province in self.all_provinces:
            if len(province.control_tokens) == 0:
                ans.append(province.ind)
        return ans

    def put_on_board_battle_token(self, player_id: int, battle_token_id: int, ind_start: int,
                                  ind_finish: int) -> bool:
        if self.can_put_army_token[ind_start][ind_finish] == 0:
            return False
        my_battle_token = self.battle_tokens[battle_token_id]

        self.players[player_id].active.remove(my_battle_token)
        my_battle_token.on_board = (ind_start, ind_finish)
        my_battle_token.in_active = False

        if ind_start == ind_finish:
            self.all_provinces[ind_start].protection_battle_token.append(my_battle_token)
        else:
            self.all_provinces[ind_start].battle_outside.append(my_battle_token)
            self.all_provinces[ind_finish].battle_inside.append(my_battle_token)
            self.can_put_army_token[ind_start][ind_finish] = 0
        return True

    def put_on_board_control_token(self, player_id: int, control_token_id: int, province_id: int) -> bool:
        if control_token_id not in self.control_tokens.keys():
            return False
        my_control_token = self.control_tokens[control_token_id]
        if self.players[player_id].caste != my_control_token.caste:
            return False
        for item in self.all_provinces[province_id].control_tokens:
            if item.caste == my_control_token.caste:
                my_control_token.visible = True
            else:
                my_control_token.visible = False
                return False
        self.all_provinces[province_id].control_tokens.append(my_control_token)
        my_control_token.province_id = province_id
        return True

    def set_control_token_to_capital(self, my_caste: Caste, my_control_token: ControlToken):
        for province in self.all_provinces:
            if province.capital and province.caste == my_caste:
                province.control_tokens.append(my_control_token)

    def swap_player_readiness(self, player_id: int) -> bool:
        if not self.players[player_id].ready_to_play:
            self.state.cnt_ready += 1
        else:
            self.state.cnt_ready -= 1
        self.players[player_id].ready_to_play = not self.players[player_id].ready_to_play
        if self.state.cnt_ready == len(self.state.move_queue) > 1 and self.state.round == -1:
            self.state.round = 0
            count_control_token = {2: 11, 3: 7, 4: 5, 5: 4}
            self.state.move_to_next_round = len(self.state.move_queue) * count_control_token[len(self.state.move_queue)]
        return True

    def show_battle_token(self, player_id: int, my_token_id: int) -> BattleToken:
        # does he have the right?
        return self.battle_tokens[my_token_id]

    def get_all_battle_token(self) -> list[BattleToken]:
        return list(self.battle_tokens.values())

    def get_all_control_token(self) -> list[ControlToken]:
        return list(self.control_tokens.values())

    def execution_phase(self):
        # pass
        pass
