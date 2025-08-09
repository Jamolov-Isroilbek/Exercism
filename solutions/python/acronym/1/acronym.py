def abbreviate(words):
    acronym = []
    is_first_letter = True 
    
    for ch in words:
        if ch.isalpha() and is_first_letter:
            acronym.append(ch)
            is_first_letter = False
        elif ch in ["-", " "]:
            is_first_letter = True    

    return "".join(acronym).upper()