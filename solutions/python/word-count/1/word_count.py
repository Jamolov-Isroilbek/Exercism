def count_words(sentence):
    word_freq = dict()
    i = 0
    
    while i < len(sentence):
        word, i = extract_next_word(i, sentence)
        
        if word:
            word = "".join(word).lower()
            word_freq[word] = word_freq.get(word, 0) + 1
        else:
            i += 1

    return word_freq    


def extract_next_word(index, sentence):
    word = []
    
    while index < len(sentence) and is_word_char(index, sentence):
        ch = sentence[index]
        if ch == "'" and \
        (
            not word or index + 1 >= len(sentence) or 
            not sentence[index+1].isalnum()
        ):
            break
        word.append(ch)
        index += 1

    return (word, index)


def is_word_char(index, sentence):
    return sentence[index].isalnum() or sentence[index] == "'"