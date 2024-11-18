def take_magic_damage(health, resist, amp, spell_power):
    final_health = (health - (spell_power * amp)) + resist
    return final_health


my_health = 100
my_resist = 5
attacker_amp = 2 
attacker_spell_power = 20

final_health = take_magic_damage(my_health, my_resist, attacker_amp, attacker_spell_power )
print(final_health)