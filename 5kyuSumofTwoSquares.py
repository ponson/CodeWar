
import unittest
import math

class Test_SumOfTwoSquare(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(all_squared_pairs(0), [[0, 0]])
    
    def testcase2(self):
        self.assertEqual(all_squared_pairs(1), [[0, 1]])

    def testcase3(self):
        self.assertEqual(all_squared_pairs(2), [[1, 1]])

    def testcase31(self):
        self.assertEqual(all_squared_pairs(8), [[2, 2]])

    def testcase4(self):
        self.assertEqual(all_squared_pairs(3), [])

    def testcase5(self):
        self.assertEqual(all_squared_pairs(10), [[1, 3]])

    def testcase6(self):
        self.assertEqual(all_squared_pairs(16), [[0, 4]])

    def testcase7(self):
        self.assertEqual(all_squared_pairs(20), [[2, 4]])

    def testcase8(self):
        self.assertEqual(all_squared_pairs(25), [[0, 5], [3, 4]])

    def testcase9(self):
        self.assertEqual(all_squared_pairs(325), [[1, 18], [6, 17], [10, 15]])

def is_sqrt(num):
    sqrtNum = math.isqrt(num)
    return sqrtNum * sqrtNum == num, sqrtNum

def all_squared_pairs(n):
    pairs = []
    isSqrt, nOffset = is_sqrt(n)
    if isSqrt:
        pairs.append([0, nOffset])
    nOffset += 1

    for num in range(1, nOffset):
        isSqrt, numSqrt = is_sqrt(n - num*num)
        if isSqrt and num <= numSqrt:
            pairs.append([num, numSqrt])

    return pairs


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4', 'testcase5', 'testcase6', 'testcase7', 'testcase8', 'testcase9']
    testOne = ['testcase31']
    suite = unittest.TestSuite(map(Test_SumOfTwoSquare, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)