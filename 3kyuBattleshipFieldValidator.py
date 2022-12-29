import copy


FIELD_SIZE = (10, 10)
battleField0 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


battleField1 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

battleField = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# 0: not checked, 1: checked, F: ship body has 'F'ound
cleanCheckedField = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


ships_size = {4: 'battleship', 3: 'Cruiser', 2: 'Destroyer', 1: 'Submarine'}
# ships_size = {'battleship': 4, 'Cruiser': 3, 'Destroyer': 2, 'Submarine': 1}
cleanShipsQuantity = {'battleship': 1, 'Cruiser': 2,
                  'Destroyer': 3, 'Submarine': 4}

EDGE_HEAD = 'head'
EDGE_BODY = 'body'
EDGE_TAIL = 'tail'
EDGE_SUBM = 'atom'


def check_empty_pos(field, entries):
    for r, c in entries:
        if 0 <= r < 10 and 0 <= c < 10 and field[r][c] == 1:
            return False
    return True


def check_edge(check_field, checkType, direction, cur_r, cur_c):
    if checkType == EDGE_HEAD:
        if direction == 'Right':
            check_list = [(cur_r-1, cur_c-1), (cur_r, cur_c-1),
                          (cur_r+1, cur_c-1), (cur_r-1, cur_c), (cur_r+1, cur_c)]
        else:
            check_list = [(cur_r-1, cur_c-1), (cur_r, cur_c-1),
                          (cur_r-1, cur_c), (cur_r-1, cur_c+1), (cur_r, cur_c+1)]
 # Down
    elif checkType == EDGE_BODY:
        if direction == 'Right':
            check_list = [(cur_r-1, cur_c), (cur_r+1, cur_c)]
        else:
            check_list = [(cur_r, cur_c-1), (cur_r, cur_c+1)]
    elif checkType == EDGE_TAIL:
        if direction == 'Right':
            check_list = [(cur_r-1, cur_c), (cur_r+1, cur_c),
                          (cur_r-1, cur_c+1), (cur_r, cur_c+1), (cur_r+1, cur_c+1)]
        else:
            check_list = [(cur_r, cur_c-1), (cur_r, cur_c+1),
                          (cur_r+1, cur_c-1), (cur_r+1, cur_c), (cur_r+1, cur_c+1)]
    elif checkType == EDGE_SUBM:
        check_list = [(cur_r-1, cur_c-1), (cur_r, cur_c-1), (cur_r+1, cur_c-1), (cur_r-1, cur_c),
                      (cur_r+1, cur_c), (cur_r-1, cur_c+1), (cur_r, cur_c+1), (cur_r+1, cur_c+1)]

    return check_empty_pos(check_field, check_list)


def check_direction(check_field, check_r, check_c):
    if check_c == FIELD_SIZE[1] - 1:
        dir_right = 0
    else:
        dir_right = check_field[check_r][check_c+1]

    if check_r == FIELD_SIZE[0] - 1:
        dir_down = 0
    else:
        dir_down = check_field[check_r+1][check_c]

    # Find both all have ship body! Wrong!
    if dir_right and dir_down:
        return 'Fail'
    elif dir_right:
        return 'Right'
    elif dir_down:
        return 'Down'
    else:
        if check_edge(check_field, EDGE_SUBM, 0, check_r, check_c):
            return 'Submarine'
        else:
            return 'Fail'


def check_ship(b_field, c_field, direction, r, c):
    if check_edge(b_field, EDGE_HEAD, direction, r, c) == False:
        return 0, False

    dr, dc = 0, 0
    if direction == 'Right':
        dc = 1
    else:
        dr = 1

    r += dr
    c += dc

    ship_len = 1
    while (r < 10 and c < 10 and b_field[r][c] == 1):
        if check_edge(b_field, EDGE_BODY, direction, r, c) == False:
            return 0, False
        ship_len += 1
        c_field[r][c] = 'F'
        r += dr
        c += dc

    if ship_len > 1:
        r -= dr
        c -= dc
        if check_edge(b_field, EDGE_TAIL, direction, r, c) == False:
            return 0, False
        return ship_len, True
    else:
        return 1, True 



def record_ship(quantities, shape):
    if quantities[shape] == 0:
        return False
    else:
        quantities[shape] -= 1
        return True


def quantity_check(quantities):
    for q in quantities.values():
        if q:
            return False

    return True

def validate_battlefield(field):
    checkedField = copy.deepcopy(cleanCheckedField)
    ships_quantity = copy.deepcopy(cleanShipsQuantity)
    for row in range(10):
        for col in range(10):
            if checkedField[row][col] == 0:
                checkedField[row][col] = 1
                if field[row][col] == 1:
                    checkedField[row][col] = 'F'
                    dir_result = check_direction(field, row, col)
                    if dir_result == 'Fail':
                        return False
                    elif dir_result == 'Submarine':
                        if record_ship(ships_quantity, 'Submarine') == False:
                            return False
                    else:
                        ship_len, result = check_ship(field, checkedField, dir_result, row, col)
                        if result == False:
                            return False
                        try:
                            if record_ship(ships_quantity, ships_size[ship_len]) == False:
                                return False
                        except KeyError:
                            return False

    return quantity_check(ships_quantity)

print(validate_battlefield(battleField))