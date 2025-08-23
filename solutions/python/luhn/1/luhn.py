class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self) -> bool:
        cleaned_num = self.card_num.replace(" ", "")
        
        if len(cleaned_num) <= 1 or not all(c.isdigit() for c in cleaned_num):
            return False

        digits = [int(c) for c in cleaned_num]
        
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            digits[i] = doubled - 9 if doubled > 9 else doubled
            
        return sum(digits) % 10 == 0