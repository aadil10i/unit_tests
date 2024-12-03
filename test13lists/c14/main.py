def validate_path(expected_path, character_path):
    character_name = character_path[0]
    correct_waypoint = 0

    for path in character_path:
        if path in expected_path:
            correct_waypoint += 1
        percentage = (correct_waypoint / len(expected_path)) * 100

    return character_name, percentage

expected_path = ["A", "B", "C", "D"]
character_path = ["Hero123", "A", "X", "C", "D"]
name, percent = validate_path(expected_path, character_path)
print(name, percent)
