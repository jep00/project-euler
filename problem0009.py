#Problem 9
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def isNatural(x):
    if x > 0:
        if x % 1 == 0:
            return True
        else:
            return False
    else:
        return False

def triplet(a, b, c): #Whilst (4,3,5) would be a triplet, we will ignore it here
    if isNatural(a):
        if isNatural(b):
            if isNatural(c):
                if a < b:
                    if b < c:
                        if a**2 + b**2 == c**2:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
        

found = False #We haven't yet found the triple!
for a in range(1, 333): #a is between 1 and 1000/3 as a<b<c
    for b in range(a, 500): #b is between 2 and 1000/2 as a<b<c
        for c in range(b, 1000):
            if a + b + c == 1000:
                if triplet(a,b,c):
                    found = True
                    print("a = ", a)
                    print("b = ", b)
                    print("c = ", c)
                    break

print("abc = ", a*b*c)
