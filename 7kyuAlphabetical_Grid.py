
def grid(N):
    if N < 0:
        return None
    alphabetics = list("abcdefghijklmnopqrstuvwxyz")
    grid_str = ""
    for i in range(N):
        shift_idx = i
        for j in range(N):
            grid_str += alphabetics[(shift_idx + j) % 26]
            if j < N-1:
                grid_str += " "
        if i < N-1:
            grid_str += "\n"
    return grid_str


print(grid(30))