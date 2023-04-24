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
        new_op1 = op1.replace('?', n)
        new_op2 = op2.replace('?', n)
        new_answer = answer.replace('?', n)
        if (int(new_op1) == 0 and new_op1 != '0') or (int(new_op2) == 0 and new_op2 != '0') or (int(new_answer) == 0 and new_answer != '0'):
            continue
        if n == '0':
            if (new_op1[0] == n and len(new_op1) > 1) or (new_op2[0] == n and len(new_op2) > 1) or (new_answer[0] == n and len(new_answer) > 1):
                continue
            if (len(new_op1) > 1 and new_op1[1] == n and new_op1[0] == '-') or (len(new_op2) > 1 and new_op2[1] == n and new_op2[0] == '-') or (len(new_answer) > 1 and new_answer[1] == n and new_answer[0] == '-'): 
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
