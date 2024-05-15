import unittest
import itertools


class Test_The_boolean_order(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(solve("tft", "^&"), 2)

    def testcase2(self):
        self.assertEqual(solve("ttftff", "|&^&&"), 16)

    def testcase3(self):
        self.assertEqual(solve("ttftfftf", "|&^&&||"), 339)
    
    def testcase4(self):
        self.assertEqual(solve("ttftfftft", "|&^&&||^"), 851)

    def testcase5(self):
        self.assertEqual(solve("ttftfftftf", "|&^&&||^&"),2434)
    

def count(oprands, oprators, cacheCnts):

    keyStr = oprands + oprators

    # Got cache, return counts directly
    cntTuple = cacheCnts.get(keyStr)
    if cntTuple:
        return cntTuple

    #TODO 1: main process
    trueCnt, falseCnt = 0, 0
    oprandLen = len(oprands)
    opratorLen = len(oprators)

    # Expression complete
    if oprandLen == 1:
        if oprands == 't':
            trueCnt = 1
        else:
            falseCnt = 1
        return (falseCnt, trueCnt)

    for i in range(0, opratorLen):
        opr = oprators[i]
        loprands = oprands[0: i+1]
        loprators = oprators[0: i]
        roprands = oprands[i+1:oprandLen]
        roprators = oprators[i+1:opratorLen]

        lcntTuple = count(loprands, loprators, cacheCnts)
        rcntTuple = count(roprands, roprators, cacheCnts)
        lfalseCnt, ltrueCnt = lcntTuple
        rfalseCnt, rtrueCnt = rcntTuple


        if (opr == '&'):
            trueCnt += ltrueCnt * rtrueCnt
            falseCnt += ltrueCnt * rfalseCnt
            falseCnt += lfalseCnt * rtrueCnt
            falseCnt += lfalseCnt * rfalseCnt
        elif (opr == '|'):
            trueCnt += ltrueCnt * rtrueCnt
            trueCnt += ltrueCnt * rfalseCnt
            trueCnt += lfalseCnt * rtrueCnt
            falseCnt += lfalseCnt * rfalseCnt
        elif (opr == '^'):
            falseCnt += ltrueCnt * rtrueCnt
            trueCnt += ltrueCnt * rfalseCnt
            trueCnt += lfalseCnt * rtrueCnt
            falseCnt += lfalseCnt * rfalseCnt

    #TODO 2: save the result to cache
    cacheCnts[keyStr] = (falseCnt, trueCnt)

    return (falseCnt, trueCnt)



def solve(s, ops):
    memCache = {}
    cntResult = count(s, ops, memCache)

    return cntResult[1] #return True counts


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4', 'testcase5']
    testOne = ['testcase2']
    suite = unittest.TestSuite(map(Test_The_boolean_order, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)