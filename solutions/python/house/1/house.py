verbs = ['belonged to', 'kept', 'woke', 'married', 'kissed', 'milked', 'tossed', 'worried', 'killed', 'ate', 'lay in']

lines = [
    'the horse and the hound and the horn',
    'the farmer sowing his corn',
    'the rooster that crowed in the morn',
    'the priest all shaven and shorn',
    'the man all tattered and torn',
    'the maiden all forlorn',
    'the cow with the crumpled horn',
    'the dog',
    'the cat',
    'the rat',
    'the malt',
    'the house that Jack built'
]

def recite(start_verse, end_verse):
    poems = []
    
    for i in range(start_verse, end_verse + 1):
        poems += repeat(i)
    
    return poems

def repeat(n):
    verses = []

    for i in range(n,  0, -1):
        if i != n:
            verse = f"that {verbs[-i]} {lines[-i]}"
        else:
            verse = f"This is {lines[-i]}"
        verses.append(verse)
            
    return [" ".join(verses) +"."]
            