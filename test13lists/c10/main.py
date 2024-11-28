def filter_messages(messages):
    filtered_message = []
    words_removed_count = []

    for message in messages:
        words = message.split()
        non_bad_words = []
        words_removed = 0
        
        for word in words:
            if word == "dang":
                words_removed += 1
            else:
                non_bad_words.append(word)
            
        clean_message = " ".join(non_bad_words)
        filtered_message.append(clean_message)
        words_removed_count.append(words_removed) 

    return filtered_message, words_removed_count
    
the_messages = ["darn it", "this dang thing won't work", "lets fight one on one"]
filter_messages(the_messages)
