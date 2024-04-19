def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for num in range(1, 1001):
    if is_prime(num):
        primes.append(num)

print(primes)
