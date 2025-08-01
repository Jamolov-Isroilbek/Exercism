def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    cnt_steps = 0

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
        cnt_steps += 1

    return cnt_steps