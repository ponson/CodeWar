import unittest


class Test_Simple_ASMInterpret(unittest.TestCase):

    def testcase1(self):
        code = '''\
; My first program
mov  a, 5
inc  a
call function
msg  '(5+1)/2 = ', a    ; output message
end

function:
    div  a, 2
    ret
'''

        self.assertEqual(simple_assembler(code.splitlines()), '(5+1)/2 = 3')

    def testcase2(self):
        code = '''\
mov   a, 5
mov   b, a
mov   c, a
call  proc_fact
call  print
end

proc_fact:
    dec   b
    mul   c, b
    cmp   b, 1
    jne   proc_fact
    ret

print:
    msg   a, '! = ', c ; output text
    ret
'''
        self.assertEqual(simple_assembler(code.splitlines()), '5! = 120')

    def testcase3(self):
        code = '''\
mov   a, 8            ; value
mov   b, 0            ; next
mov   c, 0            ; counter
mov   d, 0            ; first
mov   e, 1            ; second
call  proc_fib
call  print
end

proc_fib:
    cmp   c, 2
    jl    func_0
    mov   b, d
    add   b, e
    mov   d, e
    mov   e, b
    inc   c
    cmp   c, a
    jle   proc_fib
    ret

func_0:
    mov   b, c
    inc   c
    jmp   proc_fib

print:
    msg   'Term ', a, ' of Fibonacci series is: ', b        ; output text
    ret
'''
        self.assertEqual(simple_assembler(code.splitlines()), 'Term 8 of Fibonacci series is: 21')


    def testcase4(self):
        code = '''\
mov   a, 11           ; value1
mov   b, 3            ; value2
call  mod_func
msg   'mod(', a, ', ', b, ') = ', d        ; output
end

; Mod function
mod_func:
    mov   c, a        ; temp1
    div   c, b
    mul   c, b
    mov   d, a        ; temp2
    sub   d, c
    ret
'''
        self.assertEqual(simple_assembler(code.splitlines()),'mod(11, 3) = 2')


    def testcase5(self):
        code = '''\
mov   a, 81         ; value1
mov   b, 153        ; value2
call  init
call  proc_gcd
call  print
end

proc_gcd:
    cmp   c, d
    jne   loop
    ret

loop:
    cmp   c, d
    jg    a_bigger
    jmp   b_bigger

a_bigger:
    sub   c, d
    jmp   proc_gcd

b_bigger:
    sub   d, c
    jmp   proc_gcd

init:
    cmp   a, 0
    jl    a_abs
    cmp   b, 0
    jl    b_abs
    mov   c, a            ; temp1
    mov   d, b            ; temp2
    ret

a_abs:
    mul   a, -1
    jmp   init

b_abs:
    mul   b, -1
    jmp   init

print:
    msg   'gcd(', a, ', ', b, ') = ', c
    ret
'''
        self.assertEqual(simple_assembler(code.splitlines()),'gcd(81, 153) = 9')
    
    
    def testcase6(self):
        code = '''\
call  func1
call  print
end

func1:
    call  func2
    ret

func2:
    ret

print:
    msg 'This program should return -1'
'''
        self.assertEqual(simple_assembler(code.splitlines()), -1)
    
    
    def testcase7(self):
        code = '''\
mov   a, 2            ; value1
mov   b, 10           ; value2
mov   c, a            ; temp1
mov   d, b            ; temp2
call  proc_func
call  print
end

proc_func:
    cmp   d, 1
    je    continue
    mul   c, a
    dec   d
    call  proc_func

continue:
    ret

print:
    msg a, '^', b, ' = ', c
    ret
'''
        self.assertEqual(simple_assembler(code.splitlines()),  '2^10 = 1024')
#####################################


def mov_func(regs, cmds, lbls, inters):
    if cmds[2].isnumeric() or (cmds[2][0] == '-' and cmds[2][1:].isnumeric()):
        regs[cmds[1]] = int(cmds[2])
    else:
        regs[cmds[1]] = regs[cmds[2]]

    return None


def inc_func(regs, cmds, lbls, inters):
    regs[cmds[1]] += 1

    return None


def dec_func(regs, cmds, lbls, inters):
    regs[cmds[1]] -= 1

    return None


def add_func(regs, cmds, lbls, inters):
    #target register
    tr = cmds[1]
    param = cmds[2]
    if param.isnumeric() or (param[0] == '-' and param[1:].isnumeric()):
        regs[tr] += int(param)
    else:
        regs[tr] += regs[cmds[2]]

    return None


def sub_func(regs, cmds, lbls, inters):
    #target register
    tr = cmds[1]
    param = cmds[2]
    if param.isnumeric() or (param[0] == '-' and param[1:].isnumeric()):
        regs[tr] -= int(param)
    else:
        regs[tr] -= regs[cmds[2]]

    return None


def mul_func(regs, cmds, lbls, inters):
    #target register
    tr = cmds[1]
    param = cmds[2]
    if param.isnumeric() or (param[0] == '-' and param[1:].isnumeric()):
        regs[tr] *= int(param)
    else:
        regs[tr] *= regs[cmds[2]]

    return None


def div_func(regs, cmds, lbls, inters):
    #target register
    tr = cmds[1]
    param = cmds[2]
    if param.isnumeric() or (param[0] == '-' and param[1:].isnumeric()):
        regs[tr] /= int(param)
    else:
        regs[tr] /= regs[cmds[2]]
    regs[tr] = int(regs[tr])

    return None


def call_func(regs, cmds, lbls, inters):
    if cmds[1] in lbls.keys():
        if '_ret' not in inters.keys():
            inters['_ret'] = []
        inters['_ret'].append(inters['_pc'])
        return lbls[cmds[1]] + 1
    else:
        return -1


def jmp_func(regs, cmds, lbls, inters):
    if cmds[1] in lbls.keys():
        return lbls[cmds[1]] + 1
    else:
        return -1


def end_func(regs, cmds, lbls, inters):
    return inters['_codeLen']


def ret_func(regs, cmds, lbls, inters):
    return inters['_ret'].pop() + 1


def comment_func(regs, cmds, lbls, inters):
    pass


def msg_func(regs, cmds, lbls, inters):
    msg = []
    source = cmds[1]
    srcLen = len(source)
    start_idx = 0

    while start_idx < srcLen:
        if source[start_idx] == "'":  #Found '
            second_apo_idx = source.find("'", start_idx+1)
            msg.append(source[start_idx+1:second_apo_idx])
            if (second_apo_idx+1 < srcLen) and source[second_apo_idx+1] == ",":
                start_idx = second_apo_idx + 3
            else:
                start_idx = second_apo_idx + 2
        elif source[start_idx] == ";":  #Found ;
            break
        else:
            if source[start_idx] == ' ':
                start_idx += 1
                continue
            spc_idx = source.find(" ", start_idx)
            if spc_idx > 0:
                if source[spc_idx-1] == ',':
                    msg.append(str(regs[source[start_idx:spc_idx-1]]))
                else:
                    msg.append(str(regs[source[start_idx:spc_idx]]))
                start_idx = spc_idx + 1
            else: # no more spaces
                msg.append(str(regs[source[start_idx:srcLen]]))
                start_idx = srcLen

    return "".join(msg)


def cmp_func(regs, cmds, lbls, inters):
    #target register
    x = cmds[1]
    y = cmds[2]
    if x.isnumeric() or (x[0] == '-' and x[1:].isnumeric()):
        x = int(x)
    else:
        x = regs[x]
    if y.isnumeric() or (y[0] == '-' and y[1:].isnumeric()):
        y = int(y)
    else:
        y = regs[y]

    regs['cmr'] = x - y

    return None

def jcmp_func(regs, cmds, lbls, inters):
    if eval(str(regs['cmr'])+cmpDicts[cmds[0]]+'0'):
        return lbls[cmds[1]] + 1
    else:
        return None


def simple_assembler(program):
    codeLen = len(program)
    cmdLines = []
    labels = {}
    internals = {}
    for i in range(codeLen):
        program[i] = program[i].lstrip()
        if program[i][0:3] == 'msg': #Not split
            cmdLines.append(['msg', program[i][4:]])
        else:
            cmdLines.append(program[i].split())
        if len(cmdLines[i]) and cmdLines[i][0] not in funcDicts.keys():
            labels[cmdLines[i][0].rstrip(':')] = i
    pc = 0
    internals['_pc'] = pc
    internals['_codeLen'] = codeLen
    registers = {}
    output = ''
    while pc < codeLen:
        command = cmdLines[pc]
        if len(command) == 0 or pc in labels.values():
            pc += 1
            continue

        if command[0] == ';':
            pc += 1
            internals['_pc'] = pc
            continue
        # print(command)
        # Remove the last ',' if found
        if command[0] != 'msg' and len(command) > 1:
            command[1] = command[1].rstrip(',')

        cmdResult = funcDicts[command[0]](registers, command, labels, internals)

        if command[0] == 'msg':
            output = cmdResult
            cmdResult = None
        elif command[0] == 'end':
            return output

        if cmdResult == None:
            pc += 1
        elif cmdResult >= 0:
            pc = cmdResult
        else:
            return cmdResult # -1 
        internals['_pc'] = pc
        # print(registers)
	# return a dictionary with the registers
    return -1


cmpDicts = {'jne':'!=', 'je':'==', 'jge':'>=', 'jg':'>', 'jle':'<=', 'jl': '<'}


funcDicts = {'mov': mov_func, 'inc': inc_func, 'dec': dec_func,
             'add': add_func, 'sub': sub_func, 'mul': mul_func, 'div': div_func,
             'call': call_func, 'end': end_func, 'ret': ret_func, 'jmp': jmp_func,
             ';': comment_func, 'msg': msg_func,
             'cmp':cmp_func,
             'jne': jcmp_func, 'je': jcmp_func, 'jge': jcmp_func, 'jg': jcmp_func, 'jle': jcmp_func, 'jl': jcmp_func,}

if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4', 'testcase5', 'testcase6', 'testcase7']
    testOne = ['testcase7']
    suite = unittest.TestSuite(map(Test_Simple_ASMInterpret, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
