
import unittest
import math
import functools
import time

class Test_SumOfTwoSquare(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(two_squares(440), 0)

    def testcase2(self):
        self.assertEqual(two_squares(384), 0)

    def testcase3(self):
        self.assertEqual(two_squares(369), 27)

    def testcase4(self):
        self.assertEqual(two_squares(481), 31)

    def testcase5(self):
        self.assertEqual(two_squares(773), 39)

    def testcase6(self):
        self.assertEqual(two_squares(546), 0)

    def testcase7(self):
        self.assertEqual(two_squares(256), 16)

    def testcase8(self):
        self.assertEqual(two_squares(961), 31)

    def testcase9(self):
        self.assertEqual(two_squares(78400), 392)

    def testcase10(self):
        self.assertEqual(two_squares(294830386), 18496)

    def testcase11(self):
        self.assertEqual(two_squares(428216372), 29262)

    def testcase12(self):
        self.assertEqual(two_squares(767307925), 0)

    def testcase13(self):
        self.assertEqual(two_squares(866856952979), 0)


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer

# @timer
def is_sqrt(num):
    sqrtNum = math.isqrt(num)
    return sqrtNum * sqrtNum == num, sqrtNum


def two_squares(n):
    pairs = []
    squares = []
    isSqrt, nOffset = is_sqrt(n)
    if isSqrt:
        pairs = [0, nOffset]
    nOffset += 1

    for num in range(1, nOffset):
        squares.append(num*num)
        
    for num in range(1, nOffset):
        numSqure = num*num
        if n - numSqure in squares:
            nsqrt = squares.index(numSqure)+1
            if len(pairs) == 0 or sum(pairs) < num+nsqrt:
                pairs = [num, nsqrt]
    #     isSqrt, numSqrt = is_sqrt(n - num*num)
    #     if isSqrt and num <= numSqrt:
    #         if len(pairs) == 0 or sum(pairs) < num+numSqrt:
    #             pairs = [num, numSqrt]

    # print(f"The pair is: {pairs}")

    if len(pairs) > 0:
        # print(f"pairs is {pairs}")
        return sum(pairs)
    else:
        return 0


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4',
             'testcase5', 'testcase6', 'testcase7', 'testcase8', 'testcase9', 'testcase10',
             'testcase11', 'testcase12',  'testcase13']
    testOne = ['testcase9']
    suite = unittest.TestSuite(map(Test_SumOfTwoSquare, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)
