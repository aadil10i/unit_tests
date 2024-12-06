def remove_duplicates(spells):
    new_spell = set()
    new_spell_list = []
    for spell in spells:
        new_spell.add(spell)
        new_spell_list = list(new_spell)

    return new_spell_list

spells =         [
            "fireball",
            "eldritch blast",
            "fireball",
            "eldritch blast",
            "chill touch",
            "eldritch blast",
            "chill touch",
            "chill touch",
            "fireball",
            "fireball",
            "shocking grasp",
            "fireball",
            "fireball",
        ]

print(remove_duplicates(spells))
