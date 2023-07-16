"""Problem 263: An Engineer's Dream Come True

Consider the number 6. The divisors of 6 are 1, 2, 3, and 6.

Every number from 1 up to and including 6 can be written as a sum of distinct
divsors of 6:
    1 = 1; 2 = 2, 3 = 1+2, 4 = 1+3, 5 = 2+3, 6=6
A number n is called a practical number if every number from 1 up to and
including n can be expressed as a sum of distinct divisors of n.

A pair of consective prime numbers with a difference of six is called a 
sexy pair. The first sexy pair is (23, 29).

We may occasionally find a triple-pair, which means three consecutive sexy
prime pairs such that the second number of each pair is the first
member of the next pair.

We shall call a number n such that:
    - (n-9, n-3), (n-3, n+3), (n+3, n+9) form a triple-pair, and
    - the numbers n-8, n-4, n, n+4, and n+8 are all practical
an engineers' paradise.

Find the sum of the first four engineers' paradises.

https://projecteuler.net/problem=263
"""
import itertools


# Functions for testing for practicality:
def find_divisors(x: int) -> list[int]:
    """Finds the divisors of integer n and returns as a list."""
    divisors = [1, x]  # Every number is divisible by itself and 1.
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            divisors.append(i)
    # divisors.extend(i for i in range(2, x / 2) if x % i == 0)
    return divisors


def form_all_possible_values(values: list[int]) -> set:
    """
    Given a list of values, a set of all values that can be made with combinations
    of the list components will be returned.
    """
    possible_values = set()
    l = len(values)
    for i in range(1, l + 1):
        possible_values = possible_values | {
            sum(v) for v in list(itertools.combinations(values, i))
        }
    return possible_values


def is_practical(x: int) -> bool:
    """Function to determine whether or number a number n is practical."""
    divisors_of_x = find_divisors(x)
    sum_of_divisors = form_all_possible_values(divisors_of_x)
    return all(i in sum_of_divisors for i in range(1, x))


# Functions for testing for sexiness:
def is_prime(x: int) -> bool:
    """Function to assess if a number is a prime or not."""
    if x == 1:
        return False
    elif x in {2, 3}:
        return True
    else:
        for i in range(3, int(x**0.5) + 1):
            if x % i == 0:
                return False
    return True


def is_sexy(t: tuple[int, int]) -> bool:
    """For an inputted tuple, if both are prime, we return True; else False."""
    n_one, n_two = t[0], t[1]
    return is_prime(n_one) and is_prime(n_two)


def is_engineers_paradise(n: int) -> bool:
    """
    For a number to be an engineers paradise, we asses first if the numbers
    n-8, n-4, n, n+4, and n+8 are all practical, before checking if
    (n-9, n-3), (n-3, n+3), and (n+3, n+9) form a triple-pair. If any of the
    criteria are not satisfied, we return False. If all are satisfied, we
    return True.
    """
    check_for_practicality = [n - 8, n - 4, n, n + 4, n + 8]
    if not all(is_practical(i) for i in check_for_practicality):
        return False

    check_for_sexiness = [(n - 9, n - 3), (n - 3, n + 3), (n + 3, n + 9)]
    return all(is_sexy(j) for j in check_for_sexiness)


# Testing
assert is_prime(1) is False
assert is_prime(17) is True
assert is_prime(50) is False

assert is_practical(22) is False
assert is_practical(132) is True
assert is_practical(120) is True
# Found from: https://en.wikipedia.org/wiki/Practical_number

# Testing, based on knowledge from the question:
assert is_practical(6) is True
assert is_sexy((23, 29)) is True


def compute():
    engineers_paradises = []
    i = 23  # We know the first sexy pair is (23,29) so we can begin our count here.
    while len(engineers_paradises) < 4:
        if is_engineers_paradise(i):
            engineers_paradises.append(i)
            print(f"Engineer's Paradise found: {i}")
        i + 1

    print(
        f"""
    Found four Engineer's Paradises: {engineers_paradises}
    The sum of these values is {sum(engineers_paradises)}
    """
    )


# Execution:
def main():
    compute()


if __name__ == "__main__":
    main()
