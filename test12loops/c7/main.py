def meditate(mana, max_mana, energy, energy_potions):
    while mana < max_mana and (energy > 0 or energy_potions > 0):
        if energy > 0:
            mana = min(mana + 3, max_mana)
            energy - 1

        else:
            energy += 50
            energy_potions -= 1

    return mana, energy, energy_potions