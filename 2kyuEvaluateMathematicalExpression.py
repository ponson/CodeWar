import unittest


class TestScreenLokingPatterns(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(calc('1 + 1'), 2)

    def test_case2(self):
        self.assertEqual(calc("8/16"), 0.5)

    def test_case3(self):
        self.assertEqual(calc("3 -(-1)"), 4)

    def test_case4(self):
        self.assertEqual(calc("10- 2- -5"), 13)

    def test_case5(self):
        self.assertEqual(calc("(((10)))"), 10)

    def test_case6(self):
        self.assertEqual(calc("3 * 5"), 15)

    def test_case7(self):
        self.assertEqual(calc("-7 * -(6 / 3)"), 14)

    def test_case8(self):
        self.assertEqual(
            calc("(22) * (83 * 37 - -(50)) / (33 / -(((-(-52 / -43)))) / -62)"), -156001.6)
        
    def test_case9(self):
        self.assertEqual(calc("-(92) * (76 * -77 - -(86)) * (53 / (((-(29 - 59)))) - -5)"), 3589527)

    def test_case10(self):
        self.assertEqual(calc("-(-75) - (81 * -7 / -(20)) + (-19 / (((-(27 * 46)))) + 11)"), 57.665)
        

opSet = ['+', '-', '*', '/']
NumSet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def real_calc(que):
    idx = 0
    while len(que) > 1 and idx < len(que):  # 先處理乘除
        if que[idx] in opSet and opSet.index(que[idx]) > 1:
            if que[idx] == '*':
                ans = que[idx-1] * que[idx+1]
            else:
                ans = que[idx-1] / que[idx+1]

            for _ in range(3):
                que.pop(idx-1)
            que.insert(idx-1, ans)
            idx -= 1
        else:
            idx += 1

    idx = 0
    while len(que) > 1 and idx < len(que):
        if que[idx] in opSet:  # 後加減
            if que[idx] == '+':
                ans = que[idx-1] + que[idx+1]
            else:
                ans = que[idx-1] - que[idx+1]

            for _ in range(3):
                que.pop(idx-1)
            que.insert(idx-1, ans)
            idx -= 1
        else:
            idx += 1

    return que[0]


def calc(expression):
    expQue = []
    parens = 0
    parensIdxs = []
    minus_tags = []
    numChars = []
    expression = expression.replace(' ', '')
    for c in expression:
        if c == '(':
            minus_tags.append(False)
            if len(numChars) == 1 and numChars[0] == '-': 
                numChars = []
                minus_tags[parens] = True
            qStart = len(expQue) if expQue else 0
            parensIdxs.append(qStart)
            parens += 1

        elif c == ')':
            if len(numChars) > 0:
                expQue.append(int(''.join(numChars)))
                numChars = []
            internalQue = expQue[parensIdxs[parens-1]:]
            if len(internalQue) > 1:    
                ilen = len(internalQue)
                calResult = real_calc(internalQue)
                for _ in range(ilen):
                    expQue.pop(parensIdxs[parens-1])
                expQue.append(calResult)
            if minus_tags[parens-1]:
                expQue[-1] *= -1
            parens -= 1
            parensIdxs.pop(parens)
            minus_tags.pop(parens)

        elif c in opSet:
            # 負號
            if c == '-' and not numChars and (not expQue or expQue[-1] in opSet):
                numChars.append(c)
            else:
                if numChars:
                    expQue.append(int(''.join(numChars)))
                    numChars = []
                expQue.append(c)
        elif c in NumSet:
            numChars.append(c)
        else:
            pass  # Space

    if numChars:
        expQue.append(int(''.join(numChars)))

    result = real_calc(expQue)
    return result


if __name__ == '__main__':
    # tests = ['test_case8']
    tests = ['test_case1', 'test_case2', 'test_case3','test_case4', 'test_case5', 'test_case6', 'test_case7', 'test_case8', 'test_case9', 'test_case10']
    # tests = ['test_case5', 'test_case6', 'test_case7']
    suite = unittest.TestSuite(map(TestScreenLokingPatterns, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
