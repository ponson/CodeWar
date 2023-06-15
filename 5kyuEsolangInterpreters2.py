def getMatchedOne(code, curP, c):
    stack = 0
    l = len(code)
    if c == '[':
        curP += 1
        while curP < l:
            if code[curP] == '[':
                stack += 1
            elif code[curP] == ']':
                if stack == 0:
                    return curP
                else:
                    stack -= 1
            curP += 1
    elif c == ']':
        curP -= 1
        while curP >= 0:
            if code[curP] == ']':
                stack += 1
            elif code[curP] == '[':
                if stack == 0:
                    return curP
                else:
                    stack -= 1
            curP -= 1

    return curP


def nextP(code, curP, value):
    if value == 0 and code[curP] == '[':
        #TODO find next ']' position
        curP = getMatchedOne(code, curP, '[')
    elif value == 1 and code[curP] == ']':
        #TODO Goto the past '['position
        curP = getMatchedOne(code, curP, ']')
    else:
        curP += 1

    return curP


def interpreter(code, tape):
    taplist = list(map(int, tape))
    p, tIdx = 0, 0

    while p < len(code):
        if code[p] == '>':
            tIdx += 1
        elif code[p] == '<':
            tIdx -= 1
        elif code[p] == '*':
            taplist[tIdx] ^= 1
        if tIdx >= 0 and tIdx < len(taplist):
            p = nextP(code, p, taplist[tIdx])
        else:
            break

    return ''.join(map(str, taplist))


def interpreter2(code, tape):
    tape = list(map(int, tape))
    ptr = step = loop = 0

    while 0 <= ptr < len(tape) and step < len(code):
        command = code[step]

        if loop:
            if command == "[":
                loop += 1
            elif command == "]":
                loop -= 1

        elif command == ">":
            ptr += 1
        elif command == "<":
            ptr -= 1
        elif command == "*":
            tape[ptr] ^= 1
        elif command == "[" and tape[ptr] == 0:
            loop += 1
        elif command == "]" and tape[ptr] == 1:
            loop -= 1

        step += 1 if not loop else loop // abs(loop)

    return "".join(map(str, tape))

def test():
    step = 1
    loop = 2

    step += 10 if not loop else 5

    print(step)

 # Flips the leftmost cell of the tape
# print(interpreter("*", "00101100"))#, "10101100")
# # Flips the second and third cell of the tape
# print(interpreter(">*>*", "00101100"))#, "01001100")
# # Flips all the bits in the tape
# print(interpreter("*>*>*>*>*>*>*>*", "00101100"))#, "11010011")
# # Flips all the bits that are initialized to 0
# print(interpreter("*>*>>*>>>*>*", "00101100"))#, "11111111")
# # Goes somewhere to the right of the tape and then flips all bits that are initialized to 1, progressing leftwards through the tape
# print(interpreter(">>>>>*<*<<*", "00101100"))#, "00000000")


# print(interpreter("*>*>>>*>*>>>>>*>[>*]", "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"))
# print(interpreter("[[]*>*>*>]", "000"))  # , "000")
# print(interpreter("*>[[]*>]<*", "100"))  # , "100")
print(interpreter2("[*>[>*>]>]", "11001"))  # , "01100")
# print(interpreter("[>[*>*>*>]>]", "10110"))  # , "10101")
# test()
