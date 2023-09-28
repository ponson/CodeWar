import unittest


class TestVCipherHelper(unittest.TestCase):
    def test_case1(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"
        c = VigenereCipher(key, abc)
        self.assertEqual(c.decode('rovwsoiv'), 'codewars')
        self.assertEqual(c.decode('laxxhsj'), 'waffles')
        self.assertEqual(c.decode('CODEWARS'), 'CODEWARS')

    def test_case2(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"
        c = VigenereCipher(key, abc)
        self.assertEqual(c.encode('codewars'), 'rovwsoiv')
        self.assertEqual(c.encode('waffles'), 'laxxhsj')
        self.assertEqual(c.encode('CODEWARS'), 'CODEWARS')

    def test_case3(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"
        c = VigenereCipher(key, abc)
        self.assertEqual(c.encode("it's a shift cipher!"), "xt'k o vwixl qzswej!")
        self.assertEqual(c.decode("xt'k o vwixl qzswej!"),"it's a shift cipher!")

class VigenereCipher(object):
    def __init__(self, key, alphabet):
        print(f"key={key}")
        print(f"alphabet={alphabet}")
        self.alphabet = alphabet
        self.dict_alphabet = {c:i for i, c in enumerate(alphabet)}
        self.shift_idx = [self.dict_alphabet[c] for c in key]
    
    def encode(self, text):
        print(f"encode_text={text}")
        self.text_idx = [self.dict_alphabet[c] if c in self.alphabet else (i+1)*(-1) for i, c in enumerate(text)]
        result = ''
        for o_i, idx in enumerate(self.text_idx):
            s_idx = self.shift_idx[o_i % len(self.shift_idx)]
            result += self.alphabet[(idx + s_idx) % len(self.alphabet)] if idx >=0 else text[int(abs(idx+1))]
        return result
    
    def decode(self, text):
        print(f"decode_text={text}")
        self.text_idx = [self.dict_alphabet[c] if c in self.alphabet else (i+1)*(-1) for i, c in enumerate(text)]
        result = ''
        for o_i, idx in enumerate(self.text_idx):
            s_idx = self.shift_idx[o_i % len(self.shift_idx)]
            result += self.alphabet[(idx - s_idx + len(self.alphabet)) % len(self.alphabet)] if idx >=0 else text[int(abs(idx+1))]
        return result



if __name__ == '__main__':
    tests = ['test_case3']
    # tests = ['test_case1', 'test_case2'] 
    suite = unittest.TestSuite(map(TestVCipherHelper, tests))
    # unittest.main(verbosity=2)
    unittest.TextTestRunner(verbosity=2).run(suite)