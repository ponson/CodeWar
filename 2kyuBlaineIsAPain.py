import unittest


class BlaineIsaPainTest(unittest.TestCase):

    def testcase1(self):
        TRACK_EX = """\
                                    /------------\\
    /-------------\\                /             |
    |             |               /              S
    |             |              /               |
    |        /----+--------------+------\\        |   
    \\       /     |              |      |        |     
     \\      |     \\              |      |        |                    
     |      |      \\-------------+------+--------+---\\
     |      |                    |      |        |   |
     \\------+--------------------+------/        /   |
            |                    |              /    | 
            \\------S-------------+-------------/     |
                                 |                   |
    /-------------\\              |                   |
    |             |              |             /-----+----\\
    |             |              |             |     |     \\
    \\-------------+--------------+-----S-------+-----/      \\
                  |              |             |             \\
                  |              |             |             |
                  |              \\-------------+-------------/
                  |                            |               
                  \\----------------------------/ 
    """
        self.assertEqual(train_crash(TRACK_EX, "Aaaa", 147,
                         "Bbbbbbbbbbb", 288, 1000), 516)

    
    def testcase2(self):
        TRACK_EX = """\
        /-----------------\\
        |                 |
        |                 |
        |                 |
        |                 |
        \\-----------------/
                """
        self.assertEqual(train_crash(TRACK_EX, "aaaaaA", 10,
                         "bbbbbB", 30, 100), -1)

    def testcase3(self):
        TRACK_EX = """\
/------S----------\\
|                 |
|                 |
|                 |
|                 |
\\----------S------/
                """
        self.assertEqual(train_crash(TRACK_EX, "aaaaaaaaaaaaA", 7,
                         "xxxX", 30, 100), 34)


    def testcase4(self):
        TRACK_EX = """\
/------\\               /--\\
|      |               |  |
|      \\---------------/  |
\\------\\               /--/ 
       |               |
       \\---------------/
                """
        self.assertEqual(train_crash(TRACK_EX, "Cccccccccc", 60,
                         "eeE", 50, 2000), 5)
        
    def testcase5(self):
        TRACK_EX = """\
/---\\
|   |
\\--\\|
   ||
   |\\------\\
   |/----\\ |
   ||    | |
/--/|    | |
|   |    | |
\\---/    \\-/
                """
        self.assertEqual(train_crash(TRACK_EX, "Eee", 10,
                         "aaA", 20, 100), 22)
        

def track_parser(alltracks):
    initCheckDirect = {'-':((0, 1)), '|':((1, 0)), '/': (-1, 1), '\\': ((1, 1)), 'S':((0, 1))}
    validNextChars = {'-':('-','\\', '/', '+', 'S'), 
                      '|':('|','\\', '/', '+', 'S'),
                      '\\':('\\', '|', '-', 'X', 'S'),
                      '/':('/', '|', '-', 'X', 'S'),
                      '+':('/', '\\', '|', '-', 'X', '+', 'S'),
                      'X':('/', '\\', '|', '-', 'X', '+', 'S'),
                      'S':('/', '\\', '|', '-', 'X', '+') }
    keepSameDirection = {'-': {'-', '+', 'S'},
                         '|': {'|', '+', 'S'},
                         '/': {'/', 'X', 'S'},
                         '\\': {'\\', 'X', 'S'}}
    nextValidChars = {(0, 1): {'/':(-1, 1), '\\':(1, 1), '-':(0, 1), 'S':(0, 1), '+':(0, 1)},
                     (0,-1): {'/':(1,-1), '\\':(-1, -1), '-':(0, -1), 'S':(0, -1), '+':(0, -1)},
                     (1, 0): {'/':(1,-1), '\\':(1, 1), '|':(1, 0), 'S':(1, 0), '+':(1, 0)},
                     (-1,0): {'/':(-1,1), '\\':(-1,-1), '|':(-1, 0), 'S':(-1, 0), '+':(-1, 0)},
                     (1, 1): {'-':(0, 1), '|':(1, 0), '\\': (1, 1), 'S': (1, 1), 'X': (1, 1), '+': (0, 1)},
                     (-1, -1): {'-':(0,-1), '|':(-1, 0), '\\': (-1, -1), 'S': (-1, -1), 'X': (-1, -1), '+': (0, -1)},
                     (-1, 1): {'-':(0, 1), '|':(-1, 0), '/': (-1, 1), 'S': (-1, 1), 'X': (-1, 1), '+': (0, 1)},
                     (1, -1): {'-':(0, -1), '|':(1, 0), '/': (1, -1), 'S': (1, -1), 'X': (1, -1), '+': (0, -1)}}
    directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]
    checkSteps = {(-1, 1): [[(-1, 0), '|S+'], [(-1, 1), '/XS+'], [(0, 1), '-S+']], 
                  (0, 1): [ [(-1, 1), ''], [(0, 1), '-S+/\\'], [(1, 1), '']], 
                  (1, 1): [[(0, 1), '-S+'], [(1, 1), '\\XS'], [(1, 0), '|S+']],
                  (1, 0): [[(1, 1), ''], [(1, 0), '|+S\\/'], [(1, -1), '']], 
                  (1, -1): [[(1, 0), '|S+'], [(1, -1), '/XS'], [(0, -1), '-S+']],
                  (0, -1): [[(1, -1), ''], [(0, -1), '-S+\\/'], [(-1, -1), '']], 
                  (-1, -1): [[(0, -1), '-S+'], [(-1, -1), '\\XS'], [(-1, 0), '|S+']], 
                  (-1, 0): [[(-1, 1), ''], [(-1, -1), ''], [(-1, 0), '|S+\\/']]}

    trackRows = alltracks.split('\n')
    tracks = []
    tmaps = {}
    for idx in range(len(trackRows[0])):
        if trackRows[0][idx] != ' ':
            tracks.append(((0, idx), trackRows[0][idx]))
            tmaps[(0, idx)] = [0]
            break

    print(f"The original pos is: ({tracks[0]})")

    parseConti = True
    curDirect = initCheckDirect[tracks[0][1]]
    curPos = tracks[-1][0]
    curChar = tracks[-1][1]
    while parseConti:
        #next position choice
        dirIdx = directions.index(curDirect)
        for l in checkSteps[curDirect]:
            delta = l[0]
            validchars = l[1]
            # delta = directions[(dirIdx+df)%8]
            candiPos = (curPos[0]+delta[0] , curPos[1]+delta[1])
            #check boundary
            rows = len(trackRows)
            if candiPos[0] >= 0 and candiPos[0] < rows and candiPos[1] >=0 and candiPos[1] < len(trackRows[candiPos[0]]):
                if trackRows[candiPos[0]][candiPos[1]] in validchars:
                    if candiPos == tracks[0][0]:
                        parseConti = False
                        break
                    nextPos = candiPos
                    nextChar = trackRows[nextPos[0]][nextPos[1]]
                    tracks.append((nextPos, nextChar))
                    if nextPos not in tmaps.keys():
                        tmaps[nextPos] = [len(tracks)-1]
                    else:
                        tmaps[nextPos].append(len(tracks)-1)
                    curPos = nextPos
                    curChar = nextChar
                    curDirect = nextValidChars[delta][curChar]
                    break

    # print(f"tracks={tracks}")
    return tracks


def set_trains(train, pos, c):

    if train[0] == 'X' or train[-1] == 'X':
        tType = 'X'
    else:
        tType = 'N'

    if train[0].isupper():
        direction = -1
    else:
        direction = 1

    # if c == 'S' and tType == 'N':
    #     stop = len(train) - 1
    # else:
    #     stop = 0

    return [pos, tType, len(train), direction, len(train)-1, 0]

        
def check_collisions(ptrains):
    for t in ptrains:
        if len(t[6]) != len(set(t[6])):
            return True

    return not set(ptrains[0][6]).isdisjoint(set(ptrains[1][6]))
    

def train_crash(track, a_train, a_train_pos, b_train, b_train_pos, limit):
    trains = []
    tracks = track_parser(track)
    trains.append(set_trains(a_train, a_train_pos, tracks[a_train_pos][1]))
    trains.append(set_trains(b_train, b_train_pos, tracks[b_train_pos][1]))
    for t in trains:
        tpos =[]
        for tidx in range(t[2]):
            # tpos.append(tracks[(t[0]+(tidx*t[3]))%len(tracks)][0])
            tpos.append(tracks[(t[0]+(tidx*t[3]*(-1)))%len(tracks)][0])
        t.append(tpos)
    if check_collisions(trains):
        return 0

    for step in range(1, limit+1):
        for train in trains:
            if train[5] > 0:
                train[5] -= 1
            else:
                train[0] += train[3]
                tHead = tracks[train[0]%len(tracks)][0]
                train[6].insert(0, tHead)
                train[6].pop(-1)
                if tracks[train[0]%len(tracks)][1] == 'S' and train[1] == 'N':
                    train[5] = train[4]

        if check_collisions(trains):
            return step 

    return -1



if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4',  'testcase5']
    testparts = ['testcase1']
    testOne = ['testcase3']
    # suite = unittest.TestSuite(map(BlaineIsaPainTest, testOne))
    suite = unittest.TestSuite(map(BlaineIsaPainTest, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
