from collections import Counter
def find_it(seq):
    counts = Counter(seq)
    for key in counts:
        if counts[key] % 2 == 1:
            return key


print(find_it([0, 0, 1]))
print(find_it([0, 0, 1, 1, 1, 1, 2]))
print(find_it([0, 0, 1, 9, 9, 1, 3]))
