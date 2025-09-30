m = int(input())
n = int(input())

primes = []

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):  # √x까지만 확인
        if x % i == 0:
            return False
    return True

for num in range(m, n + 1):
    if is_prime(num):
        primes.append(num)

if not primes:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
