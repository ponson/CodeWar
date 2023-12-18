import unittest


class TestScreenLokingPatterns(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(count_patterns_from('A', 10), 0)

    def test_case2(self):
        self.assertEqual(count_patterns_from('A', 0),  0)

    def test_case3(self):
        self.assertEqual(count_patterns_from('E', 14), 0)

    def test_case4(self):
        self.assertEqual(count_patterns_from('B', 1),  1)

    def test_case5(self):
        self.assertEqual(count_patterns_from('C', 2),  5)

    def test_case6(self):
        self.assertEqual(count_patterns_from('E', 2),  8)

    def test_case7(self):
        self.assertEqual(count_patterns_from('E', 4),  256)


Tokens = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}
axis = {'A': (-1, -1), 'B': (-1, 0), 'C': (-1, 1), 'D': (0, -1),
        'E': (0, 0), 'F': (0, 1), 'G': (1, -1), 'H': (1, 0), 'I': (1, 1)}
deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),
          (-2, -2), (-2, 0), (-2, 2), (0, -2), (0, 2), (2, -2), (2, 0), (2, 2),
          (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
MAX_X = MAX_Y = 1
MIN_X = MIN_Y = -1

def count_patterns_from(firstPoint, length):
    x, y = axis[firstPoint]
    if length < 1 or length > 9:
        return 0
    if length == 1:
        return 1
    remainTokens = Tokens.copy()
    remainTokens.remove(firstPoint)
    ans_count = 0
    return check_possible_paths(firstPoint, length-1, remainTokens, ans_count)


def check_possible_paths(token, remainLen, remainTokens, ans_count):
    x, y = axis[token]

    for dx, dy in deltas:
        innerRemainTokens = remainTokens.copy()
        if check_next_step((x+dx, y+dy), (x, y), innerRemainTokens) == True:
            newToken = list(axis.keys())[list(axis.values()).index((x+dx, y+dy))]
            innerRemainTokens.remove(newToken)
            if remainLen == 1:
                ans_count += 1
            else:
                ans_count = check_possible_paths(
                    newToken, remainLen-1, innerRemainTokens, ans_count)

    return ans_count


def check_next_step(check_axis, ori_axis, remainTokens):
    x, y = check_axis
    ox, oy = ori_axis

    if not ( -1<=x<=1 and -1<=y<=1):
        return False

    newToken = list(axis.keys())[list(axis.values()).index((x, y))]
    if MIN_X <= x <= MAX_X and MIN_Y <= y <= MAX_Y and newToken in remainTokens and not betweenNoToken(ox+(x-ox)/2, oy+(y-oy)/2, remainTokens):
        # 而且Set裡面還有這個Token,而且和原點中間沒有token了
        return True
    else:
        return False


def betweenNoToken(bet_x, bet_y, remainTOkens):

    bet_axis = (bet_x, bet_y)

    if bet_axis in axis.values():
        if list(axis.keys())[list(axis.values()).index((bet_x, bet_y))] in remainTOkens:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    # tests = ['test_case7']
    tests = ['test_case1', 'test_case2', 'test_case3', 'test_case4', 'test_case5', 'test_case6', 'test_case7']
    # tests = ['test_case5', 'test_case6', 'test_case7']
    suite = unittest.TestSuite(map(TestScreenLokingPatterns, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)

    # test all
    # unittest.main(verbosity=2)
