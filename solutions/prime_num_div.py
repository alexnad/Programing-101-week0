from is_prime import is_prime

def prime_number_of_divisors(n):
    sum = 0
    for divisor in range(1,n+1):
        if n % divisor == 0:
            sum += 1
    return is_prime(sum)

