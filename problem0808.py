## Problem 808 - Reversible Prime Squares

''' The Problem:

Both 169 and 961 are the square of a prime. 169 is the reverse of 961.

We call a number a reversible prime square if:

    It is not a palindrome, and
    It is the square of a prime, and
    Its reverse is also the square of a prime.

169 and 961 are not palindromes, so both are reversible prime squares.

Find the sum of the first 50 reversible prime squares.

'''
import math

# Helper Functions
def is_palindrome(x: int) -> bool:
    ''' Takes input integer x and returns True if palindrome, else False '''
    y = list(str(x)) #Writes the value as a list of its elements.
    if y == y[::-1]: #[::-1] provides the reverse
        return True
    else: 
        return False

def is_prime(x: int) -> bool:
    ''' Takes input integer x and returns True if prime number, else False '''
    if x == 2:
        return True
    elif x == 1:
        return False
    else:
        for i in (2, int(math.sqrt(x))+1):
            if x % i == 0: # If x modulo i = 0, ie. i is a factor of x
                return False
                break
        return True

def check_reverse_of_squared_prime(x: int) -> bool:
    ''' Takes an input integer x and returns True if the reverse is the square of a prime value '''
    y = list(str(x))
    y = int(''.join(y[::-1]))

    root_y = math.sqrt(y)
    if is_prime(root_y) and int(root_y)==float(root_y):
        return True
    else:
        return False

## Below isn't the most efficient way to run this, but I want to 
## test batch running a function until a critera is reached (in this case
## the length of accepted values reaches a certain value)

# Initialisation
accepted_values = []
offset=1
batch_size = 500

# Batch Run function
def run_batch(accepted_values, offset, batch_size):

    square_of_primes = [
        i**2 for i in range(offset,offset+batch_size) if is_prime(i) and not is_palindrome(i**2)
    ]
    accepted_values_temp = [
        x for x in square_of_primes if check_reverse_of_squared_prime(x)
    ]
    accepted_values += accepted_values_temp

    offset = offset+batch_size

    return accepted_values, offset

counter=1
while len(accepted_values)<50:
    accepted_values, offset = run_batch(
        accepted_values=accepted_values, offset=offset, batch_size=batch_size
    )
    counter+=1
print(f'- fifty accepted values found in {counter} batches of {batch_size} -')
print(f'- ** sum of first fifty reversible primes = {sum(accepted_values)} ** -')
print(f'- values: {accepted_values}')