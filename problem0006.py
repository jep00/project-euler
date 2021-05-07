#Problem 6
"""
The sum of squares of the first 10 natural numbers,
1**2 + 2**2 + 3**2 + ... + 10**2 = 385,
The square of the sum of the first 10 natural numbers,
(1+2+3+...+10)**2 = 3025,
Hence the difference is 2640. Find the difference between the sum of the
squares of the first one hundred natural numbers and the square of the sum.
"""

sumsquare = sum(i**2 for i in range(1, 101)) #101 as python doesn't use the last value
squaresum = (sum(j for j in range(1, 101)))**2
print(squaresum - sumsquare)

