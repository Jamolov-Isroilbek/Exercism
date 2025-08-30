import re

class PhoneNumber:
    def __init__(self, number):
        self.number = self._format_number(number)
        self.area_code = self.number[:3]

    def _format_number(self, number: str) -> str:
        number = re.sub(r"[().+\- ]", "", number)

        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")
        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")
        if any(not c.isalnum() for c in number):
            raise ValueError("punctuations not permitted")
        if len(number) == 11 and number[0] != "1":
            raise ValueError("11 digits must start with 1")
        if len(number) == 11:
            number = number[1:] # removing the country code once we check its correctness
        if number[0] == "0":
            raise ValueError("area code cannot start with zero")
        if number[0] == "1":
            raise ValueError("area code cannot start with one")
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        return number

    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"