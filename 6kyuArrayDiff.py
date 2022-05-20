def array_diff_v1(a, b):
    for value in b:
        while value in a:
            a.remove(value)
    return a


def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff([1, 2, 3], [2]))
print(array_diff([1, 2, 1, 2, 3], [1, 2]))
print(array_diff([1, 2, 3], [1, 2, 3]))
