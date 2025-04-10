from utils.parser import itemID_to_json, json_to_itemID

id = "i01-ATK10-SPD5-LSC2-LS10-E"
name = "Test Item"
dictObj = itemID_to_json(id, name)
reconID = json_to_itemID(dictObj)
print("ID to JSON:", dictObj)  # Expected output: {'name': 'Test Item', 'item_type': 'i01', 'rarity': 'E', 'ATK': 10, 'SPD': 5, 'LSC': 2, 'LS': 10}
print("JSON to ID:", reconID)  # Expected output: "i01-ATK10-SPD5-LSC2-LS10-E"
# Expected output: {'name': 'Test Item', 'item_type': 'i01', 'rarity': 'E', 'ATK': 10, 'SPD': 5, 'LSC': 2, 'LS': 10}

print("equal:", id == reconID)  # Expected output: Tru