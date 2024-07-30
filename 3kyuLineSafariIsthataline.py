import unittest


def show(grid):
    print('\n'.join(grid))
    return grid


class LineValidTest(unittest.TestCase):

    def testgood1(self):
        grid = ["           ",
                "X---------X",
                "           ",
                "           "]
        self.assertEqual(line(show(grid)), True)

    def testgood2(self):
        grid = ["     ",
                "  X  ",
                "  |  ",
                "  |  ",
                "  X  "]
        self.assertEqual(line(show(grid)), True)

    def testgood3(self):
        grid = ["                    ",
                "     +--------+     ",
                "  X--+        +--+  ",
                "                 |  ",
                "                 X  ",
                "                    "]
        self.assertEqual(line(show(grid)), True)

    def testgood4(self):
        grid = ["                     ",
                "    +-------------+  ",
                "    |             |  ",
                " X--+      X------+  ",
                "                     "]
        self.assertEqual(line(show(grid)), True)

    def testgood5(self):
        grid = ["                      ",
                "   +-------+          ",
                "   |      +++---+     ",
                "X--+      +-+   X     "]
        self.assertEqual(line(show(grid)), True)

    def testgood6(self):
        grid = ["              ",
                "              ",
                "     XX       ",
                "              "]
        self.assertEqual(line(show(grid)), True)

    def testgood7(self):
        grid = ["              ",
                "              ",
                "      X       ",
                "      X       "]
        self.assertEqual(line(show(grid)), True)

    def testgood8(self):
        grid = ["   X     X  ",
                "   ++++  +-+",
                "    +++--+ |",
                "         +-+"]
        self.assertEqual(line(show(grid)), True)


    def testgood9(self):
        grid = [" +-----+  ",
                " |+---+|  ",
                " ||+-+||  ",
                " |||X+||  ",
                " X|+--+|  ",
                "  +----+  "]
        self.assertEqual(line(show(grid)), True)

    def testbad1(self):
        grid = ["X-----|----X"]
        self.assertEqual(line(show(grid)), False)

    def testbad2(self):
        grid = [" X  ",
                " |  ",
                " +  ",
                " X  "]
        self.assertEqual(line(show(grid)), False)

    def testbad3(self):
        grid = ["   |--------+    ",
                "X---        ---+ ",
                "               | ",
                "               X "]
        self.assertEqual(line(show(grid)), False)

    def testbad4(self):
        grid = ["              ",
                "   +------    ",
                "   |          ",
                "X--+      X   ",
                "              "]
        self.assertEqual(line(show(grid)), False)

    def testbad5(self):
        grid = ["      +------+",
                "      |      |",
                "X-----+------+",
                "      |       ",
                "      X       "]
        self.assertEqual(line(show(grid)), False)

    def testbad6(self):
        grid = ["              ",
                "              ",
                "     X        ",
                "      X       "]
        self.assertEqual(line(show(grid)), False)

    def testbad7(self):
        grid = ["              ",
                " XX---+       ",
                " |    |       ",
                " |    |       ",
                " |    |       ",
                " +----+       "]
        self.assertEqual(line(show(grid)), False)

    def testbad8(self):
        grid = ["    ++       ",
                "   ++++      ",
                "   ++++      ",
                "  X-++-X     "]
        self.assertEqual(line(show(grid)), False)


def in_borders(r, c, rMax, cMax):
    if r<rMax and c<cMax and r>=0 and c>=0:
        return True
    else:
        return False

def path_check(start, end, grid, rlen, clen, hlcnt, vlcnt, pluslcnt):

    pathpoints = []
    stepcnt = 0
    curRow, curCol = start[0], start[1]
    findNext = True
    direction = None
    curhcnt, curvcnt, curpluscnt = 0, 0, 0
    dtmoves = {'UP': (-1, 0, '|+X', 'LEFTRIGHT'), 'DOWN': (1, 0, '|+X', 'LEFTRIGHT'), 'LEFT': (0, -1, '-+X', 'UPDOWN'), 'RIGHT': (0, 1, '-+X', 'UPDOWN')}
    plusmoves = {'UPDOWN': ([(-1, 0), (1, 0)], '|', ('UP', 'DOWN', 'LEFTRIGHT')), 'LEFTRIGHT': ([(0, -1), (0, 1)], '-', ('LEFT', 'RIGHT', 'UPDOWN'))}
    
    while findNext:
        if [curRow, curCol] in pathpoints:
            break
        else:
            pathpoints.append([curRow, curCol])

        if grid[curRow][curCol] == 'X':
            # Check four direction items
            nears = {}
            for k, v in dtmoves.items():
                if in_borders(curRow+v[0], curCol+v[1], rlen, clen) and grid[curRow+v[0]][curCol+v[1]] != ' ':
                    nears[k] = grid[curRow+v[0]][curCol+v[1]]
            
            for k, v in nears.items():  #k=Directions, v=char
                #Check UP or DOWN
                curRow += dtmoves[k][0]
                curCol += dtmoves[k][1]
                if v == dtmoves[k][2][0]: # | or -
                    direction = k
                elif v == dtmoves[k][2][1]: # + 
                    direction = dtmoves[k][3]
                elif v == dtmoves[k][2][2]: # X
                    if hlcnt == curhcnt and vlcnt == curvcnt and pluslcnt == curpluscnt:
                        return True, stepcnt
                    else:
                        return False, 0
                else:
                    curRow -= dtmoves[k][0]
                    curCol -= dtmoves[k][1]
            
            if len(nears) == 0:
                findNext = False

        elif grid[curRow][curCol] == '-' or grid[curRow][curCol] == '|':
            stepcnt += 1
            if grid[curRow][curCol] == '-':
                curhcnt += 1
            else:
                curvcnt += 1
            nextRow = curRow + dtmoves[direction][0]
            nextCol = curCol + dtmoves[direction][1]
            if in_borders(nextRow, nextCol, rlen, clen):
                curRow = nextRow
                curCol = nextCol
                if grid[nextRow][nextCol] == dtmoves[direction][2][0]:
                    continue
                elif grid[nextRow][nextCol] == '+':
                    direction = dtmoves[direction][3]
                    continue
                else:
                    findNext = False

        elif grid[curRow][curCol] == '+':
            stepcnt += 1
            curpluscnt += 1
            checkvalid = 0
            for idx, delta in enumerate(plusmoves[direction][0]):
                nextRow = curRow + delta[0]
                nextCol = curCol + delta[1]
                if in_borders(nextRow, nextCol, rlen, clen) and [nextRow, nextCol] not in pathpoints:
                    if grid[nextRow][nextCol] == plusmoves[direction][1] or (grid[nextRow][nextCol] == '+' and (in_borders(nextRow+delta[0], nextCol+delta[1], rlen, clen)==False or grid[nextRow+delta[0]][nextCol+delta[1]] != plusmoves[direction][1])):
                        checkvalid += 1
                        shiftmove = delta
                        nextdirect = idx
                    elif grid[nextRow][nextCol] == 'X':
                        curRow, curCol = nextRow, nextCol
                        findNext = False
            
            if checkvalid >= 2: #Ambigous!
                return False, 0
            elif checkvalid == 1:
                curRow += shiftmove[0]
                curCol += shiftmove[1]
                if grid[curRow][curCol] == plusmoves[direction][1]:
                    direction = plusmoves[direction][2][nextdirect]
                else:
                    direction = plusmoves[direction][2][2]

    if grid[curRow][curCol] == 'X' and [curRow, curCol] != start and hlcnt == curhcnt and vlcnt == curvcnt and pluslcnt == curpluscnt:
        return True, stepcnt
    else:
        return False, stepcnt


def line(grid):
    rows, cols = len(grid), len(grid[0])
    Xpos = []
    hlcount, vlcount, pluslcount = 0, 0, 0
    for r in range(rows):
        xIdxs = [i for i, c in enumerate(grid[r]) if c == 'X']
        for idx in xIdxs:
            Xpos.append([r, idx])
        hlcount += grid[r].count('-')
        vlcount += grid[r].count('|')
        pluslcount += grid[r].count('+')

    if len(Xpos) != 2:
        return False

    validpathcnt = 0

    pathstep = []
    for Xidx in range(2):
        sPos = Xpos[Xidx]
        ePos = Xpos[(Xidx + 1) % 2]
        Xidx += 1
        result, stepcnt = path_check(
            sPos, ePos, grid, rows, cols, hlcount, vlcount, pluslcount)
        if result:
            pathstep.append(stepcnt)
            validpathcnt += 1

    if validpathcnt == 1 or (validpathcnt == 2 and pathstep[0] == pathstep[1]):
        return True
    else:
        return False

if __name__ == '__main__':
    tests = ['testgood1', 'testgood2', 'testgood3', 'testgood4', 'testgood5', 'testgood6', 'testgood7', 'testgood8', 'testgood9',
             'testbad1', 'testbad2', 'testbad3', 'testbad4', 'testbad5', 'testbad6', 'testbad7', 'testbad8']
    testparts = ['testgood1', 'testgood2',
                 'testgood3', 'testgood4', 'testgood5']
    testOne = ['testbad1']
    # suite = unittest.TestSuite(map(LineValidTest, testOne))
    suite = unittest.TestSuite(map(LineValidTest, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
