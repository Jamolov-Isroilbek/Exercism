def is_paired(input_string):
    brackets = []

    for ch in input_string:
        if ch in '({[':
            brackets.append(ch)
        elif ch in ')}]':
            if not brackets:
                return False
            if ( 
                ( ch == ')' and brackets[-1] == '(' ) or
                ( ch == '}' and brackets[-1] == '{' ) or
                ( ch == ']' and brackets[-1] == '[' )
            ):
                    brackets.pop()
            else:
                return False

    return brackets == []