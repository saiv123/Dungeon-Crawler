from enum import Enum

class ItemID(Enum):
    """
    Enum for item IDs used to uniquely identify different types of items in the game.
    """
    SWORD = "i01"
    BOW = "i02"
    STAFF = "i03"
    SHIELD = "i04"
    HELMET = "i05"
    CHEST = "i06"
    LEGS = "i07"
    BOOTS = "i08"
    RING = "i09"
    NECKLACE = "i10"

class Rarity(Enum):
    """
    Enum for item rarities, representing the rarity levels of items in the game.
    """
    COMMON = "C"
    UNCOMMON = "UC"
    RARE = "R"
    EPIC = "E"
    LEGENDARY = "L"
    DEVELOPER = "DEV"

class StatTypes(Enum):
    """
    Enum for item stats, representing the different types of statistics that items can have in the game.
    """
    ATTACK = "ATK"
    DEFENSE = "DEF"
    SPEED = "SPD"
    LS_CHANCE = "LSC"
    LIFESTEAL = "LS"
    HEALTH = "HP"
    MANA = "MP"
    MANA_COST = "MPC"
