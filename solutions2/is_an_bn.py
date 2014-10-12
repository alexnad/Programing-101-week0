def is_an_bn(word):

    if word == '':
        return True

    if len(word) % 2 == 1:
        return False

    middle = len(word)/2
    first_part = word[:middle]
    second_part = word[middle:]

    for a, b in zip(first_part, second_part):
        if a != 'a' or b != 'b':
            return False

    return True
