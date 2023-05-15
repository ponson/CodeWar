import functools
import time
import random


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer

def isPrime_millerRabin(num):
    # n-1 => 2^s * d
    s = 0
    d = num - 1
    while d % 2 == 0:
        s += 1
        d = d >> 1

    #do 10 tests
    for i in range(0, 10):
        a = random.randint(2, num - 1)
        result = isPossiblePrime(num, a, s, d)
        if not result:
            return False

    return True


def isPossiblePrime(num, a, s, d):
    #pow(a, d, num) = a^d % num
    x = pow(a, d, num)
    if x == 1 or x == num -1:
        return True

    for i in range(0, s-1):
        x = (x * x) % num
        if x == num - 1:
            return True

    return False


# @timer
def get_prime_list(n):
    pl = [2]
    for i in range(3, n):
        if (isPrime_millerRabin(i)):
            pl.append(i)

    return pl

@timer
def prime_factors(n):
#TODO 1: Get Prime list
    prime_items = get_prime_list(n)
    # print(f"Prime list: {prime_items}")

#TODO 2: divide prime counts to dictionary
    result = {}   
    for i, v in enumerate(prime_items, 2): 
        if v == 0 or n % i > 0:
            continue
        result[i] = 1
        n = n // i
        while (n % i == 0):
            result[i] += 1
            n = n // i

    # print(f"result={result}")
    if len(result) == 0:
        return '(' + str(n) + ')'

#TODO 3: transform to a string
    rStr = ''
    for k, v in result.items():
        if v > 1:
            rStr += '(' + str(k) + '**' + str(v) + ')'
        else:
            rStr += '(' + str(k) + ')'

    return rStr




print(prime_factors(1819572902))
# print(prime_factors(21))
# print(prime_factors(2100000))
print("The end.")
# print(prime_factors(7775460))# "(2**2)(3**3)(5)(7)(11**2)(17)"
# print(prime_factors(7919))# "(7919)"
