import unittest


class TestInstantRunOffVoting(unittest.TestCase):

    def test_case1(self):
        voters = [["dem", "ind", "rep"],
                  ["rep", "ind", "dem"],
                  ["ind", "dem", "rep"],
                  ["ind", "rep", "dem"]]

        self.assertEqual(runoff(voters), "ind")

    def test_case2(self):
        voters = [["a", "c", "d", "e", "b"],
                  ["e", "b", "d", "c", "a"],
                  ["d", "e", "c", "a", "b"],
                  ["c", "e", "d", "b", "a"],
                  ["b", "e", "a", "c", "d"]]
        self.assertEqual(runoff(voters), None)

    def test_case3(self):
        voters = [['d', 'a', 'e', 'b', 'c'],
                  ['b', 'e', 'd', 'c', 'a'],
                  ['e', 'a', 'c', 'b', 'd'],
                  ['e', 'd', 'a', 'b', 'c'],
                  ['d', 'b', 'a', 'e', 'c']]
        self.assertEqual(runoff(voters), 'e')

    def test_case4(self):
        voters = [['a', 'b', 'c', 'd', 'e'],
                  ['c', 'b', 'd', 'e', 'a'],
                  ['b', 'c', 'a', 'd', 'e'],
                  ['d', 'b', 'e', 'a', 'c'],
                  ['c', 'a', 'b', 'e', 'd'],
                  ['a', 'e', 'b', 'c', 'd']]

        self.assertEqual(runoff(voters), None)

def runoff(voters):
    # Init highest vote index to some candidate
    highest_candiate_index = {}
    candidateGotVotes = {}
    for candiate in voters[0]:
        highest_candiate_index[candiate] = {}
        candidateGotVotes[candiate] = 0

    numOfCandidate = len(voters[0])
    numOfVotes = len(voters)
    votesDone = False
    checkVotes = list(range(numOfVotes))
    removed_candidates = []
    removedCnt = 0

    for i in checkVotes:
        highest_candiate_index[voters[i][0]][i] = 0 

    while votesDone == False:

        # TODO Get each candidate's votes
        for k in candidateGotVotes.keys():
            candidateGotVotes[k] = len(highest_candiate_index[k])
        # TODO check if someone has won

        if max(candidateGotVotes.values()) > numOfVotes / 2:
            for (key, value) in candidateGotVotes.items():
                if value == max(candidateGotVotes.values()):
                    return key  # Got the winner
        # TODO compare the smallest votes of candidates
        else:
            for (key, value) in candidateGotVotes.items():
                if value == min(candidateGotVotes.values()):
                    removed_candidates.append(key)
            for rCandidate in removed_candidates:
                candidateGotVotes.pop(rCandidate)
        # TODO remove the lost candidates
        for rCandidate in removed_candidates:
            for vote_i, pri_i in highest_candiate_index[rCandidate].items():
                pri_i += 1
                while pri_i < numOfCandidate:
                    if voters[vote_i][pri_i] in candidateGotVotes.keys():
                        highest_candiate_index[voters[vote_i][pri_i]][vote_i] = pri_i
                        break
                    else:
                        pri_i += 1
        for rCandidate in removed_candidates:
            removedCnt += 1
            highest_candiate_index[rCandidate] = {}

        removed_candidates = []

        if removedCnt == numOfCandidate:
            votesDone = True

    return None


if __name__ == '__main__':
    tests = ['test_case1', 'test_case2', 'test_case3', 'test_case4']
    # tests = ['test_case4']
    # suite = (unittest.TestLoader().loadTestsFromTest)
    suite = unittest.TestSuite(map(TestInstantRunOffVoting, tests))
    # unittest.main(verbosity=2)
    unittest.TextTestRunner(verbosity=2).run(suite)
