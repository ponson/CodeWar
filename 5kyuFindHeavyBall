import unittest


class TestFindHeavyBall(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(find_ball(example_first), 7)
        self.assertEqual(find_ball(example_second), 2)
        self.assertEqual(find_ball(example_third), 6)


class Scale():

    def __init__(self, balls):
        self.balls = balls
        self.checkUsage = 0


    def get_weight(self, lefts, rights):
        self.checkUsage += 1

        if self.checkUsage > 2:
            AssertionError()
        
        l = sum([self.balls[i] for i in lefts]) 
        r = sum([self.balls[i] for i in rights])

        if l > r: return -1
        if l < r: return 1
        return 0

def find_ball(scales):
    # call scales.get_weight() at most TWICE
    # return indexOfHeavierBall

    #Test First
    test1 = scales.get_weight(range(0, 3), range(3, 6))
    if test1 == 0:
        #Test Second
        test2 = scales.get_weight([6], [7])
        return 6 if test2 == -1 else 7

    elif test1 == -1:
        #Test Second
        test2 = scales.get_weight([0], [1])
        if test2 == 0: return 2
        return 0 if test2 == -1 else 1
    
    else:
        #Test Second
        test2 = scales.get_weight([3], [4])
        if test2 == 0: return 5
        return 3 if test2 == -1 else 4


if __name__ == '__main__':
    example_first = Scale([1,1,1,1,1,1,1,7])
    example_second = Scale([1,1,2,1,1,1,1,1])
    example_third = Scale([1,1,1,1,1,1,6,1])
    unittest.main(verbosity=2)