import unittest


class Test_decode(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(decode(encode("Hello World!")), "Hello World!")

    def testcase2(self):
        self.assertEqual(decode("atC5kcOuKAr!"), "Hello World!")


def encode(s):
    pass
keychain = 'bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa'
uncodeMaps = {'a': 0, 'b': 1, 'c': 39, 'd': 2, 'e': 15, 'f': 40, 'g': 23, 'h': 3, 'i': 12, 'j': 16, 'k': 59, 'l': 41, 'm': 19, 'n': 24, 'o': 54, 'p': 4, 'q': 64, 'r': 13, 's': 10, 't': 17, 'u': 62, 'v': 60, 'w': 28, 'x': 42, 'y': 30, 'z': 20, 'A': 51, 'B': 25, 'C': 44, 'D': 55, 'E': 47, 'F': 5,         'G': 32, 'H': 65, 'I': 38, 'J': 14, 'K': 22, 'L': 11, 'M': 58, 'N': 18, 'O': 53, 'P': 63, 'Q': 9, 'R': 61, 'S': 27, 'T': 29, 'U': 50, 'V': 43, 'W': 46, 'X': 31, 'Y': 37, 'Z': 21, '0': 57, '1': 52, '2': 8, '3': 26, '4': 49, '5': 45, '6': 36, '7': 56, '8': 7, '9': 48, ',': 6, '?': 34, '.': 35, ' ': 33}

def create_index():

def decode(s):
    dkeys = 'bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa'
    asciikeys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?'
    firstpvalues = 'bdfhjlnprtvxzBDFHJLNPRTVXZ13579, acegikmoqsuwyACEGIK?86.'
    sIdx = {}
    for idx, c in enumerate(asciikeys):
        sIdx[c] = dkeys.find(firstpvalues[idx])
    print(f"sIdx={sIdx}")

    print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(encode("!@#$%^&*()_+-"))
    a, b, c = "", "", ""
    for w in "abcdefghijklmnopqrstuvwxyz":
        a += encode("" + w)[0]
        b += encode("_" + w)[1]
        c += encode("__" + w)[2]
    print(a)
    print(b)
    print(c)
    return s

if __name__ == '__main__':
    tests = ['testcase1', 'testcase2']
    testOne = ['testcase1']
    suite = unittest.TestSuite(map(Test_decode, tests))
    # suite = unittest.TestSuite(map(Test_decode, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)