def get_hints(answer, guess):
    white = 0
    black = 0
    ans_list = []
    gus_list = []
    result = {}

    for ans_item, gus_item in zip(answer, guess):
        if ans_item == gus_item:
            black += 1
        else:
            gus_list.append(gus_item)
            ans_list.append(ans_item)

    for test_item in ans_list:
        if test_item in gus_list:
            white += 1
            gus_list.remove(test_item)


    result["black"] = black
    result["white"] = white

    return result


def test():
    the_list = [1, 1, 1, 2, 3, 4]
    the_list.remove(1)
    print(the_list)

print(get_hints([1, 2, 3, 4], [1, 2, 3, 4]))
print(get_hints([1, 2, 3, 4], [4, 3, 2, 1]))
print(get_hints([1, 2, 3, 4, 4, 3, 2, 1], [4, 3, 2, 1, 4, 4, 4, 4]))

test()