import unittest

class TestBowllingScore(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(bowling_score('11 11 11 11 11 11 11 11 11 11'), 20)
        self.assertEqual(bowling_score('X X X X X X X X X XXX'), 300)
        self.assertEqual(bowling_score('9/ 9/ 9/ 9/ 9/ 9/ 9/ 9/ 9/ 9/2'), 183)

def bonus_score(b1, b2=0):
    if b1 == 'X' and b2 == 'X':
        return 20
    elif b2 == '/':
        return 10
    elif b1 == 'X':
        return 10 + int(b2)
    else:
        return int(b1) + int(b2)


def bowling_score(frames):
    #1 create lists from frames
    frame_lists = [list(oneframe) for oneframe in frames.split()]
    frame_idxes = [0]
    for i in range(len(frame_lists)-1):
        frame_idxes.append(frame_idxes[i]+len(frame_lists[i]))
    shots = frames.replace(' ', '')
    # print(frame_lists)
    # print(frame_idxes)
    # print(shots)
    
    #2 Sum each score of frame
    sum = 0
    for i in range(len(frame_lists)):
        if shots[frame_idxes[i]] == 'X':
            sum += (10 + bonus_score(shots[frame_idxes[i]+1], shots[frame_idxes[i]+2]))
        elif shots[frame_idxes[i]+1] == '/':
            sum += (10 + bonus_score(shots[frame_idxes[i]+2]))
        else:
            sum += (int(shots[frame_idxes[i]]) + int(shots[frame_idxes[i]+1]))

    return sum
    
    #2 create bonus count

if __name__ == '__main__':
    unittest.main(verbosity=2)