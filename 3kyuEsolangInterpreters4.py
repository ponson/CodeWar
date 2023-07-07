def changeBitsToOutput(bits):
    result = ''
    while bits:
        bits, result = bits[8:], result + chr(int(''.join(str(c) for c in bits[:8][::-1]).rjust(8, '0'), 2))

    return result
    # strBits = ''.join(str(i) for i in bits[::-1])
    # print(f"strBits={strBits}")
    # if strBits:
    #     intBits = int(strBits, 2)
    #     result = intBits.to_bytes((intBits.bit_length()+7)//8, 'little').decode('unicode-escape', 'surrogatepass')
    #     return result if result else '\x00'
    # else:
    #     return ''

# while out:
#     out, s = out[8:], s + chr(int(''.join(str(c) for c in out[:8][::-1]).rjust(8, '0'), 2))
    # out = out[8:] 
    # s = s + chr(int(''.join(str(c) for c in out[:8][::-1]).rjust(8, '0'), 2))
def changeInputToBits(input):
    if input:
        result = ''
        for c in input:
            bitChar = bin(ord(c))[2:].rjust(8, '0')
            bitCharReverse = ''.join(x for x in bitChar[::-1])
            result += bitCharReverse
        return [int(x) for x in list(result)]
    else:
        return []


def boolfuck(code, input=""):
    code = "".join(c for c in code if c in "<>+,;[]")

    loop = codeIdx = inP = dP = 0
    outBits = []

    inBits = changeInputToBits(input)
    disk = {}

    while codeIdx < len(code):
        if loop:
            if code[codeIdx] == '[':
                loop += 1
            elif code[codeIdx] == ']':
                loop -= 1

        elif code[codeIdx] == '>':
            dP -= 1  # Move Right
        elif code[codeIdx] == '<':
            dP += 1  # Move Left
        elif code[codeIdx] == '+':
            disk[dP] = disk.get(dP, 0) ^ 1  # Flip 0/1
        elif code[codeIdx] == ',':  # Read a bit from input stream and store it under the pointer
            disk[dP] = inBits[inP] if inP < len(inBits) else 0
            inP += 1
        elif code[codeIdx] == ';':
            outBits.append(disk.get(dP, 0))  # output value
        elif code[codeIdx] == '[' and disk.get(dP, 0) == 0:
            loop += 1
        elif code[codeIdx] == ']' and disk.get(dP, 0) != 0:
            loop -= 1

        codeIdx += 1 if loop >= 0 else loop // abs(loop)

    return changeBitsToOutput(outBits)


def unicode_test(value):
    import unicodedata

    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f"value={value}, name={name}, value2={value2}")
    # print(f"yen sign= {unicodedata.lookup('YEN SIGN')}")


def unicode_test2(value):
    # cr = value.encode('unicode-escape')
    cr = value.encode('utf-8')
    print(cr)


def unicode_test3(value):
    unicode_character = "\u2612\u7688\u00C9\u00C9"
    print(unicode_character)


# changeBitsToOutput([0, 0, 0, 1, 0, 0, 1, 0])
# n = int('0110111101101100011011000110010101001000', 2)
# print(result)
# bchar = format(ord('H'), '08b')
# print(bchar)
# unicode_test('\u2603')
# unicode_test3('\n')
# changeInputToBits("H")
# print(boolfuck("", ""))
# ""
# print(boolfuck("<", ""))
# ""
# print(boolfuck(">", ""))
# ""
# print(boolfuck("+", ""))
# ""
# print(boolfuck(".", ""))
# ""
# print(boolfuck(";", ""))
# "\u0000"
print(boolfuck(">,>,>,>,>,>,>,>,<<<<<<<<>;>;>;>;>;>;>;>;<<<<<<<<", "*"))
# ""
# print(boolfuck(";;;+;+;;+;+;", ""))
# print(boolfuck(";;;+;+;;+;+;+;+;+;+;;+;;+;;;+;;+;+;;+;;;+;;+;+;;+;+;;;;+;+;;+;;;+;;+;+;+;;;;;;;+;+;;+;;;+;+;;;+;+;;;;+;+;;+;;+;+;;+;;;+;;;+;;+;+;;+;;;+;+;;+;;+;+;+;;;;+;+;;;+;+;+;", ""))
#  "Hello, world!\n"
# print(changeInputToBits("C"))
# print(changeStrBitsToOutput('110000101111011000100110101001101110111010000110011100100111001111111111'))
# print(changeStrBitsToOutput([1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0]))
# print(changeInputToBits("Codewars\u00ff"))
# print(boolfuck(">,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<;>;>;>;>;>;>;>;<<<<<<<,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]", "Codewars\u00ff"))
# Codewars\u00ff
# print(boolfuck(">,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>;>;>;>;>;>;>;>;>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>,>,>,>,>,>,>,>,>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]", "Codewars"))
# Codewars
# print(boolfuck(">,>,>,>,>,>,>,>,>>,>,>,>,>,>,>,>,<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]>[>]+<[+<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<<<<<<<<<<<<<<<<<<<[>]+<[+<]>>>>>>>>>[+]>>>>>>>>>>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]<<<<<<<<<<<<<<<<<<+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]>>>>>>>>>>>>>>>>>>>;>;>;>;>;>;>;>;<<<<<<<<", "\u0008\u0009"))
# \u0048
# input = 'Codewar\u00ff'
# olist = []
# output = ''
# for c in input:
#     print(c)
#     print(ord(c))
#     print(bin(ord(c)))
#     print(type(bin(ord(c))))
#     print(bin(ord(c))[2:])
#     print(bin(ord(c))[2:].rjust(8, '0'))
#     olist.append(bin(ord(c))[2:].rjust(8, '0')) 

# print(olist)
# for t in olist[::-1]:
#     print(t)
#     output += t

# print(output)
# olist = [int(c) for c in output]
# print(olist)
# print(olist.pop())
# print(olist.pop())
# print(olist.pop())
# input = [int(c) for c in ''.join([bin(ord(c))[2:].rjust(8, '0') for c in input][::-1])]
# print(input)
# out, s = out[8:], s + chr(int(''.join(str(c) for c in out[:8][::-1]).rjust(8, '0'), 2))
from collections import defaultdict


def boolfuckGood(code, input=""):
    input = [int(c) for c in ''.join([bin(ord(c))[2:].rjust(8, '0') for c in input][::-1])]
    cp, p, out, bits, starts, brackets = 0, 0, [], defaultdict(int), [], {}

    for i, c in enumerate(code):
        if c == '[': starts.append(i)
        elif c == ']':
            brackets[i] = starts.pop()
            brackets[brackets[i]] = i

    while cp < len(code):
        if   code[cp] == '[' and not bits[p]: cp = brackets[cp]
        elif code[cp] == ']': cp = brackets[cp] - 1
        elif code[cp] == '>': p += 1
        elif code[cp] == '<': p -= 1
        elif code[cp] == '+': bits[p] = (0 if bits[p] else 1)
        elif code[cp] == ',': bits[p] = (input.pop() if input else 0)
        elif code[cp] == ';': out.append(bits[p])
        cp += 1
        
    s = ''
    print(f"out={out}")
    while out:
        out, s = out[8:], s + chr(int(''.join(str(c) for c in out[:8][::-1]).rjust(8, '0'), 2))
    return s

# print(boolfuckGood(">,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>[+<<<<<<<<[>]+<[+<]>>>>>>>>>+<<<<<<<<+[>+]<[<]>>>>>>>>>[+]<<<<<<<<;>;>;>;>;>;>;>;<<<<<<<,>,>,>,>,>,>,>,<<<<<<<[>]+<[+<]>>>>>>>>>[+]+<<<<<<<<+[>+]<[<]>>>>>>>>>]<[+<]", "Codewars\u00ff"))
# out=[1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
# s = ''
# while out:
#     out, s = out[8:], s + chr(int(''.join(str(c) for c in out[:8][::-1]).rjust(8, '0'), 2))
    # out = out[8:] 
    # s = s + chr(int(''.join(str(c) for c in out[:8][::-1]).rjust(8, '0'), 2))
# print(s)
