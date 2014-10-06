CONSONANTS = 'bcdfghjklmnpqrstvwxz'

def count_consonants(str):
    counter = 0
    for letter in str.lower():
        if letter in CONSONANTS:
            counter += 1

    return counter
