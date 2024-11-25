def calculate_experience_points(level):
    XP_Gained = 0
    for i in range(level):
        XP_Gained += i * 5
    return XP_Gained

result = calculate_experience_points(3) 
print(result)

