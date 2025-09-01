# Score categories.
# Change the values as you see fit.
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice, category):
    def is_straight(start_num):
        return set(dice) == set(range(start_num, start_num + 5))
        
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return dice.count(category) * category
    
    if category is FULL_HOUSE:
        if len(set(dice)) == 2:
            for i in set(dice):
                if dice.count(i) not in [2, 3]:
                    return 0
            return sum(dice)
        return 0
    
    if category is FOUR_OF_A_KIND:
        if len(set(dice)) <= 2:
            for i in set(dice):
                if dice.count(i) >= 4:
                    return 4 * i
        return 0
        
    if category is LITTLE_STRAIGHT:
        return 30 if is_straight(1) else 0
    
    if category is BIG_STRAIGHT:
        return 30 if is_straight(2) else 0
    
    if category is CHOICE:
        return sum(dice)
    
    if category is YACHT:
        return YACHT if len(set(dice)) == 1 else 0