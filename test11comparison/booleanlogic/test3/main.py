def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if (player_power == enemy_defense):
        evenly_matched = True
    elif (player_power > enemy_defense):
        advantage = True
    else:
        disadvantage = True
    # your code here
    
    return advantage, disadvantage, evenly_matched

test = combat_evaluation(150, 70)
print(test)

