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


DIRECTIONS = {'n': (-1,  0, 'X+|'),                      # Pre-setting direction properties
              's': (1,  0, 'X+|'),
              'w': (0, -1, 'X+-'),
              'e': (0,  1, 'X+-'), }


def line2(grid, attempt=1):                             # Attempt = 1 means first attempt, direct path
    # Converting 2D to 1D & checking attempt
    print(f"a={''.join(grid)}")
    print(f"b={''.join(grid)[::attempt]}")
    a=''.join(grid)
    b=''.join(grid)[::attempt]
    vector = list(''.join(grid)[::attempt])
    # Variable useful for 1D implementation
    width = len(grid[0])
    state = vector.index('X'), 'news'                    # Initializing state
    while len(state) == 2:                               # State not final and unambiguous?
        i, direction = state                             # Details of the state
        if vector[i] == '+':                             # Corner?
            # Check perpendicular directions
            direction = ('ns', 'ew')[direction in 'ns']
        vector[i], state = ' ', ()                       # Cleaning up
        for neighbor in direction:                       # Check all valid directions
            # Read direction properties
            ny, nx, actives = DIRECTIONS[neighbor]
            ni = ny * width + nx + i                     # Calculate new 1D cursor position
            inside = (-1 < ni < len(vector) and          # Check we are still inside the grid vertically
                      -1 < (nx + i % width) < width)  # ...and horizontally
            # Inside? Direction has next path step?
            if inside and vector[ni] in actives:
                state += ni, neighbor                    # Develop new state
    return (all(c == ' ' for c in vector) or             # Path fully cleared?
            attempt == 1 and line(grid, attempt=-1))   # If first attempt, now try the reverse path


def line(grid):
    g = {(r, c): v for r, row in enumerate(grid)
         for c, v in enumerate(row) if v.strip()}
    ends = [k for k in g if g[k] == 'X']
    if len(ends) != 2:
        return False

    for start, finish in [ends, ends[::-1]]:
        path = [start]
        while path[-1] != finish:
            r, c = path[-1]
            d, V, H = g[path[-1]], [(r+1, c), (r-1, c)], [(r, c-1), (r, c+1)]
            mdict = {
                '+': V if len(path) > 1 and path[-1][0] == path[-2][0] else H, '|': V, '-': H, 'X': H+V}
            moves = {
                '+': V if len(path) > 1 and path[-1][0] == path[-2][0] else H, '|': V, '-': H, 'X': H+V}[d]
            possibles = {p for p in moves if p in g and p not in path and (
                d == '+' or (p[0] == r and g[p] != '|') or (p[1] == c and g[p] != '-'))}

            if len(possibles) != 1:
                break
            path.append(possibles.pop())
        if len(g) == len(path):
            return True
    return False

if __name__ == '__main__':
    tests = ['testgood1', 'testgood2', 'testgood3', 'testgood4', 'testgood5', 'testgood6', 'testgood7',
             'testbad1', 'testbad2', 'testbad3', 'testbad4', 'testbad5', 'testbad6', 'testbad7', 'testbad8']
    testparts = ['testgood1', 'testgood2',
                 'testgood3', 'testgood4', 'testgood5']
    testOne = ['testgood3']
    # testOne = ['testbad8']
    suite = unittest.TestSuite(map(LineValidTest, testOne))
    # suite = unittest.TestSuite(map(LineValidTest, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
