# Везде, где возвращаю BattleToken или ControlToken, судя по всему эти классы будут приведены в простой вид
# Чтобы Леша смог их отрисовать (вероятно просто айдиншник/какой стороной повернут/позицию на карте)

from model import *


class Facade:

    def __init__(self, my_board: Board):
        self.board = my_board

    def make_player_unique_id(self) -> int:
        # need to assign id to a player
        pass

    def add_player(self, player_id: int) -> bool:
        # видимо раз добавляю player в фасад, то знаю на какую доску
        pass

    def get_free_caste(self) -> list[Caste]:
        # return free cast for this board
        return self.board.get_free_caste()

    def set_clan(self, player_id: int, my_caste: Caste) -> bool:
        if my_caste in self.board.get_free_caste():
            # here adding putting this cast to this player
            return True
        return False

    def get_possible_positions_battle_token(self) -> list[tuple[int, int]]:
        # attack from id_1 to id_2. if id_1 == id_2 -> can protect
        # same for all players
        pass

    def get_possible_positions_control_token(self, my_board: Board) -> list[int]:
        # need in preparation phase. Return all province without an owner
        pass

    def put_control_token(self, player_id: int, province_id: int) -> bool:
        # check is can player put control token on this position
        pass

    def put_battle_token(self, player_id: int, province_from_id: int, province_to_id: int) -> bool:
        # if from == to, token put like protecting
        pass

    def show_someone_reset(self, whose_reset_id: int) -> list[BattleToken]:
        # show players battle_token reset
        pass

    def show_active(self, player_id: int) -> list[BattleToken]:
        # all token have status. Some on board (face up/down), some free, some used.
        pass

    def show_control_token(self, player_id: int) -> list[ControlToken]:
        # all token have status. Some on board (face up/down), some free, (?some used?)
        pass

    def round_count(self) -> int:
        # return 0 if preparing, 6 if ending game, 1-5 else
        pass

    def get_board(self) -> Board:
        # return all board (all status), may be replaced by many function, should rewrite
        pass

    def whose_move(self) -> int:
        # return player_id whose move
        pass

    def show_battle_token_on_board(self, player_id: int, token_id: int) -> BattleToken:
        # probably not int, maybe info about token or position
        # if token_id on board and player has the opportunity
        pass

    def use_card(self, card_id: int):  # -> bool :
        pass

    def get_all_my_cards(self, player_id: int):  # -> list[Card]:
        # card will include not soon
        pass