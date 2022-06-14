from decorators import timer

@timer
def remov_nb_v1(n):
    sum_n = sum(range(1, n+1))
    result = []
    for x in range(n, 0, -1):
        for y in range(x-1, 0, -1):
            compare = (x * y) - (sum_n - x - y)
            if compare < 0:
                break
            elif compare == 0:
                result.append((y, x))
                result.append((x, y))
            else:
                pass
    return result


@timer
def remov_nb(n):
    sum_n = sum(range(1, n + 1))
    result = []
    for i in range(n, 0, -1):
        j = (sum_n - i) / (i + 1)
        if j - int(j) == 0 and j <= n and j != i and (int(j), i) not in result:
            result.append((int(j), i))
            result.append((i, int(j)))
        else:
            pass
    result.sort()
    return result


def sort_list(ll):
    ll.sort()
    return ll


print(remov_nb(26))
print(remov_nb(100))
print(remov_nb(101))
print(remov_nb(1000))
print(remov_nb(10000))
# print(sort_list([2, 4, 1, 5, 3]))
# print(sort_list([(550320, 908566), (908566, 550320), (559756, 893250), (893250, 559756)]))
