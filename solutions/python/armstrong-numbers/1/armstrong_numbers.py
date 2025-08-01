def is_armstrong_number(number):
    length = len(str(number))
    sum_of_powers = 0
    temp_num = number
    
    for _ in range(length):
        sum_of_powers += (number % 10) ** length
        number = number // 10

    return sum_of_powers == temp_num