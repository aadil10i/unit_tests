def calculate_total(items_purchased, pinned_list):
    item_prices = {
        "health_potion": 10.00,
        "mana_potion": 12.00,
        "gold_dust": 5.00,
        "dwarven_ale": 8.00,
        "enchanted_scroll": 25.00,
        "ice_cold_milk": 50.00,
        "herbs": 7.00,
        "crystal_shard": 20.00,
        "magic_ring": 100.00,
        "mystic_amulet": 150.00,
    }
    total_price = 0
    receipt = {}
    unpurchased_items = []

    for item in items_purchased:
        if item in item_prices:
            receipt[item] = item_prices[item]
            total_price += item_prices[item]
            # item_prices[item]
            # if item element exists as key in item_prices, retrieve value associated with that key

    for pinned in pinned_list:
        if pinned not in items_purchased: 
            unpurchased_items.append(pinned) 

    # inputs = items purchased
    # inputs = items_needed
    # output receipt = dict of items purchased + price (key: item, value: price)
   
    return unpurchased_items, receipt, total_price

items_purchased =           [
                "health_potion",
                "mana_potion",
                "gold_dust",
                "herbs",
                "crystal_shard",
                "dwarven_ale",
            ]

pinned_list =              [
                "health_potion",
                "mana_potion",
                "ice_cold_milk",
                "gold_dust",
                "herbs",
                "crystal_shard",
                "magic_ring",
                "dwarven_ale",
                "mystic_amulet",
            ]

print(calculate_total(items_purchased, pinned_list))
