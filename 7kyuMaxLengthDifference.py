def mxdiflg_v1(a1, a2):
    list_len1 = []
    list_len2 = []
    if not bool(a1) or not bool(a2):
        return -1
    for item1 in a1:
        list_len1.append(len(item1))
    for item2 in a2:
        list_len2.append(len(item2))
    max_value_a1 = max(list_len1)
    max_value_a2 = max(list_len2)
    min_value_a1 = min(list_len1)
    min_value_a2 = min(list_len2)
    print(f"max a1, a2 is {max_value_a1}, {max_value_a2}")
    print(f"min a1, a2 is {min_value_a1}, {min_value_a2}")
    output = []
    print(f"{abs(max_value_a1-max_value_a2)},{abs(max_value_a1-min_value_a2)},{abs(min_value_a1-max_value_a2)},{abs(min_value_a1-min_value_a2)}")
    output.append(abs(max_value_a1-max_value_a2))
    output.append(abs(max_value_a1-min_value_a2))
    output.append(abs(min_value_a1-max_value_a2))
    output.append(abs(min_value_a1-min_value_a2))
    output.sort()
    return output[-1]


def mxdiflg(a1, a2):
    if a1 and a2:
        return max(abs(len(max(a1, key=len)) - len(min(a2, key=len))), abs(len(max(a2, key=len)) - len(min(a1, key=len))))
    else:
        return -1

list1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
list2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

ans = mxdiflg(list1, list2)
print(f"ans = {ans}")




