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
    isX = False
    while findNext:
        if grid[curRow][curCol] == 'X':
            if [curRow, curCol] in pathpoints:
                findNext = False
            else:
                pathpoints.append([curRow, curCol])
            # Check four direction items
            nears = []
            if curRow+1 < rlen and grid[curRow+1][curCol] != ' ':
                nears.append(grid[curRow+1][curCol])
            if curRow-1 >= 0 and grid[curRow-1][curCol] != ' ':
                nears.append(grid[curRow-1][curCol])
            if curCol-1 >= 0 and grid[curRow][curCol-1] != ' ':
                nears.append(grid[curRow][curCol-1])
            if curCol+1 < clen and grid[curRow][curCol+1] != ' ':
                nears.append(grid[curRow][curCol+1])
            if 'X' in nears:
                isX = True
            else:
                isX = False
            # Check DOWN
            if curRow+1 < rlen and grid[curRow+1][curCol] != ' ' and (grid[curRow+1][curCol] != 'X' or isX == True):
                if grid[curRow+1][curCol] == '|':
                    curRow += 1
                    direction = 'DOWN'
                    continue
                elif grid[curRow+1][curCol] == '+':
                    curRow += 1
                    direction = 'LEFTRIGHT'
                    continue
                elif grid[curRow+1][curCol] == 'X':
                    curRow += 1
                    findNext = False

            # Check UP
            elif curRow-1 >= 0 and grid[curRow-1][curCol] != ' ' and (grid[curRow-1][curCol] != 'X' or isX == True):
                if grid[curRow-1][curCol] == '|':
                    curRow -= 1
                    direction = 'UP'
                    continue
                elif grid[curRow-1][curCol] == '+':
                    curRow -= 1
                    direction = 'LEFTRIGHT'
                    continue
                elif grid[curRow-1][curCol] == 'X':
                    curRow -= 1
                    findNext = False
            # Check LEFT
            elif curCol-1 >= 0 and grid[curRow][curCol-1] != ' ' and (grid[curRow][curCol-1] != 'X' or isX == True):
                if grid[curRow][curCol-1] == '-':
                    curCol -= 1
                    direction = 'LEFT'
                    continue
                elif grid[curRow][curCol-1] == '+':
                    curCol -= 1
                    direction = 'UPDOWN'
                    continue
                elif grid[curRow][curCol-1] == 'X':
                    curCol -= 1
                    findNext = False
            # Check RIGHT
            elif curCol+1 < clen and grid[curRow][curCol+1] != ' ' and (grid[curRow][curCol+1] != 'X' or isX == True):
                if grid[curRow][curCol+1] == '-':
                    curCol += 1
                    direction = 'RIGHT'
                    continue
                elif grid[curRow][curCol+1] == '+':
                    curCol += 1
                    direction = 'UPDOWN'
                    continue
                elif grid[curRow][curCol+1] == 'X':
                    curCol += 1
                    findNext = False
            else:
                findNext = False

        elif grid[curRow][curCol] == '-':
            stepcnt += 1
            if [curRow, curCol] in pathpoints:
                findNext = False
            else:
                pathpoints.append([curRow, curCol])
            curhcnt += 1
            # Check LEFT or RIGHT
            if direction == 'LEFT':
                nextCol = curCol - 1
            else:
                nextCol = curCol + 1
            if nextCol >= 0 and nextCol < clen:
                if grid[curRow][nextCol] == '-':
                    curCol = nextCol
                    continue
                elif grid[curRow][nextCol] == '+':
                    curCol = nextCol
                    direction = "UPDOWN"
                    continue
                elif grid[curRow][nextCol] == 'X':
                    curCol = nextCol
                    findNext = False

        elif grid[curRow][curCol] == '|':
            stepcnt += 1
            if [curRow, curCol] in pathpoints:
                findNext = False
            else:
                pathpoints.append([curRow, curCol])
            curvcnt += 1
            # Check UP or DOWN
            if direction == 'UP':
                nextRow = curRow - 1
            else:
                nextRow = curRow + 1
            if nextRow >= 0 and nextRow < rlen:
                if grid[nextRow][curCol] == '|':
                    curRow = nextRow
                    continue
                elif grid[nextRow][curCol] == '+':
                    curRow = nextRow
                    direction = 'LEFTRIGHT'
                    continue
                elif grid[nextRow][curCol] == 'X':
                    curRow = nextRow
                    findNext = False

        elif grid[curRow][curCol] == '+':
            stepcnt += 1
            if [curRow, curCol] in pathpoints:
                findNext = False
            else:
                pathpoints.append([curRow, curCol])
            curpluscnt += 1
            # Check UP or DOWN
            if direction == 'UPDOWN':
                # Check UP side
                nextRow = curRow - 1
                if nextRow >= 0 and [nextRow, curCol] not in pathpoints:
                    if grid[nextRow][curCol] == '|' or (grid[nextRow][curCol] == '+' and ((nextRow - 1 >= 0 and grid[nextRow-1][curCol] != '|') or nextRow-1 < 0)):
                        curRow = nextRow
                        if grid[nextRow][curCol] == '|':
                            direction = 'UP'
                        else:
                            direction = 'LEFTRIGHT'
                        continue
                    elif grid[nextRow][curCol] == 'X':
                        curRow = nextRow
                        findNext = False

                # Check DOWN side
                nextRow = curRow + 1
                if nextRow < rlen and [nextRow, curCol] not in pathpoints:
                    if grid[nextRow][curCol] == '|' or (grid[nextRow][curCol] == '+' and ((nextRow + 1 < rlen and grid[nextRow+1][curCol] != '|') or nextRow+1 >= rlen)):
                        curRow = nextRow
                        if grid[nextRow][curCol] == '|':
                            direction = 'DOWN'
                        else:
                            direction = 'LEFTRIGHT'
                        continue
                    elif grid[nextRow][curCol] == 'X':
                        curRow = nextRow
                        findNext = False

            # Check LEFT or RIGHT
            else:
                # Check LEFT side
                nextCol = curCol - 1
                if nextCol >= 0 and [curRow, nextCol] not in pathpoints:
                    if grid[curRow][nextCol] == '-' or (grid[curRow][nextCol] == '+' and ((nextCol - 1 >= 0 and grid[curRow][nextCol-1] != '-') or nextCol-1 < 0)):
                        curCol = nextCol
                        if grid[curRow][nextCol] == '-':
                            direction = 'LEFT'
                        else:
                            direction = 'UPDOWN'
                        continue
                    elif grid[curRow][nextCol] == 'X':
                        curCol = nextCol
                        findNext = False

                # Check RIGHT side
                nextCol = curCol + 1
                if nextCol < clen and [curRow, nextCol] not in pathpoints:
                    if grid[curRow][nextCol] == '-' or (grid[curRow][nextCol] == '+' and ((nextCol + 1 < rlen and grid[curRow][nextCol-1] != '-') or nextCol+1 >= rlen)):
                        curCol = nextCol
                        if grid[curRow][nextCol] == '-':
                            direction = 'RIGHT'
                        else:
                            direction = 'UPDOWN'
                        continue
                    elif grid[curRow][nextCol] == 'X':
                        curCol = nextCol
                        findNext = False

    if grid[curRow][curCol] == 'X' and [curRow, curCol] != start and hlcnt == curhcnt and vlcnt == curvcnt and pluslcnt == curpluscnt:
        if isX and (curhcnt+curvcnt+curpluscnt > 0):
            return False, stepcnt
        else:
            return True, stepcnt
    else:
        return False, stepcnt


def line(grid):
    rows = len(grid)
    cols = len(grid[0])
    print(f"cols={cols}, rows={rows}")
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
    testOne = ['testbad8']
    suite = unittest.TestSuite(map(LineValidTest, testOne))
    # suite = unittest.TestSuite(map(LineValidTest, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
