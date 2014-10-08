from is_prime import is_prime


def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num


def factorise(num, prime):
    arr = [num, 0]

    while arr[0] % prime == 0:
        arr[0] /= prime
        arr[1] += 1

    return arr


def prime_factorization(n):
    num = n
    factorised = []
    prime = 2

    while num > 1:
        arr = factorise(num, prime)
        if arr[1] > 0:
            num = arr[0]
            factorised.append(tuple(arr[1:]))
        prime = next_prime(prime)

    return factorised
