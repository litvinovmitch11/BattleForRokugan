import enum


class Caste(enum.Enum):
    crab = "crab"
    crane = "crane"
    lion = "lion"
    scorpion = "scorpion"
    unicorn = "unicorn"
    dragon = "dragon"
    phoenix = "phoenix"
    none = "none"


class TokenType(enum.Enum):
    army = "army"
    fleet = "fleet"
    shinobi = "shinobi"
    blessing = "blessing"
    diplomacy = "diplomacy"
    pogrom = "pogrom"
    empty = "empty"


class SpecialTokenType(enum.Enum):
    scorched_earth = "scorched_earth"
    peace = "peace"
    shrine = "shrine"
    honor = "honor"  # слава
    harbor = "harbor"
    honor_bonus_1 = "honor_bonus_1"  # бонус чести +1
    honor_bonus_2 = "honor_bonus_2"  # бонус чести +2


class CardData:
    province = "province"
    battle_token = "battle_token"
    other_player = "other_player"
    special_token = "special_token"

    throw_off = "throw_off"  # поместить в сброс
    leave_in_stock = "leave_in_stock"  # поместить в запас
