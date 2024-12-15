def join_strings(strings):
    joined_string = ""
    joined_string_with_comma = ""

    for i in range(len(strings)):
        joined_string += strings[i]

        if i < len(strings) - 1:
            joined_string_with_comma += strings[i] + ","
        else:
            joined_string_with_comma += strings[i]

    return joined_string_with_comma
    
print(join_strings(["hello", "my", "man"]))
