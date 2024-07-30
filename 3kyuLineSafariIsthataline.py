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


def path_check(start, end, grid, rlen, clen, hlcnt, vlcnt, pluslcnt):

    pathpoints = []
    stepcnt = 0
    curRow, curCol = start[0], start[1]
    findNext = True
    direction = None
    curhcnt, curvcnt, curpluscnt = 0, 0, 0
    dtmoves = {'UP': -1, 'DOWN': 1, 'LEFT': -1, 'RIGHT': 1}
    
    while findNext:
        if [curRow, curCol] in pathpoints:
            break
        else:
            pathpoints.append([curRow, curCol])

        if grid[curRow][curCol] == 'X':
            # Check four direction items
            nears = {}
            if curRow+1 < rlen and grid[curRow+1][curCol] != ' ':
                nears['DOWN']= grid[curRow+1][curCol]
            if curRow-1 >= 0 and grid[curRow-1][curCol] != ' ':
                nears['UP']= grid[curRow-1][curCol]
            if curCol-1 >= 0 and grid[curRow][curCol-1] != ' ':
                nears['LEFT']= grid[curRow][curCol-1]
            if curCol+1 < clen and grid[curRow][curCol+1] != ' ':
                nears['RIGHT']= grid[curRow][curCol+1]
            if 'X' in nears.values():
                if hlcnt == curhcnt and vlcnt == curvcnt and pluslcnt == curpluscnt:
                    return True, stepcnt
                else:
                    return False, 0
            for k, v in nears.items():
                #Check UP or DOWN
                if k == 'UP' or k == 'DOWN':
                    curRow += dtmoves[k]
                    if v == '|':
                        direction = k
                    elif v == '+':
                        direction = 'LEFTRIGHT'
                    else:
                        curRow -= dtmoves[k]
                else:
                    curCol += dtmoves[k]
                    if v == '-':
                        direction = k
                    elif v == '+':
                        direction = 'UPDOWN'
                    else:
                        curCol -= dtmoves[k]
            
            if len(nears) == 0:
                findNext = False

        elif grid[curRow][curCol] == '-':
            stepcnt += 1
            curhcnt += 1
            nextCol = curCol + dtmoves[direction]
            if nextCol >= 0 and nextCol < clen:
                curCol = nextCol
                if grid[curRow][nextCol] == '-':
                    continue
                elif grid[curRow][nextCol] == '+':
                    direction = "UPDOWN"
                    continue
                elif grid[curRow][nextCol] == 'X':
                    findNext = False

        elif grid[curRow][curCol] == '|':
            stepcnt += 1
            curvcnt += 1
            nextRow = curRow + dtmoves[direction]
            if nextRow >= 0 and nextRow < rlen:
                curRow = nextRow
                if grid[nextRow][curCol] == '|':
                    continue
                elif grid[nextRow][curCol] == '+':
                    direction = 'LEFTRIGHT'
                    continue
                elif grid[nextRow][curCol] == 'X':
                    findNext = False

        elif grid[curRow][curCol] == '+':
            stepcnt += 1
            curpluscnt += 1
            checkvalid = 0
            # Check UP or DOWN
            if direction == 'UPDOWN':
                # Check UP side
                nextRow = curRow - 1
                if nextRow >= 0 and [nextRow, curCol] not in pathpoints:
                    if grid[nextRow][curCol] == '|' or (grid[nextRow][curCol] == '+' and ((nextRow - 1 >= 0 and grid[nextRow-1][curCol] != '|') or nextRow-1 < 0)):
                        checkvalid += 1
                        shiftmove = -1
                    elif grid[nextRow][curCol] == 'X':
                        curRow = nextRow
                        findNext = False

                # Check DOWN side
                nextRow = curRow + 1
                if nextRow < rlen and [nextRow, curCol] not in pathpoints:
                    if grid[nextRow][curCol] == '|' or (grid[nextRow][curCol] == '+' and ((nextRow + 1 < rlen and grid[nextRow+1][curCol] != '|') or nextRow+1 >= rlen)):
                        checkvalid += 1
                        shiftmove = 1
                    elif grid[nextRow][curCol] == 'X':
                        curRow = nextRow
                        findNext = False

                if checkvalid >= 2: #Ambigous!
                    findNext = False
                elif checkvalid == 1:
                    curRow += shiftmove
                    if shiftmove == -1 or shiftmove == 1:
                        if grid[curRow][curCol] == '|':
                            if shiftmove == -1:
                                direction = 'UP'
                            else:
                                direction = 'DOWN'
                        else:
                            direction = 'LEFTRIGHT'

            # Check LEFT or RIGHT
            else:
                shiftmove = 0
                # Check LEFT side
                nextCol = curCol - 1
                if nextCol >= 0 and [curRow, nextCol] not in pathpoints:
                    if grid[curRow][nextCol] == '-' or (grid[curRow][nextCol] == '+' and ((nextCol - 1 >= 0 and grid[curRow][nextCol-1] != '-') or nextCol-1 < 0)):
                        shiftmove = -1
                        checkvalid += 1
                    elif grid[curRow][nextCol] == 'X':
                        curCol = nextCol
                        findNext = False

                # Check RIGHT side
                nextCol = curCol + 1
                if nextCol < clen and [curRow, nextCol] not in pathpoints:
                    if grid[curRow][nextCol] == '-' or (grid[curRow][nextCol] == '+' and ((nextCol + 1 < rlen and grid[curRow][nextCol-1] != '-') or nextCol+1 >= rlen)):
                        shiftmove = 1
                        checkvalid += 1
                    elif grid[curRow][nextCol] == 'X':
                        curCol = nextCol
                        findNext = False

                if checkvalid >= 2: #Ambigous!
                    findNext = False
                elif checkvalid == 1:
                    curCol += shiftmove
                    if shiftmove == -1 or shiftmove == 1:
                        if grid[curRow][curCol] == '-':
                            if shiftmove == -1:
                                direction = 'LEFT'
                            else:
                                direction = 'RIGHT'
                        else:
                            direction = 'UPDOWN'

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
    tests = ['testgood1', 'testgood2', 'testgood3', 'testgood4', 'testgood5', 'testgood6', 'testgood7',
             'testbad1', 'testbad2', 'testbad3', 'testbad4', 'testbad5', 'testbad6', 'testbad7', 'testbad8']
    testparts = ['testgood1', 'testgood2',
                 'testgood3', 'testgood4', 'testgood5']
    testOne = ['testgood9']
    suite = unittest.TestSuite(map(LineValidTest, testOne))
    # suite = unittest.TestSuite(map(LineValidTest, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
