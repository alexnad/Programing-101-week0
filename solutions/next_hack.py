from palindromes import is_int_palindrom


def dec_to_bin(x):
    return int(bin(x)[2:])


def next_hack(n):
    num = n
    while True:
        num += 1
        if is_int_palindrom(dec_to_bin(num)):
            return num
