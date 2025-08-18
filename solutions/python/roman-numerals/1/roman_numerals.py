def roman(number):
    ROMAN_NUMERALS  = [
        (1000, "M"), 
        (900, "CM"), 
        (500, "D"), 
        (400, "CD"), 
        (100, "C"), 
        (90, "XC"), 
        (50, "L"), 
        (40, "XL"), 
        (10, "X"), 
        (9, "IX"), 
        (5, "V"), 
        (4, "IV"), 
        (1, "I")
    ]

    roman_result = []

    for value, roman_char in ROMAN_NUMERALS:
        while number >= value:
            roman_result.append(roman_char) 
            number -= value 

    return "".join(roman_result)