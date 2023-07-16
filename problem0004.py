# Problem 4
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of
two 3-digit numbers.
"""


def palindrome(x):
    y = list(str(x))  # Writes the value as a list of its elements.
    if y == y[::-1]:  # [::-1] provides the reverse
        return True
    else:
        return False


soln = max(i * j for i in range(100, 1000) for j in range(i, 1000) if palindrome(i * j))
print(soln)
