from model import *


class GameFacade:

    def __init__(self, my_board: Board):
        self.board = my_board

    def get_possible_positions_battle_token(self) -> list[tuple[int, int]]:
        # attack from id_1 to id_2 (1 - if can, 0 - else). if id_1 == id_2 -> can protect
        # same for all players
        return self.board.get_possible_position_to_put_battle_token()

    def put_battle_token(self, player_id: int, province_from_id: int, province_to_id: int) -> bool:
        # if from == to, token put like protecting
        pass

    def show_someone_reset(self, player_id: int) -> list[BattleToken]:
        # show players battle_token reset

        # return False, if error, list[BattleToken] else
        return self.board.players[player_id].get_reset()

    def show_active(self, player_id: int) -> list[BattleToken]:
        return self.board.players[player_id].get_active()
        # all token have status. Some on board (face up/down), some free, some used.
        pass

    def show_control_token(self, player_id: int) -> list[ControlToken]:
        # all token have status. Some on board (face up/down), some free, (?some used?)
        pass

    def round_count(self) -> int:
        # return 0 if preparing, 6 if ending game, 1-5 else
        return self.board.state.round

    def whose_move(self) -> int:
        # return player_id whose move
        return self.board.state.move_queue[self.board.state.id_move]

    def show_battle_token_on_board(self, player_id: int, token_id: int) -> BattleToken:
        # probably not int, maybe info about token or position
        # if token_id on board and player has the opportunity
        pass

    def use_card(self, card_id: int):  # -> bool :
        pass

    def get_all_my_cards(self, player_id: int):  # -> list[Card]:
        # card will include not soon
        pass


class StarterFacade:

    def __init__(self, my_board: Board):
        self.board = my_board
        self.unique_id = 1

    def get_unique_id(self) -> int:
        self.unique_id += 1
        return self.unique_id

    def add_player(self, player_id: int) -> bool:
        if player_id not in self.board.players.keys() and len(self.board.players) <= 4:
            self.board.add_player(Player(player_id))
            return True
        return False

    def swap_player_readiness_value(self, player_id: int) -> bool:
        return self.board.swap_player_readiness(player_id)

    def get_free_caste(self) -> list[Caste]:
        # return free cast for this board
        return self.board.get_free_caste()

    def set_caste(self, player_id: int, my_caste: Caste) -> bool:
        if my_caste not in self.get_free_caste() or player_id not in board.players.keys() or \
                self.board.state.round != 0:
            return False
        self.board.players[player_id].set_clan(my_caste)
        self.board.set_control_token_to_capital(my_caste, self.board.players[player_id].control_tokens[0])
        return True

    def get_possible_positions_control_token(self) -> list[int]:
        # need in preparation phase. Return all province without an owner
        return self.board.get_possible_position_to_put_control_token()

    def put_control_token(self, player_id: int, control_token: ControlToken, province_id: int) -> bool:
        if not self.board.state.this_player_move(player_id) or self.board.state.round != 0:
            return False
        if not self.board.put_on_board_control_token(control_token, province_id):
            return False
        return self.board.state.make_move()

    def round_count(self) -> int:
        return self.board.state.round


if __name__ == "__main__":
    board = Board()
    facade = StarterFacade(board)
    print(facade.round_count())

    facade.add_player(1)
    facade.add_player(2)
    facade.swap_player_readiness_value(1)
    facade.swap_player_readiness_value(2)
    facade.set_caste(1, Caste.crane)
    facade.set_caste(2, Caste.lion)
    print(*facade.get_possible_positions_control_token())
    print(facade.round_count())
    for i in range(12):
        facade.put_control_token(1, facade.board.players[1].control_tokens[2 * i], 2 * i)
        facade.put_control_token(2, facade.board.players[2].control_tokens[2 * i + 1], 2 * i + 1)
        print(*facade.get_possible_positions_control_token())
    print(facade.round_count())
