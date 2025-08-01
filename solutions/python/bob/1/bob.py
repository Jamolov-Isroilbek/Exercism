def response(hey_bob):
    def contains_letter(s):
        return any(char.isalpha() for char in s)

    hey_bob = hey_bob.strip()

    is_question = hey_bob.endswith('?')
    is_yelling = hey_bob.isupper() and contains_letter(hey_bob)

    if hey_bob == "":
        return "Fine. Be that way!"
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_question:
        return "Sure."
    if is_yelling:
        return "Whoa, chill out!"
    return "Whatever."

