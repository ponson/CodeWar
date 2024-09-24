import unittest


class Test_last_digit(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(last_digit(4, 1), 4)

    def testcase2(self):
        self.assertEqual(last_digit(4, 2), 6)

    def testcase3(self):
        self.assertEqual(last_digit(9, 7), 9)

    def testcase4(self):
        self.assertEqual(last_digit(10, 10 ** 10), 0)

    def testcase5(self):
        self.assertEqual(last_digit(2 ** 200, 2 ** 300), 6)
        
    def testcase6(self):
        self.assertEqual(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

    def testcase7(self):
        self.assertEqual(last_digit(95260401745938272741270354905929274348560759762696270002, 19150309221999908662482878738112873089126528921190764433312), 6)


digit2_circle = {4:[4, 6], 9: [9, 1]}
digit4_circle = {2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6]}
const_digits = [0, 1, 5, 6]

def last_digit(n1, n2):
    n1Last = n1 % 10
    if n2 == 0:
        return 1
    if n2 == 1 or n1Last in const_digits:
        return n1Last

    if n1Last in digit2_circle.keys():
        return digit2_circle[n1Last][(n2-1)%2]
    else:
        return digit4_circle[n1Last][(n2-1)%4]




if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4',
             'testcase5', 'testcase6', 'testcase7']
    testOne = ['testcase7']
    suite = unittest.TestSuite(map(Test_last_digit, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)