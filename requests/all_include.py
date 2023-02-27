import enum


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
