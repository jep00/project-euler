# Problem 10
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

# We use Problem 7's prime list functions:


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


primeList = [2]  # Assign 2, the first Prime

i = 3
while i < 2000000:
    if isPrime(i):
        primeList.append(i)
        i = i + 2
    else:
        i = i + 2  # We can ignore even numbers

print(sum(primeList))
