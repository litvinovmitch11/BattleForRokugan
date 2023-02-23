# dose Facade knows whose request? If yes, info about player are useless

class Facade:

    def __init__(self, player_id):
        self.player = player_id
        self.caste = None
        # request to server say about new player

    def free_caste(self):
        if self.player == 1:
            return ["crab"]
        return ["tsaplya"]

    def choose_clan(self):
        a = input(*self.free_caste())
        self.caste = a
        # next_step

    def get_possible_positions_battle_token(self):
        # same for all players
        pass

    def get_possible_positions_control_token(self):
        # same for all players
        pass

    def put_control_token(self, pos_on_board):
        # check is can player put control token on this position
        pass

    def put_battle_token(self, pos_on_board):
        # check is can player put control token on this position
        pass

    def get_all_my_cards(self):
        if self.player == "crab":
            return ["all"]
        return []

    def use_card(self, player, card):
        player_cards = self.get_player_cards(self, player)
        if len(player_cards) != 0:
            decision = input("Хотите сыграть карту?\n")
        else:
            print("У вас нет карт, вы пропускаете ход\n")
        # should cut later

        # if card == None, move come to next player
        pass

    def show_someone_reset(self, player, whose_reset):
        # show players battle_token
        pass

    def get_all_my_battle_token(self, player):
        # all token have status. Some on board (face up/down), some free, some used.
        pass

    def get_all_my_control_token(self, player):
        # all token have status. Some on board (face up/down), some free, (?some used?)
        pass

    def round_count(self):
        # return 0 if preparing, 6 if ending game, 1-5 else
        pass

    def get_board(self):
        # return all board (all status), may be replaced by many function
        pass

    def whose_move(self):
        # obvi
        pass

    def show_battle_token(self, token_id):
        pass
