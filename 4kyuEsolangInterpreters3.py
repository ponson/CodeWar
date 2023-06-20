def interpreter(code, iterations, width, height):
    mm = [[0] * width for _ in range(height)]
    codeIdx = rowIdx = colIdx = loop = 0
    #loop 可取代skip, 當loop != 0時，就相當於skip = 1
    validChars = 'news*[]'
    code = ''.join(c for c in code if c in validChars)
    while iterations and codeIdx < len(code):
        if loop:
            if code[codeIdx] == '[': loop += 1
            elif code[codeIdx] == ']': loop -=1
            
        elif code[codeIdx] == 'n':  rowIdx = (rowIdx - 1) % height  #UP
        elif code[codeIdx] == 'e':  colIdx = (colIdx + 1) % width   #RIGHT
        elif code[codeIdx] == 'w':  colIdx = (colIdx - 1) % width   #LEFT
        elif code[codeIdx] == 's':  rowIdx = (rowIdx + 1) % height  #DOWN
        elif code[codeIdx] == '*':  mm[rowIdx][colIdx] ^= 1         #Reverse
        elif code[codeIdx] == '[' and mm[rowIdx][colIdx] == 0: loop += 1
        elif code[codeIdx] == ']' and mm[rowIdx][colIdx] != 0: loop -= 1

        codeIdx += 1 if loop >= 0 else loop // abs(loop)
        iterations -= 1 if not loop else 0

    result = '\\r\\n'.join(''.join(str(n) for n in row) for row in mm)

    # return result
    print(result)

def test(width, height):
    mm = [[0] * width] * height
    (mm[0])[2] = 1
    print(mm[0][2])
    print(mm[0])
    print(len(mm))
    return


# test(6,9)
interpreter("*[s[e]*]", 23, 5, 5)
# '11000\r\n10000\r\n10000\r\n10000\r\n10000'
# interpreter("*[es*]", 37, 5, 6)
# interpreter("*[s[e]*]", 9, 5, 5)
# '10000\r\n10000\r\n10000\r\n00000\r\n00000'
# interpreter("*[es*]", 5, 5, 6)
# '10000\r\n01000\r\n00000\r\n00000\r\n00000\r\n00000'
# "000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000"
# interpreter("o*e*eq*reqrqp*ppooqqeaqqsr*yqaooqqqfqarppppfffpppppygesfffffffffu*wrs*agwpffffst*w*uqrw*qyaprrrrrw*nuiiiid???ii*n*ynyy??ayd*r:rq????qq::tqaq:y???ss:rqsr?s*qs:q*?qs*tr??qst?q*r", 7, 6, 9)
# '111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000'
# interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9)
# "000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000"
# interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9)
# # "111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000"
# interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9)
# # "111100\r\n000010\r\n000001\r\n000010\r\n000100\r\n000000\r\n000000\r\n000000\r\n000000"
# interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9)
# # "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000"
# interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9)
# # "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000"