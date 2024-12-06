def count_vowels(text):
    vowel_count = 0
    unique_vowels = set()
    for letter in text:
        if letter in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            vowel_count += 1
            unique_vowels.add(letter)
    return vowel_count, unique_vowels



text = "Did someone say Thunderfury, Blessed Blade of the Windseeker?"
print(count_vowels(text))
