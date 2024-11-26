def does_attack_hit(attack_roll, armor_class):
    return (attack_roll != 1 and attack_roll >= armor_class) or (attack_roll == 20)

test = does_attack_hit(17, 18)
print(test)