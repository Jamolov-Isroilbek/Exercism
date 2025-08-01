def commands(binary_str):
    code_actions = ['wink', 'double blink', 'close your eyes', 'jump']
    result = []
    
    for index, value in enumerate(reversed(binary_str)):
        if index == len(binary_str) - 1:
            continue
        if value == '1':
             result.append(code_actions[index])    

    return list(reversed(result)) if binary_str[0] == '1' else result