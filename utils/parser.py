import json
import logging
from enum import Enum
from utils.enums import ItemID, Rarity
from utils.enums import StatTypes

# Configure logging (you can adjust the level and format as needed)
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def split_stat(stat_str: str)-> tuple[str, int]:
    """
    Split a stat string into its type and value.
    args:
        stat_str (str): The stat string to split.
    returns:
        tuple: A tuple containing the stat type and value.
    """
    for i, c in enumerate(stat_str):
        if c.isdigit():
            return stat_str[:i], int(stat_str[i:])
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
    itemObject = {
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

def json_to_itemID(item_json: dict) -> str:
    """
    Convert a JSON dict to an itemID string.
    
    Args:
        item_json (dict): The JSON dict to convert.
        
    Returns:
        str: The itemID string representation of the JSON dict.
    
    Expected Structure:
        item_json (dict): A dictionary with the following keys:
            - "name" (str): The name of the item.
            - "item_type" (str): The type of the item, corresponding to a valid `ItemID` enum name.
            - "rarity" (str): The rarity of the item, corresponding to a valid `Rarity` enum name.
            - Additional keys (str): Stat types corresponding to valid `StatTypes` enum names, with their values as integers.

        logging.error('Missing \'name\' key in item_json')
        Example input: {"name": "Test Item", "item_type": "i01", "rarity": "E", "ATK": 10, "SPD": 5, "LSC": 2, "LS": 10}
        This will convert the JSON dict back to an itemID string.
    """
    try:
        name = item_json["name"]
    except KeyError:
        logging.error("Missing 'name' key in item_json")
        return None
    try:
        item_type = item_json["item_type"]
        if item_type not in [item.name for item in ItemID]:
            logging.error(f"Invalid 'item_type': {item_type}")
            return None
    except KeyError:
        logging.error("Missing 'item_type' key in item_json")
        return None
    try:
        rarity = item_json["rarity"]
        if rarity not in [rar.name for rar in Rarity]:
            logging.error(f"Invalid 'rarity': {rarity}")
            return None
    except KeyError:
        logging.error("Missing 'rarity' key in item_json")
        return None
    list_of_stats = []
    for stat_key, value in item_json.items():
        if stat_key not in ["name", "item_type", "rarity"]:  # Skip non-stat keys
            if isinstance(value, (int, float, str)):  # Check if value is a primitive type
                list_of_stats.append(stat_key + str(value))
            else:
                logging.warning(f"Skipping non-primitive stat: {stat_key} with value: {value}")
    
    stats_string = "-".join(list_of_stats)
    itemID = f"{item_type}-{stats_string}-{rarity}"
    return itemID