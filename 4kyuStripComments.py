import unittest
import re


class TestStripComments(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', [
                         '#', '!']), 'apples, pears\ngrapes\nbananas')

    def test_case2(self):
        self.assertEqual(strip_comments(
            'a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')

    def test_case3(self):
        self.assertEqual(strip_comments(
            ' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')

    def test_case4(self):
        self.assertEqual(strip_comments(
            '\n$', ['#', '$']), '\n')


def strip_comments(strng, markers):
    print(f"strng={strng}")
    print(f"markers={markers}")
    ans = ''
    for line in strng.splitlines():
        cutLine = ''
        isMatched = False
        for n, c in enumerate(line):
            if c in markers:
                isMatched = True
                cutLine = line[:n]
                cutLine = cutLine.rstrip()
                break

        if isMatched == False:
            ans += (line + '\n')
        else:
            ans += (cutLine + '\n')

    return ans[0:-1]

if __name__ == '__main__':
    tests = ['test_case1', 'test_case2', 'test_case3', 'test_case4'] 
    # tests = ['test_case4'] 
    # suite = (unittest.TestLoader().loadTestsFromTest)
    suite = unittest.TestSuite(map(TestStripComments, tests))
    # unittest.main(verbosity=2)
    unittest.TextTestRunner(verbosity=2).run(suite)