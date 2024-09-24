
import unittest


class Test_last_digit(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(last_digit([]), 1)

    def testcase2(self):
        self.assertEqual(last_digit([0, 0]), 1)

    def testcase3(self):
        self.assertEqual(last_digit([0, 0, 0]), 0)

    def testcase4(self):
        self.assertEqual(last_digit([1, 2]), 1)

    def testcase5(self):
        self.assertEqual(last_digit([3, 4, 5]), 1)
        
    def testcase6(self):
        self.assertEqual(last_digit([4, 3, 6]), 4)

    def testcase7(self):
        self.assertEqual(last_digit([7, 6, 21]), 1)

    def testcase8(self):
        self.assertEqual(last_digit([12, 30, 21]), 6)

    def testcase9(self):
        self.assertEqual(last_digit([2, 2, 2, 0]), 4)

    def testcase10(self):
        self.assertEqual(last_digit([937640, 767456, 981242]), 0)

    def testcase11(self):
        self.assertEqual(last_digit([499942, 898102, 846073]), 6)

    def testcase12(self):
        self.assertEqual(last_digit([123232, 694022, 140249]), 6)

digit2_circle = {4:[4, 6], 9: [9, 1]}
digit4_circle = {2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6]}
const_digits = [0, 1, 5, 6]

def last_digit(lst):
    if len(lst) == 0:
        return 1
    if len(lst) == 1:
        return lst[0]

    baseLast = lst[0] % 10

    if baseLast in const_digits:
        circles = [baseLast]
        looplen = 1
    elif baseLast in digit2_circle.keys():
        circles = digit2_circle[baseLast]
        looplen = 2
    else:
        circles = digit4_circle[baseLast]
        looplen = 4

    for i in range(len(lst)-1, 0, -1):
        if i == len(lst) - 1:
            explist = lst[i] % 10
        else:
            if lst[i] == 0 and explist == 0:
                explist = 1
            else:
                b = lst[i] 
                e = explist
                explist = (b**(e if e < 4 else e % 4 + 4))
        
    if lst[0] == 0:
        if explist == 0:
            return 1
        else:
            return 0

    return circles[(explist+looplen-1) % looplen]


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4',
             'testcase5', 'testcase6', 'testcase7',  'testcase8',
             'testcase9',  'testcase10']
    testOne = ['testcase7']
    # suite = unittest.TestSuite(map(Test_last_digit, tests))
    suite = unittest.TestSuite(map(Test_last_digit, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)