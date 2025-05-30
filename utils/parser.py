import json
import logging
from enum import Enum
from utils.enums import ItemID, Rarity
from utils.enums import StatTypes

# Configure logging (you can adjust the level and format as needed)
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def split_stat(stat_str: str) -> tuple[str, int]:
    """
    Split a stat string into its type and value.
    """
    for i, c in enumerate(stat_str):
        if c.isdigit():
            stat_type = stat_str[:i]
            value = int(stat_str[i:])
            # Validate the stat type against the StatTypes enum
            if stat_type not in StatTypes.__members__.values():
                raise ValueError(f"Invalid stat type: {stat_type}")
            return stat_type, value
    # If no digits are found, return the stat type with a value of 0
    if stat_str not in StatTypes.__members__.values():
        raise ValueError(f"Invalid stat type: {stat_str}")
    return stat_str, 0

def get_enum_name_from_value(value: str, enumtype: Enum) -> str:
    """
    Get the enum name from its value.
    args:
        value (str): The value of the enum.
        enumtype (Enum): The enum type to search in.
    returns:
        str: The name of the enum.
    """
    for item in enumtype:
        if item.value == value:
            return item.name  # or return item if you want the enum itself
    raise ValueError(f"Enum value '{value}' not found in {enumtype.__name__}.")  # or raise an error if not found


def itemID_to_json(itemID: str, name: str) -> dict:
    """
    Convert an itemID to a JSON dict.
    
    Args:
        itemID (str): The item ID to convert.
        name (str): The name of the item.
        
    Returns:
        dict: The JSON dict representation of the item ID.
    
    Examples:
        Example input: "i01-ATK10-SPD5-LSC2-LS10-E"
        This will use the enum to get the itemID and rarity.
    """
    itemObject: dict = {
        "name": name,
    }
    itemID_segments = itemID.split("-")
    itemID = itemID_segments[0]
    stats = itemID_segments[1:-1]
    rarity = itemID_segments[-1]
    try:
        itemObject["item_type"] = get_enum_name_from_value(itemID, ItemID)
    except ValueError as e:
        logging.error(e.args[0])  # Log the error
        return None
    for stat in stats:
        strStat, value = split_stat(stat)
        try:
            itemObject[get_enum_name_from_value(strStat, StatTypes)] = int(value)
        except ValueError as e:
            logging.error(e.args[0])  # Log the error
            return None
    try:
        itemObject["rarity"] = get_enum_name_from_value(rarity, Rarity)
    except ValueError as e:
        logging.error(e.args[0])  # Log the error
        return None
    return itemObject