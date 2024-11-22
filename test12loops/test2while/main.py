def regenerate(current_health, max_health, enemy_distance):
    new_current_health = current_health
    while (current_health < max_health) and (enemy_distance > 3):
        new_current_health += 1
        enemy_distance -= 2

    return new_current_health

print(regenerate(9, 10, 3))


# def regenerate(current_health, max_health, enemy_distance):

#     new_current_health = current_health
#     while True:
#         enemy_distance -= 2
#         if (current_health < max_health and enemy_distance > 3):
#             new_current_health += 1