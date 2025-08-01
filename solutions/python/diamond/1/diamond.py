def rows(letter):
    base = ord('A')
    n = ord(letter) - base
    result = []

    for i in range(2 * n + 1):
        char_index = i if i <= n else 2 * n - i
        char = chr(base + char_index)
        padding = ' ' * (n - char_index)
        
        if char_index == 0:
            row = f"{padding}{char}{padding}"
        else:
            middle = ' ' * (2 * char_index - 1)
            row = f"{padding}{char}{middle}{char}{padding}"
        
        result.append(row)

    return result