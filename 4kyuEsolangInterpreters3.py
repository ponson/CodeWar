def interpreter(code, iterations, width, height):
    mm = [[0] * width for _ in range(height)]
    codeIdx, rowIdx, colIdx, loop, skip = 0, 0, 0, 0, 0
    validChars = 'news*[]'
    # print(f"code={code}")
    # print(f"iter={iterations}")
    # print(f"w={width}")
    # print(f"h={height}")
    while iterations and codeIdx < len(code):
        # check = code[codeIdx] in list(validChars) 
        # print(f"check={check}, codeIdx={codeIdx}")
        if code[codeIdx] in list(validChars):
            if code[codeIdx] == 'n' and skip == 0:  #UP
                rowIdx -= 1
                rowIdx %= height
                iterations -= 1
            elif code[codeIdx] == 'e' and skip == 0:  #RIGHT
                colIdx += 1
                colIdx %= width
                iterations -= 1
            elif code[codeIdx] == 'w' and skip == 0:  #LEFT
                colIdx -= 1
                colIdx %= width
                iterations -= 1
            elif code[codeIdx] == 's' and skip == 0:  #DOWN
                rowIdx += 1
                rowIdx %= height
                iterations -= 1
            elif code[codeIdx] == '*' and skip == 0:  #Reverse
                mm[rowIdx][colIdx] ^= 1
                iterations -= 1
            elif code[codeIdx] == '[':
                if skip > 0 and loop >= 0:
                    skip += 1
                if loop == -1:
                    loop += 1
                    skip = 0
                    iterations -= 1
                elif skip == 0:
                    if mm[rowIdx][colIdx] == 0:
                        skip = 1
                    iterations -= 1
                loop += 1
            elif code[codeIdx] == ']':
                if loop >= 0:
                    if skip > 0:
                        skip -= 1
                    else:
                        if mm[rowIdx][colIdx] == 1:
                            skip = 1
                            loop -= 1
                        else:
                            skip = 0
                loop -= 1

        codeIdx += 1 if loop >= 0 else loop // abs(loop)

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