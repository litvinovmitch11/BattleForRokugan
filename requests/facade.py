from model import *


class GameFacade:

    def __init__(self, my_board: Board):
        self.board = my_board

    def get_possible_positions_battle_token(self) -> list[list[int]]:
        # attack from id_1 to id_2 (1 - if can, 0 - else). if id_1 == id_2 -> can protect
        # same for all players
        return self.board.get_possible_position_to_put_battle_token()

    def put_battle_token(self, player_id: int, my_token_id: int, province_from_id: int, province_to_id: int) -> bool:
        if not self.board.state.this_player_move(player_id) or not (1 <= self.board.state.round <= 5):
            return False
        return self.board.put_on_board_battle_token(player_id, my_token_id, province_from_id, province_to_id)

    def show_someone_reset(self, player_id: int) -> list[BattleToken]:
        # show players battle_token reset

        # return False, if error, list[BattleToken] else
        return self.board.players[player_id].get_reset()

    def show_active(self, player_id: int) -> list[BattleToken]:
        return self.board.players[player_id].get_active()
        # all token have status. Some on board (face up/down), some free, some used.
        pass

    def round_count(self) -> int:
        # return 0 if preparing, 6 if ending game, 1-5 else
        return self.board.state.round

    def whose_move(self) -> int:
        # return player_id whose move
        return self.board.state.move_queue[self.board.state.id_move]

    def show_battle_token(self, player_id: int, my_token_id: int) -> BattleToken:
        # probably not int, maybe info about token or position
        # if token_id on board and player has the opportunity
        return self.board.show_battle_token(player_id, my_token_id)

    def get_all_control_token(self) -> list[ControlToken]:
        return self.board.get_all_control_token()

    def get_all_battle_token(self) -> list[BattleToken]:
        return self.board.get_all_battle_token()

    def use_card(self, player_id) -> bool:
        return self.board.used_card(player_id)

    def unused_card(self, player_id: int) -> bool:
        return self.board.unused_card(player_id)

    def get_all_my_cards(self, player_id: int):  # -> list[Card]:
        # card will include not soon
        pass

    def do_execution_phase(self) -> bool:
        return self.board.execution_phase()

    def get_winner(self) -> list[int]:  # return player_id. Empty list if game not finished
        if self.board.state.round == 6:
            return self.board.get_winner()
        else:
            return []

    def get_free_caste(self) -> list[Caste]:
        return self.board.get_free_caste()

    def set_caste(self, player_id: int, my_caste: Caste) -> bool:
        if my_caste not in self.get_free_caste() or player_id not in self.board.players.keys() or \
                self.board.state.round != 0:
            return False
        if not self.board.set_caste_to_player(player_id, my_caste):
            return False
        self.board.set_control_token_to_capital(my_caste, self.board.players[player_id].control_tokens[0])
        return True

    def get_possible_positions_control_token(self) -> list[int]:
        return self.board.get_possible_position_to_put_control_token()

    def put_control_token(self, player_id: int, control_token_id: int, province_id: int) -> bool:
        if not self.board.state.this_player_move(player_id) or self.board.state.round != 0:
            return False
        return self.board.put_on_board_control_token(player_id, control_token_id, province_id)


class StarterFacade:  # update logic! After this facade must make board

    def __init__(self):
        self.players = dict()  # player_id -> his readiness
        self.unique_id = -1

    def get_unique_id(self) -> int:
        self.unique_id += 1
        return self.unique_id

    def add_player(self, player_id: int) -> bool:
        if player_id not in self.players and len(self.players) <= 4:
            self.players[player_id] = False
            return True
        return False

    def swap_player_readiness_value(self, player_id: int) -> bool:
        if player_id not in self.players:
            return False
        self.players[player_id] = not self.players[player_id]
        return True

    def should_start_game(self) -> bool:
        everyone_ready = True
        for player_id in self.players:
            everyone_ready &= self.players[player_id]
        return len(self.players) > 1 and everyone_ready

    def get_players_ids(self) -> list[int]:
        return [*self.players.keys()]
