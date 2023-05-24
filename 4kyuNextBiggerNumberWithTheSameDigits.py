def next_bigger(n):
    strn = list(str(n))
    i = j = len(strn) - 1
    while i > 0 and strn[i - 1] >= strn[i]:
        i -= 1
    if i <= 0:
        return -1
    while strn[j] <= strn[i - 1]:
        j -= 1
    strn[i - 1], strn[j] = strn[j], strn[i - 1]
    strn[i:] = reversed(strn[i:])
    return int(''.join(strn))
    


def next_smaller(n):
    s = list(str(n))
    i = j = len(s) - 1
    while i > 0 and s[i - 1] <= s[i]:
        i -= 1
    if i <= 0:
        return -1
    while s[j] >= s[i - 1]:
        j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = reversed(s[i:])
    if s[0] == '0':
        return -1
    return int(''.join(s))

def reverse_test(n):
    s = list(str(n))
    s = reversed(s)
    return int(''.join(s))


print(next_bigger(12)) #21
print(next_bigger(21)) #-1
print(next_bigger(513)) #531
print(next_bigger(2017)) #2071
print(next_bigger(414)) #441
print(next_bigger(144)) # 414


# print(next_smaller(21)) #12
# print(next_smaller(531)) #513
# print(next_smaller(2071)) #2017
# print(next_smaller(2534)) #2453

# print(reverse_test(123456))