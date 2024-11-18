def total_xp(level, xp_to_add):
    current_level_xp = level * 100
    current_xp = current_level_xp + xp_to_add
    return current_xp

level = 6
xp_to_add = 50 

current_xp = total_xp(level, xp_to_add)
print(current_xp)