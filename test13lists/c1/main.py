def smelt_ore(inventory):
    if ("Iron Ore" in inventory) or ("Iron Bar" in inventory):
        if "Iron Ore" in inventory:
            inventory[1] = "Iron Ore"
            inventory[1] = "Iron Bar"
        else: 
            inventory[1] = "Iron Bar"

    return inventory

test = ["Iron Ore", "Deadie"]
print(smelt_ore(test))