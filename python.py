sword_damage = 10
player_health = 100
health_after_attack = player_health - sword_damage

print(f"Lollilfred's health is: {player_health}")
print(f"Lollilfred is hit by a sword for {sword_damage} damage...")
print(f"Lollilfred's health is now: {health_after_attack}")

quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

print(f"{quest_start}")
print(f"{quest_middle}")
print(f"{quest_end} {space} {quest_objective}")

game_one_score = 97
game_two_score = 9
game_three_score = 106
game_four_score = 105
game_five_score = 96
game_six_score = 93
game_seven_score = 104

# Don't touch above this line

average_score = (game_one_score + game_two_score + game_three_score + game_four_score + game_five_score + game_six_score + game_seven_score) / 7
print(round (average_score))

# Functions
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

radius = 5
area = area_of_circle(radius)
print(area)

# Function

def knowing_myself(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro

my_name = "aadil"
my_age = "22"
my_height = "180"
my_weight = "80"

result = knowing_myself(my_name, my_age, my_height, my_weight)
print(result)


# def averageNumbers(numbers):
#     total = 0
#     for number in numbers:
#         print(len(numbers))
#         total += sum(number)
#     average = total / len(numbers)
#     return average

# my_numbers = [10, 30, 5, 25, 40]

# total_average = averageNumbers(my_numbers)
# print(f"the total average is {total_average}")

def fullHealth(h , a):
    full_health = h + a
    print (f"the player now has {full_health} health")
    return full_health

health = 10
armor = 5
fullHealth(health, armor)

def get_names():
    names = ["aad", "daad", "baab", "lucy"]
    for name in names:
        x = name
    print(x)

get_names()