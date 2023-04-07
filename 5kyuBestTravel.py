import itertools
import bisect

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64,
      123, 2333, 144, 50, 132, 123, 34, 89]


def choose_best_sum(t, k, ls):
    sort_ls = sorted(ls)
    r = itertools.combinations(sort_ls, k)
    sum_r = []
    for i in r:
       sum_r.append(sum(i))

    if len(sum_r) == 0:
        return None

    sum_r = sorted(sum_r)
    index = bisect.bisect_left(sum_r, t)
    if index == len(sum_r):  #最大的sum都比t小
        return sum_r[index-1]
    elif index == 0 and sum_r[index] > t: #最小的sum都比t大
        return None
    else:
        if sum_r[index] == t:
            return t
        else:
            return sum_r[index-1]

print(choose_best_sum(230, 4, xs))