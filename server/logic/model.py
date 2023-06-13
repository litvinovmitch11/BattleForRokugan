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

    def to_reset(self):
        self.on_board = (-1, -1)
        self.in_reset = True
        self.in_active = False
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

    def to_reset(self):
        self.province_id = -1
        self.visible = False


class Player:
    def __init__(self, values: (int, str)):
        self.caste = Caste.none  # class Caste
        self.battle_tokens = []  # list BattleTokens
        self.control_tokens = []  # list ControlTokens
        self.active = []  # list BattleTokens
        self.player_id = values[0]  # int
        self.name = values[1]  # str

        self.cards = dict()  # int: id card -> class Card
        self.ready_to_play = False  # bool

    def set_caste(self, my_caste: Caste) -> bool:
        if self.caste is not Caste.none:
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
        self.battle_tokens.append(
            BattleToken(self.caste, 2 if self.caste == Caste.lion else 0, TokenType.empty, token_id + 2))
        token_id += 3
        random.shuffle(self.battle_tokens)

    def take_control_token(self):
        global token_id
        power = 2 if self.caste == Caste.crab else 1
        for i in range(130):
            self.control_tokens.append(ControlToken(self.caste, power, token_id))
            token_id += 1

    def make_active(self):
        for token in self.battle_tokens:
            if token.type == TokenType.empty and not token.in_active:
                if token.caste == Caste.lion and token.on_board != (-1, -1):
                    continue
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

    def get_free_control_token(self) -> ControlToken:
        for token in self.control_tokens:
            if token.province_id == -1:
                return token


class GameState:

    def __init__(self):
        self.id_move = 0  # 1st player start all time?
        self.move_queue = []  # player_ids
        self.round = -1  # -1 -> adding_players, 0 -> putting control_tokens/choose caste,  1-5 -> round of game
        self.move_to_next_round = 0
        self.phase = 0  # in range [1, 3]

    def this_player_move(self, player_id: int) -> bool:
        return self.move_queue[self.id_move] == player_id

    def make_move(self) -> bool:
        self.move_to_next_round -= 1
        self.id_move = (self.id_move + 1) % len(self.move_queue)
        return True

    def add_player(self, my_player: Player) -> bool:
        self.move_queue.append(my_player.player_id)
        return True

    def used_card(self, was_used: bool):
        if was_used:
            self.make_move()
            self.move_to_next_round = len(self.move_queue) - 1
        else:
            self.make_move()

    def next_round(self):
        self.round += 1
        # if round == 6 cringe
        self.phase = 1
        self.id_move = random.randint(0, len(self.move_queue) - 1)
        self.move_to_next_round = len(self.move_queue)
        # for used/unused cards

    def is_adding_players(self):
        return self.round == -1


class Province:

    def __init__(self, ind: int):
        self.capital = False
        self.mainland = False  # материковая. False - если прибрежная
        self.shadow = False
        self.caste = Caste.none
        self.owning_caste = Caste.none
        self.card_id_inside = -1  # can be only in capital or shadow province

        self.battle_inside = []
        self.battle_outside = []
        self.protection_battle_token = []
        self.control_tokens = []
        self.special_tokens = []

        self.ind = ind
        self.glory_points = 0
        self.control_power = 0

        self.set_correct_field_value(ind)

    def set_correct_field_value(self, ind):
        if ind in [27, 25, 23, 18, 16, 14, 5]:
            self.capital = True
            self.control_power = 2
        if ind in [3, 4]:
            self.shadow = True
            self.control_power = 1
        if ind not in [0, 1, 2, 3, 5, 9, 11, 12, 13, 14, 15, 29]:
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

    def remove_fake_tokens(self):
        if self.ind == 30:
            for token in self.battle_inside + self.protection_battle_token:
                token.on_board = (-1, -1)
                if token.type != TokenType.empty:
                    token.in_reset = True
            for token in self.battle_outside:
                if token.type != TokenType.fleet:
                    token.on_board = (-1, -1)
                    if token.type != TokenType.empty:
                        token.in_reset = True
        else:
            for token in self.battle_inside + self.battle_outside:
                if token.type in [TokenType.diplomacy, TokenType.fleet, TokenType.blessing]:
                    token.on_board = (-1, -1)
                    token.in_reset = True
                if token.type == TokenType.empty:
                    token.on_board = (-1, -1)
            for token in self.protection_battle_token:
                if (token.type == TokenType.fleet and self.mainland) or (token.type == TokenType.blessing):
                    token.on_board = (-1, -1)
                    token.in_reset = True
                if token.type == TokenType.empty:
                    if not (token.caste == Caste.lion and self.owning_caste == Caste.lion):
                        token.on_board = (-1, -1)

    def remove_token_after_battles(self):
        for token in self.battle_outside + self.battle_inside + self.protection_battle_token:
            if token.caste == Caste.lion and token.type == TokenType.empty and token in self.protection_battle_token:
                continue
            token.on_board = (-1, -1)
            if token.type != TokenType.empty:
                token.in_reset = True

    def get_winner(self) -> Caste:
        # suppose all tokens.py are correct. NO, smth can be token.on_board == (-1, -1)
        points = dict()
        for caste in Caste:
            points[caste] = 0
        points[self.owning_caste] = self.control_power
        for control_token in self.control_tokens:
            if control_token.visible:
                points[control_token.caste] += control_token.power
        for battle_token in self.protection_battle_token:
            if battle_token.on_board != (-1, -1):
                points[battle_token.caste] += battle_token.power
        for battle_token in self.battle_inside:
            if battle_token.on_board != (-1, -1):
                points[battle_token.caste] += battle_token.power
        max_power = 0
        winner = [Caste.none]
        for caste in Caste:
            if points[caste] > max_power:
                max_power = points[caste]
                winner = [caste]
            elif points[caste] == max_power:
                winner.append(caste)

        points[self.owning_caste] -= self.control_power
        phoenix_win = True
        for caste in Caste:
            if points[caste] >= points[Caste.phoenix] and caste != Caste.phoenix:
                phoenix_win = False

        if phoenix_win:
            return Caste.phoenix

        if len(winner) == 1:
            return winner[0]
        if Caste.crane in winner:
            return Caste.crane
        if self.owning_caste in winner:
            return self.owning_caste
        return Caste.none

    def set_boost_to_winner(self, caste: Caste, control_token: ControlToken):
        if self.owning_caste == Caste.none or self.owning_caste != caste:
            for c_t in self.control_tokens:
                c_t.to_reset()
            self.control_tokens.clear()
            self.owning_caste = caste
            control_token.province_id = self.ind
            self.control_tokens.append(control_token)
        elif caste == self.owning_caste:
            control_token.make_visible()
            control_token.province_id = self.ind
            self.control_tokens.append(control_token)


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

        self.all_card = dict()  # id -> class Card
        self.take_cards()

    def take_cards(self):
        for prov in self.all_provinces:
            card = None
            if prov.capital:
                if prov.caste == Caste.dragon:
                    card = CardMovingTowardsTheGoal()
                if prov.caste == Caste.crab:
                    card = CardAccessToTheSea()
                if prov.caste == Caste.crane:
                    card = CardDiplomaticMission()
                if prov.caste == Caste.lion:
                    card = CardGloriousBattle()
                if prov.caste == Caste.phoenix:
                    card = CardCleansing()
                if prov.caste == Caste.scorpion:
                    card = CardLightsOfTheUprising()
                if prov.caste == Caste.unicorn:
                    card = CardCulturalExchange()
            if card is not None:
                self.all_card[card.ind] = card
                prov.card_id_inside = card.ind
        independent_region = {0: CardProsperity(), 3: CardThePowerOfTerror(), 4: CardKillingTheWeak(),
                              9: CardRichHarvest()}
        for prov_id in [0, 3, 4, 9]:  # add cards
            card = independent_region[prov_id]
            self.all_card[card.ind] = card
            self.all_provinces[prov_id].card_id_inside = card.ind

    def add_player(self, values: (int, str)):
        if 0 <= len(self.players) <= 4 and self.state.is_adding_players():
            player = Player(values)
            self.players[values[0]] = player
            self.state.add_player(player)

    def swap_player_readiness_value(self, player_id: int) -> bool:  # return should start game
        if player_id not in self.players:
            return False
        player = self.players[player_id]
        player.ready_to_play = not player.ready_to_play
        all_ready = True
        for id_player in self.players:
            all_ready &= self.players[id_player].ready_to_play
        if len(self.players) > 1 and all_ready:
            if self.state.round == -1:
                self.start_game()
                return True
            elif self.state.phase == 3:
                self.execution_phase()
                return True
        return False

    def get_free_caste(self) -> list[Caste]:
        free_castes = []
        for watching_caste in Caste:
            used_caste = False
            for player in self.players.values():
                if player.caste == watching_caste:
                    used_caste = True
            if not used_caste and watching_caste != Caste.none:
                free_castes.append(watching_caste)
        return free_castes

    def set_caste_to_player(self, player_id: int, my_caste: Caste) -> bool:
        if my_caste not in self.get_free_caste() or player_id not in self.players.keys() or self.state.round != 0:
            return False
        if not self.players[player_id].set_caste(my_caste):
            return False
        for control_token in self.players[player_id].control_tokens:
            self.control_tokens[control_token.id] = control_token
        for battle_token in self.players[player_id].battle_tokens:
            self.battle_tokens[battle_token.id] = battle_token
        self.set_control_token_to_capital(my_caste, self.players[player_id].control_tokens[0])
        return True

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
        if self.state.move_to_next_round <= 0 or self.state.phase != 2:
            return False
        if not (min(ind_finish, ind_start) >= 0 and max(ind_finish, ind_start) <= 30) \
                or self.can_put_army_token[ind_start][ind_finish] == 0 \
                or battle_token_id not in self.battle_tokens.keys():
            return False
        my_battle_token = self.battle_tokens[battle_token_id]
        if my_battle_token.caste != self.players[player_id].caste or \
                my_battle_token not in self.players[player_id].active:
            return False
        self.players[player_id].active.remove(my_battle_token)
        my_battle_token.on_board = (ind_start, ind_finish)
        my_battle_token.in_active = False

        if ind_start == ind_finish:
            self.all_provinces[ind_start].protection_battle_token.append(my_battle_token)
        else:
            self.all_provinces[ind_start].battle_outside.append(my_battle_token)
            self.all_provinces[ind_finish].battle_inside.append(my_battle_token)
            self.can_put_army_token[ind_start][ind_finish] = 0
        self.state.make_move()
        if self.state.move_to_next_round == 0:
            self.state.phase = 3
            self.make_all_battle_tokens_on_board_visible()
            for id_player in self.players:
                self.players[id_player].ready_to_play = False
            # !!! do execution phase. IMPORTANT !!!
        return True

    def put_on_board_control_token(self, player_id: int, province_id: int) -> bool:  # only when round = 0 (preparation)
        if player_id not in self.players:
            return False
        my_control_token = self.players[player_id].get_free_control_token()
        for item in self.all_provinces[province_id].control_tokens:
            if item.caste == my_control_token.caste:
                my_control_token.visible = True
            else:
                my_control_token.visible = False
                return False
        self.all_provinces[province_id].control_tokens.append(my_control_token)
        my_control_token.province_id = province_id
        self.state.make_move()
        if self.state.move_to_next_round == 0 and self.state.round == 0:
            # use card instead random in future
            self.state.id_move = random.randrange(len(self.state.move_queue))
            self.state.phase = 1
            self.state.round = 1
            self.state.move_to_next_round = len(self.state.move_queue)
            for player in self.players.values():
                player.make_active()
            # try to use card
        return True

    def set_control_token_to_capital(self, my_caste: Caste, my_control_token: ControlToken):
        for province in self.all_provinces:
            if province.capital and province.caste == my_caste:
                province.control_tokens.append(my_control_token)

    def get_all_battle_token(self) -> list[BattleToken]:
        return list(self.battle_tokens.values())

    def get_all_control_token(self) -> list[ControlToken]:
        return list(self.control_tokens.values())

    def execution_phase(self):
        for province in self.all_provinces:
            province.remove_fake_tokens()

        # use pogrom token
        for province in self.all_provinces:
            token_caste = Caste.none
            should_play = False
            inside = False
            for token in province.protection_battle_token:
                if token.type == TokenType.pogrom:
                    inside = True
                    token_caste = token.caste
                if token.type == TokenType.shinobi:
                    should_play = True
            for prov_neighbour in self.all_provinces:
                if have_land_way[province.ind][prov_neighbour.ind] and prov_neighbour.owning_caste == token_caste and \
                        prov_neighbour.ind != province.ind:
                    should_play = True
            if inside and should_play:
                province.owning_caste = Caste.none
                for token in province.battle_outside + province.battle_inside + province.protection_battle_token:
                    token.to_reset()
                province.battle_inside = []
                province.battle_outside = []
                province.protection_battle_token = []
                for token in province.control_tokens:
                    token.to_reset()
                province.control_tokens = []
                province.special_tokens = [SpecialTokenType.scorched_earth]
                for i in range(31):
                    have_land_way[i][province.ind] = 0
                    have_land_way[province.ind][i] = 0

        # use diplomacy token
        for province in self.all_provinces:
            for token in province.protection_battle_token:
                if token.type == TokenType.diplomacy and province.owning_caste == token.caste:
                    province.special_tokens.append(SpecialTokenType.shrine)
                    for my_token in province.battle_inside + province.protection_battle_token:
                        my_token.to_reset()
                    province.battle_inside = []
                    province.protection_battle_token = []

        # do all battle
        for province in self.all_provinces:
            winner = province.get_winner()
            if winner != Caste.none:
                for player in self.players.values():
                    if player.caste == winner:  # find winner
                        token = player.get_free_control_token()
                        province.set_boost_to_winner(winner, token)  # set correct_value
                        break

        self.take_region_cards()
        for province in self.all_provinces:
            province.remove_token_after_battles()
        self.state.next_round()
        self.can_put_army_token = have_land_way
        for player in self.players.values():
            player.make_active()

    def take_region_cards(self):
        for province_with_card in self.all_provinces:
            if province_with_card.card_id_inside == -1:
                continue
            owner = province_with_card.owning_caste
            if province_with_card.ind in [0, 9]:
                to = [0, 1, 2] if province_with_card.ind == 0 else [9, 10, 11]
                for prov_id in to:
                    if owner != self.all_provinces[prov_id].owning_caste:
                        owner = Caste.none
            for prov in self.all_provinces:
                if prov.caste == Caste.none:
                    continue
                if prov.caste == province_with_card.caste and owner != prov.owning_caste:
                    owner = Caste.none
            if owner == Caste.none:
                continue
            card_id = province_with_card.card_id_inside

            for player in self.players.values():
                if player.caste == owner:
                    player.cards[card_id] = self.all_card[card_id]
                    self.all_card[card_id].set_owner(player.player_id)
                    province_with_card.card_id_inside = -1
                    self.all_card[card_id].set_owner(player.player_id)
                    break

    def make_all_battle_tokens_on_board_visible(self):
        for token in self.battle_tokens.values():
            if token.on_board != (-1, -1):
                token.make_visible()

    def get_special_tokens(self) -> list[(int, SpecialTokenType)]:
        ans = []
        for province in self.all_provinces:
            for sp_t in province.special_tokens:
                ans.append((province.ind, sp_t))
        return ans

    def used_card(self, player_id: int, card_id: int, data: list[int]) -> bool:
        # need redone
        if not self.state.this_player_move(player_id):
            return False
        if self.all_card[card_id].apply(self, player_id, data):
            self.state.used_card(True)
            return True
        return False

    def unused_card(self, player_id: int) -> bool:
        if not self.state.this_player_move(player_id) or self.state.phase != 1:
            return False
        self.state.used_card(False)
        if self.state.move_to_next_round == 0:
            self.state.phase = 2
            self.state.move_to_next_round = len(self.state.move_queue) * 5
        return True

    def get_game_winner(self) -> list[int]:
        if self.state.round != 6:
            return []
        points = dict()
        for caste in Caste:
            points[caste] = 0
        ans = []
        for province in self.all_provinces:
            if province.owning_caste != Caste.none:
                points[province.owning_caste] += province.glory_points
        for token in self.control_tokens.values():
            if token.province_id != -1 and token.visible:
                points[token.caste] += 1
        # point for secret goal
        for caste in Caste:
            if caste == Caste.none:
                continue
            region = []
            for province in self.all_provinces:
                if province.caste == caste:
                    region.append(province)

            one_owning = True
            for i in range(len(region)):
                province = region[i]
                if province.owning_caste != region[0].owning_caste:
                    one_owning = False
            if one_owning:
                points[region[0].owning_caste] += 5

        max_point = 0
        for caste in Caste:
            max_point = max(max_point, points[caste])
        for caste in Caste:
            if points[caste] == max_point:
                for player in self.players.values():
                    if player.caste == caste:
                        ans.append(player.player_id)
        return ans

    def start_game(self):
        self.state.round = 0
        count_control_token = {2: 11, 3: 7, 4: 5, 5: 4}
        self.state.move_to_next_round = len(self.state.move_queue) * count_control_token[len(self.state.move_queue)]


class Card:

    def __init__(self, card_id=-1):
        self.ind = card_id
        self.owner = -1  # player_id
        self.caste = Caste.none
        self.data = []
        self.used = False

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        if not board.state.this_player_move(player_id) or board.state.phase != 1 or self.used:
            return False

    def set_owner(self, player_id):
        self.owner = player_id

    @staticmethod
    def all_prov_id_correct(*data):
        inside = []
        for elem in data:
            if type(elem) != int or not 0 <= elem <= 29 or elem in inside:
                return False
            inside.append(elem)
        return True


class CardMovingTowardsTheGoal(Card):  # двжиение к цели. Клан дракона. ID=1

    def __init__(self):
        super().__init__(1)
        self.caste = Caste.dragon
        self.data = [CardData.province, CardData.province]
        # owning_province, owning_province (not same)

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        if not super().apply(board, player_id, data):
            return False
        # data contains prov_1_id and prov_2_id
        if len(data) != 2 or not self.all_prov_id_correct(data):
            return False
        prov_1 = data[0]
        prov_2 = data[1]
        player = board.players[player_id]
        if not (board.all_provinces[prov_1].owning_caste == player.caste and
                board.all_provinces[prov_2].owning_caste == player.caste and prov_1 != prov_2):
            return False
        for prov in [prov_1, prov_2]:
            token = player.get_free_control_token()
            token.province_id = prov
            token.visible = True
            board.all_provinces[prov].control_tokens.append(token)
        self.used = True
        return True


class CardLightsOfTheUprising(Card):  # Огни восстания. Клан скорпиона. ID=2
    def __init__(self):
        super().__init__(2)
        self.caste = Caste.scorpion
        self.data = [CardData.province]
        # province_with_peace

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        if not super().apply(board, player_id, data):
            return False
        # data contains province_id
        if len(data) != 1 or not self.all_prov_id_correct(data):
            return False
        prov = board.all_provinces[data[0]]
        player = board.players[player_id]
        if SpecialTokenType.peace not in prov.special_tokens:
            return False
        prov.special_tokens.remove(SpecialTokenType.peace)
        if prov.owning_caste == player.caste:
            for i in range(2):
                token = player.get_free_control_token()
                token.province_id = prov.ind
                token.visible = True
                prov.control_tokens.append(token)
        self.used = True
        return True


class CardCleansing(Card):  # Очищение. Клан Феникцса. ID=3

    def __init__(self):
        super().__init__(3)
        self.caste = Caste.phoenix
        self.data = [CardData.province]
        # province_with_scorched_earth

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        if not super().apply(board, player_id, data):
            return False
        # data contains province_id
        if len(data) != 1 or not self.all_prov_id_correct(data):
            return False
        prov = board.all_provinces[data[0]]
        player = board.players[player_id]
        if SpecialTokenType.scorched_earth not in prov.special_tokens:
            return False
        prov.special_tokens.remove(SpecialTokenType.scorched_earth)
        for i in range(2):
            token = player.get_free_control_token()
            token.province_id = prov.ind
            if i == 1:
                token.visible = True
            prov.control_tokens.append(token)
        self.used = True
        return True


class CardCulturalExchange(Card):  # Культурный обмен. Клан единорога. ID=4. Be careful!

    def __init__(self):
        super().__init__(4)
        self.caste = Caste.unicorn
        self.data = [CardData.province, CardData.province]
        # owning_province, other_owning_province

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        # owning_prov_id, other_owning_prov_id
        if not super().apply(board, player_id, data):
            return False
        if len(data) != 2 or not self.all_prov_id_correct(data):
            return False
        my_prov = board.all_provinces[data[0]]
        other_prov = board.all_provinces[data[1]]
        my_player = board.players[player_id]
        if my_prov.owning_caste != my_player.caste or other_prov.owning_caste == my_player.caste or \
                other_prov.owning_caste == Caste.none:
            return False
        if SpecialTokenType.scorched_earth in my_prov.special_tokens or \
                SpecialTokenType.scorched_earth in other_prov.special_tokens:
            return False
        my_tokens = my_prov.control_tokens
        other_tokens = other_prov.control_tokens

        for token in my_tokens:
            token.province_id = other_prov.ind
        for token in other_tokens:
            token.province_id = my_prov.ind

        my_prov.control_tokens = other_tokens
        other_prov.control_tokens = my_tokens

        my_prov.owning_caste, other_prov.owning_caste = other_prov.owning_caste, my_prov.owning_caste
        self.used = True
        return True


class CardAccessToTheSea(Card):  # Выход к морю. Каста краба. ID=5

    def __init__(self):
        super().__init__(5)
        self.caste = Caste.crab
        self.data = [CardData.province]
        # mainland_province

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        # province_id
        if not super().apply(board, player_id, data):
            return False
        if len(data) != 1 or not self.all_prov_id_correct(data):
            return False
        prov = board.all_provinces[data[0]]
        if not prov.mainland or SpecialTokenType.scorched_earth in prov.special_tokens or \
                SpecialTokenType.harbor in prov.special_tokens:
            return False
        prov.special_tokens.append(SpecialTokenType.harbor)
        self.used = True
        return True


class CardGloriousBattle(Card):  # Славная битва. Каста льва. ID=6

    def __init__(self):
        super().__init__(6)
        self.caste = Caste.lion
        self.data = [CardData.province]
        # any_province

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        # province_id
        if not super().apply(board, player_id, data):
            return False
        if len(data) != 1 or not self.all_prov_id_correct(data):
            return False
        prov = board.all_provinces[data[0]]
        if SpecialTokenType.scorched_earth in prov.special_tokens or SpecialTokenType.honor in prov.special_tokens:
            return False
        prov.special_tokens.append(SpecialTokenType.honor)
        self.used = True
        return True


class CardDiplomaticMission(Card):  # Кодекс чести. Каста журавля. ID=7

    def __init__(self):
        super().__init__(7)
        self.caste = Caste.crane
        self.data = [CardData.province, CardData.province]
        # any_province_not_shadow, any_province_not_shadow

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        # prov_1_id, prov_2_id
        if not super().apply(board, player_id, data):
            return False
        if len(data) != 2 or self.all_prov_id_correct(data):
            return False
        prov_1 = board.all_provinces[data[0]]
        prov_2 = board.all_provinces[data[1]]
        if prov_1.shadow or prov_2.shadow:
            return False
        prov_1.special_tokens.append(SpecialTokenType.honor_bonus_1)
        prov_2.special_tokens.append(SpecialTokenType.honor_bonus_1)
        self.used = True
        return True


class CardRichHarvest(Card):  # Богатый урожай. (9, 10, 11) провинции. ID=8

    def __init__(self):
        super().__init__(8)
        self.data = [CardData.province]
        # owning_province

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        # prov_1_id
        if not super().apply(board, player_id, data):
            return False
        if len(data) != 1 or self.all_prov_id_correct(data):
            return False
        prov = board.all_provinces[data[0]]
        player = board.players[player_id]
        if prov.owning_caste != player.caste:
            return False
        for i in range(2):
            token = player.get_free_control_token()
            token.province_id = prov.ind
            token.visible = True
            prov.control_tokens.append(token)
        self.used = True
        return True


class CardProsperity(Card):  # Процветание. (0, 1, 2) провинции. ID=9
    def __init__(self):
        super().__init__(9)
        self.data = [CardData.province]
        # any_province_not_shadow

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        # prov_id
        if not super().apply(board, player_id, data):
            return False
        if len(data) != 1 or self.all_prov_id_correct(data):
            return False
        prov = board.all_provinces[data[0]]
        if prov.shadow:
            return False
        prov.special_tokens.append(SpecialTokenType.honor_bonus_2)
        self.used = True
        return True


class CardThePowerOfTerror(Card):  # Власть ужаса. Теневая провинция вниз. ID=10

    def __init__(self):
        super().__init__(9)
        self.data = [CardData.province, CardData.province, CardData.special_token, CardData.province,
                     CardData.special_token]

    # owning_province_not_shadow, province_with_special_token, SpecialToken, province_with_special_token, SpecialToken

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        if player_id not in board.players or self.owner != player_id or not board.state.this_player_move(player_id):
            return False
        if self.used or not (len(data) not in (3, 5)) or not 0 <= data[2] <= 6:
            return False
        sp_ts = [list(SpecialTokenType)[data[2]]]
        if len(data) == 5:
            if not 0 <= data[4] <= 6:
                return False
            sp_ts.append(list(SpecialTokenType)[data[4]])
        for i in range(1, len(data), 2):
            prov = board.all_provinces[data[i]]
            if sp_ts[i - 1 - i // 2] not in prov.special_tokens:
                return False
        for i in range(1, len(data), 2):
            prov = board.all_provinces[data[i]]
            prov.special_tokens.remove(sp_ts[i - 1 - i // 2])
        self.used = True
        return True


class CardKillingTheWeak(Card):  # Умерщвление слабых. Теневая провинция вверх. ID=11
    def __init__(self):
        super().__init__(11)
        self.data = [CardData.battle_token, CardData.battle_token, CardData.battle_token]
        # battle_token_in_active_id, other_battle_token_on_board_id, other_battle_token_on_board_id

    def apply(self, board: Board, player_id: int, data: list[int]) -> bool:
        if player_id not in board.players or self.owner != player_id or not board.state.this_player_move(player_id):
            return False
        if self.used or len(data) != 3 or type(data[0]) != int or type(data[1]) != int or type(data[2]) != int:
            return False
        if board.state.phase != 2:
            return False
        for ind in data:
            if ind not in board.battle_tokens:
                return False
        my_token = board.battle_tokens[data[0]]
        other_token_1 = board.battle_tokens[data[1]]
        other_token_2 = board.battle_tokens[data[2]]
        player = board.players[player_id]

        if my_token not in player.active or other_token_1.on_board == (-1, -1) or \
                other_token_2.on_board == (-1, -1) or other_token_1.caste == player.caste or \
                other_token_2.caste == player.caste:
            return False

        player.active.remove(my_token)
        my_token.in_active = False
        my_token.in_reset = True
        board.state.make_move()

        for token in [other_token_1, other_token_2]:
            prov_from, prov_to = token.on_board
            if prov_to != prov_from:
                board.all_provinces[prov_from].battle_outside.remove(token)
                board.all_provinces[prov_to].battle_inside.remove(token)
            else:
                board.all_provinces[prov_to].protection_battle_token.remove(token)
            token.on_board = (-1, -1)
            token.in_reset = True
        self.used = True
        return True
