def double_string(string):
    final_sentence = ""
    for i in range(0, len(string)):
        sentence = string[i] * 2
        final_sentence += sentence
    return final_sentence

sentence = "LF3M BRD full clear"
print(double_string(sentence))
