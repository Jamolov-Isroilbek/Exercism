def decode(string):
    result = []
    digits = ""
    
    for char in string:
        if char.isdigit():
            digits += char
        else:
            run_length = int(digits) if digits else 1
            result.append(char * run_length)
            digits = ""

    return "".join(result)


def encode(string):
    if len(string) <= 1:
        return string

    result = []
    run_length = 1

    for i in range(len(string)):
        if i < len(string) - 1 and string[i] == string[i+1]:
            run_length += 1
        else:
            if run_length > 1:
                result.append(str(run_length))
            result.append(string[i])
            run_length = 1
    
    return "".join(result)