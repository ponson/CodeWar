import unittest


class Test_compute_ranks(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(compute_ranks(6,
                                       [[0, 5, 2, 2],
                                        [1, 4, 0, 2],
                                        [2, 3, 1, 2],
                                        [1, 5, 2, 2],
                                        [2, 0, 1, 1],
                                        [3, 4, 1, 1],
                                        [2, 5, 0, 2],
                                        [3, 1, 1, 1],
                                        [4, 0, 2, 0]]),
                         [4, 4, 6, 3, 1, 2])

    def testcase2(self):
        self.assertEqual(compute_ranks(6,
                                       [[0, 5, 2, 0],
                                        [1, 4, 2, 2],
                                        [2, 3, 1, 3],
                                        [1, 5, 0, 0],
                                        [2, 0, 2, 1],
                                        [3, 4, 3, 1]]),
                         [2, 3, 4, 1, 5, 6])
        
    def testcase3(self):
        self.assertEqual(compute_ranks(4,
                                       [[0, 3, 1, 1],
                                        [1, 2, 2, 2],
                                           [1, 3, 2, 0],
                                           [2, 0, 2, 0]]),
                         [3, 1, 1, 3])

    def testcase4(self):
        self.assertEqual(compute_ranks(10, []),
                         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    def testcase5(self):
        self.assertEqual(compute_ranks(8, [[0, 7, 2, 0]]),
                         [1, 2, 2, 2, 2, 2, 2, 8])


def compute_ranks(number, games):
    rankit = 1
    ranks = [0] * number
    points = [0] * number
    scores = [0] * number
    diffscore = [0] * number
    #TODO 1: parsing the games result
    for game in games:
        scores[game[0]] += game[2]
        diffscore[game[0]] += (game[2] - game[3])
        scores[game[1]] += game[3]
        diffscore[game[1]] += (game[3] - game[2])
        if game[2] > game[3]:
            points[game[0]] += 2
        elif game[3] > game[2]:
            points[game[1]] += 2
        else:
            points[game[0]] += 1
            points[game[1]] += 1

    #TODO 2: Ranking...
    dictPoints = {}
    for idx, p in enumerate(points):
        if p not in dictPoints.keys():
            dictPoints[p] = [idx]
        else:
            dictPoints[p].append(idx)

    lkeys = list(dictPoints.keys())
    lkeys.sort()
    lkeys.reverse()
    for p in lkeys:
        if len(dictPoints[p]) == 1:
            ranks[dictPoints[p][0]] = rankit
            rankit += 1
        else:
            samepDiff = {}
            for team in dictPoints[p]:
                if diffscore[team] not in samepDiff.keys():
                    samepDiff[diffscore[team]] = [team]
                else:
                    samepDiff[diffscore[team]].append(team)

            spkeys = list(samepDiff.keys())
            spkeys.sort()
            spkeys.reverse()
            for sd in spkeys:
                if len(samepDiff[sd]) == 1:
                    ranks[samepDiff[sd][0]] = rankit
                    rankit += 1
                else:
                    samedfScore = {}
                    for team in samepDiff[sd]:
                        if scores[team] not in samedfScore.keys():
                            samedfScore[scores[team]] = [team]
                        else:
                            samedfScore[scores[team]].append(team)
                    sdfkeys = list(samedfScore.keys())
                    sdfkeys.sort()
                    sdfkeys.reverse()
                    for score in sdfkeys:
                        if len(samedfScore[score]) == 1:
                            ranks[samedfScore[score][0]] = rankit
                            rankit += 1
                        else:
                            for team in samedfScore[score]:
                                ranks[team] = rankit
                            rankit += len(samedfScore[score])

    print(f'rank={ranks}')
    return ranks






if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4',
             'testcase5']
    testOne = ['testcase2']
    suite = unittest.TestSuite(map(Test_compute_ranks, tests))
    # suite = unittest.TestSuite(map(Test_compute_ranks, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)
