def nth_floyd(n):
    sub_num = 1
    while n > sub_num:
        n = n - sub_num
        sub_num += 1
    return sub_num
