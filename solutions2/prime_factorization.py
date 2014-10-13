from is_prime import is_prime

memory = {}
def memoize(func):
    def memoized(*args):
        if args in memory:
            return memory[args]
        result = func(*args)
        memory[args] = result
        return result
    return memoized

@memoize
def is_prime(n):
    for divisor in range(2,n//2+1):
        if n % divisor == 0:
            return False
    return True



def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num


def factorise(num, prime):
    arr = [num, prime,0]

    while arr[0] % prime == 0:
        arr[0] /= prime
        arr[2] += 1

    return arr


def prime_factorization(n):
    num = n
    factorised = []
    prime = 2

    while num > 1:
        arr = factorise(num, prime)
        if arr[2] > 0:
            num = arr[0]
            factorised.append(tuple(arr[1:]))
        prime = next_prime(prime)

    return factorised

print(prime_factorization(100042))