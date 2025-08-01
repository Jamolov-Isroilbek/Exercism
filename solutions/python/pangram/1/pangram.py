def is_pangram(sentence):
    return len({i.lower() for i in sentence if i.isalpha()}) == 26