import functools
import time
# import math
import copy
import itertools as itl
import decimal


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

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


def permu_counts(word):
    c_set = set(word)
    c_count_dict = {c: word.count(c) for c in c_set}
    pcount = factorial(len(word))
    divider = 1
    for value in c_count_dict.values():
        divider *= factorial(value)
        
    # decimalP = decimal.Decimal()
    # print(f"pcount b divide= {pcount}")
    pcount /= decimal.Decimal(divider)
    # print(f"Decimal p= {}")
    # print(f"divider = {divider}")
    # print(f"pcount after divide = {pcount}")
    return int(pcount)


# @timer
def listPosition(word):
    sorted_l = sorted(word)
    idx, total = 0, 0

    wl = len(word)
    while (idx < wl and word[idx] == sorted_l[idx]):
        idx += 1

    if idx == wl:
        total = 1
    else:
        sorted_idx = sorted_l.index(word[idx])
        diff_len = sorted_idx - idx
        sorted_l = sorted_l[idx:]
        front_partial = sorted_l[:diff_len]
        for first_c in set(front_partial):
            dup_sorted_l = copy.deepcopy(sorted_l)
            dup_sorted_l.remove(first_c)
            total += permu_counts(''.join(dup_sorted_l))
            
        total += listPosition(word[idx+1:])

    return total

@timer
def listPosition0(word):
    p = itl.permutations(word)

    l = []
    for s in p:
        l.append(''.join(s))

    # print(f"Permutation count is {len(l)}")

    l = sorted(set(l))
    print(f"Acutual Permutation count is {len(l)}")
    # print(l)

    return l.index(word) + 1

@timer
def timer_listPosition(word):
    return listPosition(word)



# print(listPosition('THISISABOOK')) #2
# print(listPosition0('THISISABOOK')) #2

print(listPosition('A')) #1
print(listPosition('ABAB')) #2
print(listPosition('AAAB')) #1
print(listPosition('BAAA')) #4
print(listPosition('QUESTION')) #24572
print(listPosition('BOOKKEEPER')) #10743
print(listPosition('THISISABOOK')) #4645383

# 718393983731145681789 should equal 
# 718393983731145698173

# 24952064910166592320048 should equal 
# 24952064910166594089520

print(listPosition('IMMUNOELECTROPHORETICALLY')) #718393983731145698173
print(listPosition('YFPMITNTQHALRBSPFTZOKKIOF')) #24952064910166594089520
# print(int(listPosition('IMMUNOELECTROPHORETICALLY'))) #718393983731145698173
# print(int(listPosition('YFPMITNTQHALRBSPFTZOKKIOF'))) #24952064910166594089520