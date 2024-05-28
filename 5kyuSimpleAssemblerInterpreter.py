import unittest


class Test_Simple_ASMInterpret(unittest.TestCase):

    def testcase1(self):
        code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''

        self.assertEqual(simple_assembler(code.splitlines()), {'a': 1})

    def testcase2(self):
        code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
        self.assertEqual(simple_assembler(code.splitlines()), {
                         'a': 409600, 'c': 409600, 'b': 409600})

                        
    def testcase3(self):
        code = ['mov a -10', 'mov b a', 'inc a', 'dec b', 'jnz a -2']
        self.assertEqual(simple_assembler(code), {'a': 0, 'b': -20})


def mov_func(regs, cmds):
    if cmds[2].isnumeric() or (cmds[2][0] == '-' and cmds[2][1:].isnumeric()):
        regs[cmds[1]] = int(cmds[2])
    else:
        regs[cmds[1]] = regs[cmds[2]]

    return 0


def inc_func(regs, cmds):
    regs[cmds[1]] += 1

    return 0


def dec_func(regs, cmds):
    regs[cmds[1]] -= 1

    return 0


def jnz_func(regs, cmds):
    if cmds[1].isnumeric() or (cmds[1][0] == '-' and cmds[1][1:].isnumeric()):
        v = int(cmds[1])
    else:
        v = regs[cmds[1]]

    if v:
        if cmds[2].isnumeric() or (cmds[2][0] == '-' and cmds[2][1:].isnumeric()):
            return int(cmds[2])
        else:
            return regs[cmds[2]]
    else:
        return 0


def simple_assembler(program):
    codeLen = len(program)
    pc = 0
    registers = {}
    while pc < codeLen:
        command = program[pc].split()
        # print(command)

        cmdResult = funcDicts[command[0]](registers, command)

        if command[0] == 'jnz' and cmdResult != 0:
            pc += cmdResult
        else:
            pc += 1
        # print(registers)
	# return a dictionary with the registers
    return registers


funcDicts = {'mov':mov_func, 'inc':inc_func, 'dec':dec_func, 'jnz':jnz_func}

if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3']
    testOne = ['testcase3']
    suite = unittest.TestSuite(map(Test_Simple_ASMInterpret, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)
