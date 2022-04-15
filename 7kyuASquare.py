import math


def is_square_v1(n):

    if n < 0:
        return False

    for i in range(n+1):
        if i**2 == n:
            return True
        if i**2 > n:
            return False


def is_square(n):
    if n > -1:
        n_sqrt = math.sqrt(n)
        print(f"the sqrt {n} is {n_sqrt % 1}")
    return n > -1 and math.sqrt(n) % 1 == 0

print(is_square(-1))
print(is_square(0))
print(is_square(25))
print(is_square(26))
