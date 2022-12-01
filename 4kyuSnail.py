def snail(snail_map):
    output = []
    loops = []
    n = len(snail_map)
    if n == 1 and sum(snail_map[0]) == 0:
        return output
    loops.append(n)
    for i in range(n-1, 1, -1):
        loops.append(i)
        loops.append(i)
    last = n*n - sum(loops)
    if last == 2:
        loops.append(1)
        loops.append(1)
    else:
        loops.append(last)

    x, y = -1, 0
    dx, dy = 1, 0
    for j in loops:
        for k in range(j):
            x += dx
            y += dy
            output.append(snail_map[y][x])
        dx, dy = -dy, dx

    return output

    


smap = [[1,2],
        [7,6]]


smap1 = [[1,2,3],
        [8,9,4],
        [7,6,5]]

smap2 = [[1,2,3, 10],
        [8, 9,4, 11],
        [13, 14, 15, 16],
        [7,6,5, 12]]

smap0 = [[]]
print(snail(smap0))
print(snail(smap))
print(snail(smap1))
print(snail(smap2))