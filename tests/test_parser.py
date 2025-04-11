import unittest
from ..utils.parser import split_stat, get_enum_name_from_value, itemID_to_json
from ..utils.enums import ItemID, Rarity, StatTypes

class TestParser(unittest.TestCase):

    def test_split_stat(self):
        self.assertEqual(split_stat("ATK10"), ("ATK", 10))
        self.assertEqual(split_stat("SPD5"), ("SPD", 5))
        self.assertEqual(split_stat("LSC2"), ("LSC", 2))
        self.assertEqual(split_stat("NoDigits"), ("NoDigits", 0))

    def test_get_enum_name_from_value(self):
        # Assuming ItemID, Rarity, and StatTypes enums are defined in utils.enums
        self.assertEqual(get_enum_name_from_value("i01", ItemID), "SWORD")  # Replace with actual enum name
        self.assertEqual(get_enum_name_from_value("E", Rarity), "EPIC")  # Replace with actual enum name
        self.assertEqual(get_enum_name_from_value("ATK", StatTypes), "ATTACK")  # Replace with actual enum name

        with self.assertRaises(ValueError):
            get_enum_name_from_value("INVALID", ItemID)

    def test_itemID_to_json(self):
        # Assuming enums are properly defined in utils.enums
        itemID = "i01-ATK10-SPD5-LSC2-LS10-E"
        name = "Test Item"
        expected_output = {
            "name": "Test Item",
            "item_type": "ITEM_01",  # Replace with actual enum name
            "ATTACK": 10,  # Replace with actual enum name
            "SPEED": 5,  # Replace with actual enum name
            "LIFESTEAL_CRIT": 2,  # Replace with actual enum name
            "LIFESTEAL": 10,  # Replace with actual enum name
            "rarity": "EPIC"  # Replace with actual enum name
        }
        self.assertEqual(itemID_to_json(itemID, name), expected_output)

        # Test invalid itemID
        invalid_itemID = "invalid-ATK10-SPD5-LSC2-LS10-E"
        self.assertIsNone(itemID_to_json(invalid_itemID, name))

        # Test invalid stat
        invalid_stat_itemID = "i01-INVALID10-SPD5-LSC2-LS10-E"
        self.assertIsNone(itemID_to_json(invalid_stat_itemID, name))

        # Test invalid rarity
        invalid_rarity_itemID = "i01-ATK10-SPD5-LSC2-LS10-INVALID"
        self.assertIsNone(itemID_to_json(invalid_rarity_itemID, name))

if __name__ == "__main__":
    unittest.main()