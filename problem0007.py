# Problem 7
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


primeList = [2]  # Assign 2, the first Prime

i = 3
while len(primeList) < 10001:
    if isPrime(i):
        primeList.append(i)
        i = i + 1
    else:
        i = i + 1

print(primeList[-1])
