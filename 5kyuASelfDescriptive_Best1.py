from itertools import count, islice
from PonsonModules.decorators import timer

def sequence():
    cnt = count(1) 
    print(f"cnt={cnt}")
    seq = sequence()
    while 1:
        yield next(cnt)
        n = next(seq)
        print(f"n is={n}")
        yield from islice(cnt, n-1)
        yield n

for i in islice(sequence(), 100000):
    print(f"ans={i}")

# a112382 = list(islice(sequence(), 100000)).__getitem__


# print(type(a112382))
# print(a112382(10000))
