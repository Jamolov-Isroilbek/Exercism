def is_valid(isbn):
    isbn = isbn.replace('-', '')
    isbn_sum, multiplier = 0, 10

    if len(isbn) != 10:
        return False
    
    for i in isbn:
        if not i.isdigit() and i != 'X':
            return False
        if i == 'X':
            if multiplier != 1:
                return False
            i = 10
        
        isbn_sum += int(i) * multiplier
        multiplier -= 1

    return isbn_sum % 11 == 0
        