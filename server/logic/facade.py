from model import *


class GameFacade:

    def __init__(self):
        self.board = Board()
        self.unique_id = -1

    def get_unique_id(self) -> int:
        self.unique_id += 1
        return self.unique_id

    def add_player(self, player_id: int, name: str) -> list[Player]:
        return self.board.add_player((player_id, name))

    def swap_player_readiness_value(self, player_id: int) -> bool:  # return True if should start game
        return self.board.swap_player_readiness_value(player_id)

    def get_players(self) -> list[Player]:
        return list(self.board.players.values())

    def get_all_special_tokens(self) -> list[(int, SpecialTokenType)]:
        return self.board.get_special_tokens()

    def get_possible_positions_battle_token(self) -> list[list[int]]:
        # attack from id_1 to id_2 (1 - if can, 0 - else). if id_1 == id_2 -> can protect
        # same for all players
        return self.board.get_possible_position_to_put_battle_token()

    def put_battle_token(self, player_id: int, my_token_id: int, province_from_id: int, province_to_id: int) -> bool:
        if not self.board.state.this_player_move(player_id) or not (1 <= self.board.state.round <= 5):
            return False
        return self.board.put_on_board_battle_token(player_id, my_token_id, province_from_id, province_to_id)

    def get_someone_reset(self, player_id: int) -> list[BattleToken]:
        # show players battle_token reset

        # return False, if error, list[BattleToken] else
        return self.board.players[player_id].get_reset()

    def get_player_active(self, player_id: int) -> list[BattleToken]:
        return self.board.players[player_id].get_active()
        # all token have status. Some on board (face up/down), some free, some used.
        pass

    def get_round(self) -> int:  # rename (was round_count)
        # return 0 if preparing, 6 if ending game, 1-5 else
        return self.board.state.round

    def get_phase(self) -> int:
        return self.board.state.phase

    def whose_move(self) -> int:
        # return player_id whose move
        return self.board.state.move_queue[self.board.state.id_move]

    def get_all_control_token(self) -> list[ControlToken]:
        return self.board.get_all_control_token()

    def get_all_battle_token(self) -> list[BattleToken]:
        return self.board.get_all_battle_token()

    def use_card(self, player_id, card_id: int, *data) -> bool:  # add card_id !!!
        return self.board.used_card(player_id, card_id, *data)

    def unused_card(self, player_id: int) -> bool:
        return self.board.unused_card(player_id)

    def get_all_cards(self) -> list[Card]:  # !!!! Теперь не принимаем player_id !!!!
        return list(self.board.all_card.values())

    def do_execution_phase(self) -> bool:
        return self.board.execution_phase()

    def get_winner(self) -> list[int]:  # return list[player_id] (maybe more 1 winner). Empty list if game not finished
        return self.board.get_game_winner()

    def get_free_caste(self) -> list[Caste]:
        return self.board.get_free_caste()

    def set_caste(self, player_id: int, my_caste: Caste) -> bool:
        if not self.board.set_caste_to_player(player_id, my_caste):
            return False
        return True

    def get_possible_positions_control_token(self) -> list[int]:
        return self.board.get_possible_position_to_put_control_token()

    def put_control_token(self, player_id: int, province_id: int) -> bool:  # del control_token_id
        if not self.board.state.this_player_move(player_id) or self.board.state.round != 0:
            return False
        return self.board.put_on_board_control_token(player_id, province_id)
