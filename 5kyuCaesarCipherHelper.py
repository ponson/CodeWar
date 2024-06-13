import unittest



class Test_CaesarCipher(unittest.TestCase):

    def testcase1(self):
        c = CaesarCipher(5)
        self.assertEqual(c.encode('Codewars'), 'HTIJBFWX')
        self.assertEqual(c.decode('HTIJBFWX'), 'CODEWARS')


class CaesarCipher(object):
    def __init__(self, shift):
        self.aAZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.shift = int(shift)

    def encode(self, st):
        self.st = st.upper()
        self.enstr = ''
        for self.c in self.st:
            if self.c in self.aAZ:
                self.enstr += self.aAZ[(self.aAZ.find(self.c)+self.shift) % 26]
            else:
                self.enstr += self.c

        return self.enstr 

    def decode(self, st):
        self.st = st.upper()
        self.destr = ''
        for self.c in self.st:
            if self.c in self.aAZ:
                self.destr += self.aAZ[(self.aAZ.find(self.c)+26-self.shift) % 26]
            else:
                self.destr += self.c

        return self.destr 
    

if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4', 'testcase5']
    testOne = ['testcase1']
    suite = unittest.TestSuite(map(Test_CaesarCipher, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)