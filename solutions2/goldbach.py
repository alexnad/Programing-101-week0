from is_prime import is_prime
from prime_factorization import next_prime


def goldbach(n):
    result = []
    prime_addend = 2
    while prime_addend <= n/2:
        if is_prime(n - prime_addend):
            result.append((prime_addend, n - prime_addend))
        prime_addend = next_prime(prime_addend)

    return result
