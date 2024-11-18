def calculate_damage(*weapons):
    total_damage = sum(weapons)
    average_damage = total_damage / len(weapons)
    return total_damage, average_damage

my_sword = 3 
my_arrow = 5
my_spear = 2
my_dagger = 1
my_fireball = 4

result = calculate_damage(my_sword, my_arrow, my_spear, my_dagger, my_fireball)
print(result)