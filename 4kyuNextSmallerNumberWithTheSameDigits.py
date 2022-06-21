def compare_if_need_change_first_pos(o_l, s_l):
    index = s_l.index(o_l[0])
    comp_idx = 1
    for i in range(len(o_l)):
        if i == index:
            continue
        elif s_l[i] == o_l[comp_idx]:
           comp_idx += 1
        elif s_l[i] < o_l[comp_idx]:
            return False
        else:
            return True
        if comp_idx == len(o_l):
            return True
    return True


def find_smaller_digit(ori_l, sorted_l, rels):
    if len(ori_l) == 0:
        return
    index = -1
    for i in range(len(ori_l)):
        if ori_l[i] == sorted_l[i]:
            index = i
        else:
            break
    # print(f"index={index}")
    if index != -1:
        rels.extend(sorted_l[:index + 1])
        ori_l = ori_l[index + 1:]
        sorted_l = sorted_l[index + 1:]
        find_smaller_digit(ori_l, sorted_l, rels)
    else:
        if len(ori_l) == 2:
            rels.extend(sorted_l)
        elif not compare_if_need_change_first_pos(ori_l, sorted_l):  # 最大位數要留著
            value = ori_l[0]
            rels.append(value)
            sorted_l.remove(value)
            ori_l.remove(value)
            find_smaller_digit(ori_l, sorted_l, rels)
        else:
            pos = sorted_l.index(ori_l[0])
            pos -= 1
            value = sorted_l[pos]
            rels.append(value)
            sorted_l.remove(value)
            ori_l.remove(value)
            sorted_l.reverse()
            rels.extend(sorted_l)


def find_smaller_digit_v1(ori_l, sorted_l, rels):
    if len(ori_l) == 0:
        return
    index = -1
    for i in range(len(ori_l)):
        if ori_l[i] == sorted_l[i]:
            index = i
        else:
            break
    # print(f"index={index}")
    if index != -1:
        rels.extend(sorted_l[:index+1])
        ori_l = ori_l[index + 1:]
        sorted_l = sorted_l[index + 1:]
        find_smaller_digit(ori_l, sorted_l, rels)
    else:
        if sorted_l[0] < ori_l[1]: #最大位數要留著
            value = ori_l[0]
            rels.append(value)
            sorted_l.remove(value)
            ori_l.remove(value)
            find_smaller_digit(ori_l, sorted_l, rels)
        elif sorted_l[0] == ori_l[1]:
            compare_if_need_change_first_pos(ori_l, sorted_l)
        else:
            pos = sorted_l.index(ori_l[0])
            pos -= 1
            value = sorted_l[pos]
            rels.append(value)
            sorted_l.remove(value)
            ori_l.remove(value)
            sorted_l.reverse()
            rels.extend(sorted_l)


def next_smaller(n):
    print(n)
    digits = list(str(n))
    print(digits)
    sorted_digits = digits.copy()
    sorted_digits.sort()
    print(sorted_digits)
    if digits == sorted_digits:
        return -1
    results = []
    find_smaller_digit(digits, sorted_digits, results)
    print(f"results={results}")

    if results[0] == '0' or results == list(str(n)):
        return -1
    else:
        return int("".join(results))


# print(next_smaller(1027))  #-1
print(next_smaller(315))  #153
print(next_smaller(1207))  #1072
print(next_smaller(59884848483559))  #59884848459853
print(next_smaller(907))  #790
print(next_smaller(531))  #513
print(next_smaller(135))  #-1
print(next_smaller(2071)) #2017
print(next_smaller(2171)) #2117
print(next_smaller(414))  #144
print(next_smaller(700))  #-1
print(next_smaller(7123456))  #6754321
print(next_smaller(123456798)) #123456789
print(next_smaller(123456789)) #-1
print(next_smaller(1234567908)) # 1234567890
