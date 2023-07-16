"""
Project Euler -- Project  0030

Problem:

    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

        1634 = 1**4 + 6**4 + 3**4 + 4**4
        8208 = 8**4 + 2**4 + 0**4 + 8**4
        9474 = 9**4 + 4**4 + 7**4 + 4**4

    As 1 = 1**4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


"""


# Helper Functions
def split_value(x: int) -> list:
    """Takes input integer x, and splits into the consituent values"""
    l = [int(i) for i in str(x)]
    return l


def power_list(l: list, p: int) -> list:
    """Raises every value in a list to a specified power"""
    l = [v**p for v in l]
    return l


def valid_value_check(l: list, v: int) -> bool:
    """Checks if the sum of a list of integers l is equal to a value v"""
    if sum(l) == v:
        return True
    else:
        return False


# Execution Function
def solution():
    """
    Brute force method is used
    """
    accepted_values = []
    for i in range(10, 5 * 9**5 + 1):
        if valid_value_check(l=power_list(split_value(i), p=5), v=i):
            accepted_values.append(i)
        else:
            pass

    print(
        f"Accepted Values = {accepted_values}\nSum of these values = {sum(accepted_values)}"
    )


# Execution
solution()

# Output
"""
Accepted Values = [4150, 4151, 54748, 92727, 93084, 194979]
Sum of these values = 443839
"""
