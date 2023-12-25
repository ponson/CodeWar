import unittest
import re


class TestRemoveVowels(unittest.TestCase):
    
    def test_case1(self):
        self.assertEqual(
            disemvowel("This website is for losers LOL!"), 
            "Ths wbst s fr lsrs LL!")

    def test_case2(self):
        self.assertEqual(disemvowel(
            "No offense but,\nYour writing is among the worst I've ever read"), 
            "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd")

    def test_case3(self):
        self.assertEqual(disemvowel(
            "What are you, a communist?"), 
            "Wht r y,  cmmnst?")


def disemvowel(string_):

    return ''.join(re.split("[aeiouAEIOU]", string_))


if __name__ == '__main__':
    tests = ['test_case1', 'test_case2', 'test_case3' ]
    suit = unittest.TestSuite(map(TestRemoveVowels, tests))
    unittest.TextTestRunner(verbosity=2).run(suit)