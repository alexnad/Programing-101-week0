from is_prime import is_prime

def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num
        

def factorise(num, prime):
    arr = [num, prime, 0]
    
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

    return factorised

print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))