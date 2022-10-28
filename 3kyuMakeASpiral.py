def handle_one_direction(side, cur_x, cur_y, maps, depth):
#Right
    if side == 0: 
        # Has touched the edge. End.
        if cur_y >= depth - 3:
            return [False, cur_x, cur_y, side]
        
        # Check the first met whick value is 1
        for j in range(cur_y+1, depth):
            if maps[cur_x][j] == 1:
                break
        # All 0 case
        if j == depth-1 and maps[cur_x][j] == 0:
            for jj in range(cur_y+1, depth):
                maps[cur_x][jj] = 1
            cur_y = jj
            cont = True
        # Can move more 
        elif j >= cur_y + 2:
            if maps[cur_x][j] == 1:
                j -= 1
            for jj in range(cur_y+1, j):
                maps[cur_x][jj] = 1

            cur_y = jj
            cont = True
        # No more space. End
        else:
            cont = False
#Down
    elif side == 1: 
        # Has touched the edge. End.
        if cur_x >= depth - 3:
            return [False, cur_x, cur_y, side]

        # Check the first met whick value is 1
        for i in range(cur_x+1, depth):
            if maps[i][cur_y] == 1:
                break

        # All 0 case
        if i == depth-1 and maps[i][cur_y] == 0:
            for ii in range(cur_x+1, depth):
                maps[ii][cur_y] = 1
                
            cur_x = ii 
            cont = True
        # Can move more 
        elif i >= cur_x + 2:
            if maps[i][cur_y] == 1:
                i -= 1
            for ii in range(cur_x+1, i):
                maps[ii][cur_y] = 1

            cur_x = ii 
            cont = True
        # No more space. End
        else:
            cont = False
#Left
    elif side == 2: 
        # Has touched the edge. End.
        if cur_y <= 2:
            return [False, cur_x, cur_y, side]
        
        # Check the first met whick value is 1
        for j in range(cur_y-1, -1, -1):
            if maps[cur_x][j] == 1:
                break

        # All 0 case
        if j == 0 and maps[cur_x][j] == 0:
            for jj in range(cur_y-1, -1, -1):
                maps[cur_x][jj] = 1
                
            cur_y = jj
            cont = True
        # Can move more 
        elif j <= cur_y - 2:
            if maps[cur_x][j] == 1:
                j += 1
            for jj in range(cur_y-1, j, -1):
                maps[cur_x][jj] = 1

            cur_y = jj
            cont = True
        # No more space. End
        else:
            cont = False
#Up
    elif side == 3: 
        # Has touched the edge. End.
        if cur_x <= 2:
            return [False, cur_x, cur_y, side]
        
        # Check the first met whick value is 1
        for i in range(cur_x-1, -1, -1):
            if maps[i][cur_y] == 1:
                break

        # All 0 case, may never happen
        if i == 0 and maps[i][cur_y] == 0:
            for ii in range(cur_x-1, -1, -1):
                maps[ii][cur_y] = 1
                
            cur_x = ii 
            cont = True
        # Can move more 
        elif i <= cur_x - 2:
            if maps[i][cur_y] == 1:
                i += 1
            for ii in range(cur_x-1, i, -1):
                maps[ii][cur_y] = 1

            cur_x = ii 
            cont = True
        # No more space. End
        else:
            cont = False
   
    return [cont, cur_x, cur_y, (side + 1) % 4]
    
def spiralize(size):
    # Make a snake
    # spiral = [[0] *size] * size
    # spiral = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    spiral = []
    for i in range(size):
        line = []
        for j in range(size):
            line.append(0)
        spiral.append(line)

    spiral[0][0] = 1
    # print(f"spiral={spiral}")
    # print(f"spiral[0]={spiral[0]}")
    # print(f"spiral[0][0]={spiral[0][0]}")
    x = 0
    y = 0
    next_try = True
    direction = 0  #Right 
    while next_try:
        re_list = handle_one_direction(direction, x, y, spiral, size)
        next_try = re_list[0]
        x = re_list[1] 
        y = re_list[2]
        direction = re_list[3]
        # print(re_list)

    return spiral

print(spiralize(8))