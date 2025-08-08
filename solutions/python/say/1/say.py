numbers = {
        1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
        80: "eighty", 90: "ninety"
} 
    
scales = ["", "thousand", "million", "billion"]


def say(number):  
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
        
    if number == 0:
        return "zero"
        
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000

    result = []

    for i in range(len(chunks)):
        chunk = chunks[i]
        if chunk == 0:
            continue
        chunk_word = convert_chunk(chunk)
        scale = scales[i]
        if scale:
            result.append(f"{chunk_word} {scale}")
        else:
            result.append(chunk_word)

    return " ".join(reversed(result))

def convert_chunk(n):
    if n == 0:
        return ""

    parts = []
    if n >= 100:
        parts.append(numbers[n // 100] + " hundred")
        n %= 100
    if n >= 20:
        tenth = n // 10 * 10
        once = n % 10
        parts.append(numbers[tenth] + (f"-{numbers[once]}" if once != 0 else ""))
    elif n > 0:
        parts.append(numbers[n])

    return " ".join(parts)