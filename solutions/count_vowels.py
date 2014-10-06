def count_vowels(str):
    
    counter = 0
    for letter in str.lower():
        if letter in ('aoeuiy'):
            counter += 1

    return counter
