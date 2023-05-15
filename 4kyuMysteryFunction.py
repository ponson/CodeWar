
def dTable(tableLen, tableIdx):
    if tableLen <= 0:
        return ""
    size = 2**tableLen
    middle = size // 2
    if tableIdx > middle - 1:
        offset = tableIdx - middle
        return '1' + dTable(tableLen-1, middle - offset - 1)
    else:
        return '0' + dTable(tableLen-1, tableIdx)
# TODO 1 先拿到是幾個digits  T(?)


def mystery(n):
    print(f"bin n is: {str(bin(n))}")
    tLen = len(str(bin(n))) - 2
# TODO 2: recursive找出對應index的數值
    digitStr = dTable(tLen, n)
    print(digitStr)
    # return BitArray(bin='0' + digitStr).int
    return int(digitStr, 2)


def mystery_inv(n):
    print(f"bin n is: {str(bin(n))}")
    binstr = str(bin(n))[2:]
    exp = 0
    index = 0
    for i in binstr[::-1]: 
        if exp == 0: 
            if i == '1':
                index = 1
            else:
                index = 0
        else:
            if i == '1':
                index = 2**exp + 2**exp - index - 1
        exp += 1

    return index

def name_of_mystery():
    pass


print(mystery(8)) #12
print(mystery(19)) #26
# print(mystery_inv(26))
