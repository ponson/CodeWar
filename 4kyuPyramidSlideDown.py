import functools
import time
cur_max = 0


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def sum_and_compare(data, axis0, axis1, root, length):
    global cur_max

    left_sum = data[axis0+1][axis1] + root
    right_sum = data[axis0+1][axis1+1] + root

    row_maxs = []
    for i in range(axis0+1, axis0+length):
        row_maxs.append(max(data[i][axis1: axis1+i-axis0+1]))

    if cur_max >= sum(row_maxs) + root:
        return 

    if length == 2:
        cur_max = max(left_sum, right_sum) 
        return 
    else:
        sum_and_compare(data, axis0+1, axis1, left_sum, length-1)
        sum_and_compare(data, axis0+1, axis1+1, right_sum, length-1)
        return
    
@timer
def longest_slide_down1(pyramid):
    global cur_max

    pyramid_len = len(pyramid)
    cur_max = pyramid[0][0]
    sum_and_compare(pyramid, 0, 0, pyramid[0][0], pyramid_len)

    return cur_max

@timer
def longest_slide_down(pyramid):
    row = pyramid.pop()
    while pyramid:
        up_row = pyramid.pop()
        row = [up_row[i] + max(row[i], row[i+1]) for i in range(len(up_row))]

    return row.pop()

data = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]


data1 = [
    [3],
    [7, 4],
    [2, 4, 8],
    [8, 5, 9, 3],
]
print(longest_slide_down(data))