def move_zeros(the_list):
    zero_count = the_list.count(0)

    for i in range(zero_count):
        the_list.remove(0)

    for j in range(zero_count):
        the_list.append(0)
    return the_list





print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))