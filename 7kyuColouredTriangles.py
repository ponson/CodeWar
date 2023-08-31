import unittest


class TestDinglemouse(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(triangle('GB'), 'R')

    def test_case2(self):
        self.assertEqual(triangle('RRR'), 'R')

    def test_case3(self):
        self.assertEqual(triangle('RGBG'), 'B')

    def test_case4(self):
        self.assertEqual(triangle('RBRGBRB'), 'G')

    def test_case5(self):
        self.assertEqual(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')

    def test_case6(self):
        self.assertEqual(triangle('B'), 'B')


def check_rules(c1, c2):
    if c1 == c2:
        return c1
    else:
        c = [x for x in 'RGB' if x not in (c1, c2)]
        return c[0]

def triangle(row):
    loop = len(row) - 1
    for _ in range(loop):
        row = [check_rules(row[i], row[i+1]) for i in range(len(row)-1)]
    return row[0]

if __name__ == '__main__':
    unittest.main(verbosity=2)