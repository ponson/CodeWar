def replaceQmarkAndCheckValid(num, n):
    num = num.replace('?', n)

    if (int(num) == 0 and num != '0') or (num[0] == '0' and len(num) > 1) or ():
        return num, "Invalid"

    if len(num) > 1 and (num[0] == '0' or (num[0] == '-' and num[1] == '0')):
        return num, "Invalid"
        
    return num, "Valid"


def solve_runes(runes):
    #TODO 1 切出tokens。 operators, operands, answer
    operands = ['*', '+', '-']
    equal_idx = runes.find('=')
    answer = runes[equal_idx+1:]
    op_idx = 0
    optor = ''
    for idx, c in enumerate(runes):
        if c in operands:
            if idx == 0 and c == '-':
                continue
            optor = c
            op_idx = idx
            break
    
    op1 = runes[:op_idx]
    op2 = runes[op_idx+1:equal_idx]
    print(f"op1={op1}, op2={op2}, optor={optor} answer={answer}")
    #TODO 2 除去現有的數字, 一次將未出現的數字去替換?執行運算和Answer做比對，找出第一個符合的lowest，找不到return -1
    num_pool = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for item in runes:
        if item in num_pool:
            num_pool.remove(item)

    print(num_pool)
    for n in num_pool:
        new_op1, result = replaceQmarkAndCheckValid(op1, n)
        if result == "Invalid":
            continue
        new_op2, result = replaceQmarkAndCheckValid(op2, n)
        if result == "Invalid":
            continue
        new_answer, result = replaceQmarkAndCheckValid(answer, n)
        if result == "Invalid":
            continue
            
        if optor == '+':
            if int(new_op1) + int(new_op2) == int(new_answer):
                return int(n)
            else:
                continue
        elif optor == '-':
            # print(f"int op1 = {int(new_op1)}")
            # print(f"int op2 = {int(new_op2)}")
            # print(f"int answer = {int(new_answer)}")
            if int(new_op1) - int(new_op2) == int(new_answer):
                return int(n)
            else:
                continue
        elif optor == '*':
            if int(new_op1) * int(new_op2) == int(new_answer):
                return int(n)
            else:
                continue

    return -1
    
    
# print(solve_runes("123?45*?=?"))   #0
# print(solve_runes("?*123?45=?"))   #0
# print(solve_runes("??+??=??"))     #-1
print(solve_runes("-?56373--9216=-?47157"))   #8
# print(solve_runes("1+1=?")) #2
# print(solve_runes("123*45?=5?088")) #6
# print(solve_runes("-5?*-1=5?")) #0
# print(solve_runes("19--45=5?")) #-1
# print(solve_runes("??*??=302?")) #5
# print(solve_runes("?*11=??")) #2
# print(solve_runes("??*1=??")) #2
