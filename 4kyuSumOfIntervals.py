def merge_overlap(input, output):
    in_len = len(input)
    if in_len > 1:
        a, b = input[:2]
        a_begin, a_end = a
        b_begin, b_end = b
        if a_end >= b_begin:
            if a_end >= b_end:
                c = (a_begin, a_end)
            else:
                c = (a_begin, b_end)
            del input[:2]
            input.insert(0, c)
        else:
            output.append(a) 
            del input[0]
        merge_overlap(input, output)

    else:
        output.extend(input)

def sum_of_intervals(intervals):
#1: Sorting
    intervals.sort()
    # print(intervals)
#2: Merge
    merged_list = []
    merge_overlap(intervals, merged_list)
    # print(merged_list)
#3: Sum of Lengths
    total_len = 0
    for item in merged_list:
        total_len += item[1] - item[0]

    # print(total_len)

    return total_len


sum_of_intervals([(1, 5)])
sum_of_intervals([(1, 5), (6, 10)])
sum_of_intervals([(1, 5), (1, 5)])
sum_of_intervals([(1, 4), (7, 10), (3, 5)])
sum_of_intervals([(-1_000_000_000, 1_000_000_000)])
sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)])
