def find_missing_ids(first_ids, second_ids):
    set_not_present = set()
    list_not_present = []

    for id in first_ids:
        if id not in second_ids:
            set_not_present.add(id)
    list_not_present = list(set_not_present)
    return list_not_present

first_ids = []
second_ids = []
print(find_missing_ids(first_ids, second_ids))

