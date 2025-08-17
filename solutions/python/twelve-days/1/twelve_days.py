def recite(start_verse, end_verse):
    days = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    gifts = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "a Partridge in a Pear Tree."
    ]

    result = []

    for i in range(start_verse, end_verse + 1):
        first_verse = f"On the {days[i]} day of Christmas my true love gave to me: "
        verse = []
        verse.append(first_verse)
        verse += gifts[-i:]
        verse[-1] = "and " + verse[-1] if i > 1 else verse[-1]
        verse = "".join(verse)
        
        result.append(verse)
    
    return result