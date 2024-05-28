import unittest
from sympy import Symbol, series


class Test_expand_testcases(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(expand("(x+1)^0"), "1")

    def testcase2(self):
        self.assertEqual(expand("(x+1)^1"), "x+1")

    def testcase3(self):
        self.assertEqual(expand("(x+1)^2"), "x^2+2x+1")

    def testcase4(self):
        self.assertEqual(expand("(x-1)^0"), "1")

    def testcase5(self):
        self.assertEqual(expand("(x-1)^1"), "x-1")

    def testcase6(self):
        self.assertEqual(expand("(x-1)^2"), "x^2-2x+1")

    def testcase7(self):
        self.assertEqual(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")

    def testcase8(self):
        self.assertEqual(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")

    def testcase9(self):
        self.assertEqual(expand("(7x-7)^0"), "1")

    def testcase10(self):
        self.assertEqual(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")

    def testcase11(self):
        self.assertEqual(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")

    def testcase12(self):
        self.assertEqual(expand("(-7x-7)^0"), "1")


def expand(expr):
    pass


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4', 'testcase5', 'testcase6', 'testcase7', 'testcase8', 'testcase9', 'testcase10', 'testcase11', 'testcase12', ]
    testOne = ['testcase7']
    suite = unittest.TestSuite(map(Test_expand_testcases, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)