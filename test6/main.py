def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score

score = 0
incremental = 100

final_score = update_player_score(score, incremental)
print(final_score)