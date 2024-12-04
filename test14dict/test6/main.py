def merge(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        merged_dict[key] = dict1[key]
    for key in dict2:
        merged_dict[key] = dict2[key]

    return merged_dict


def total_score(score_dict):
    total_score = 0
    for key in score_dict:
        total_score += score_dict[key]  
        
        if total_score == 0:
            return 0
    return total_score


two_towers = {"Frodo": "One Ring", "Aragorn": "Narsil"}
rotk = {"Aragorn": "Andúril", "Gandalf": "Glamdring"}

score = {"first_quarter": 24, "second_quarter": 31}

print(total_score(score))
