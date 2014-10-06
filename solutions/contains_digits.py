from contains_digit import contains_digit

def contains_digits(number, digits):
    for num in digits:
        if not contains_digit(number, num):
            return False
    return True
