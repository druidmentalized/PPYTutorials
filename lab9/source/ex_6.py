from sympy import isprime

def generate_primes():
    curr = 1
    while True:
        if isprime(curr):
            yield curr
        curr += 1

prime_gen = generate_primes()

for _ in range(40):
    print(next(prime_gen))