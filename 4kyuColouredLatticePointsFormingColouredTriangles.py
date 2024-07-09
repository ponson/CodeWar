
import unittest
from itertools import combinations

class Test_ColouredLatticePoints(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(count_col_triang([[[3, -4], 'blue'], [[-7, -1], 'red'],
                                           [[7, -6], 'yellow'], [[2, 5], 'yellow'],
                                           [[1, -5], 'red'], [[-1, 4], 'red'],
                                           [[1, 7], 'red'], [[-3, 5], 'red'],
                                           [[-3, -5], 'blue'], [[4, 1], 'blue']]),
                         [10, 3, 11, ['red', 10]])
    
    def testcase2(self):
        self.assertEqual(count_col_triang([[[3, -4], 'blue'], [[-7, -1], 'red'],
                                           [[7, -6], 'yellow'], [[2, 5], 'yellow'],
                                           [[1, -5], 'red'], [[1, 1], 'red'],
                                           [[1, 7], 'red'], [[1, 4], 'red'],
                                           [[-3, -5], 'blue'], [[4, 1], 'blue']]),
                         [10, 3, 7, ['red', 6]])

    def testcase3(self):
        self.assertEqual(count_col_triang([[[1, -2], 'red'],
                                           [[7, -6], 'yellow'], [[2, 5], 'yellow'],
                                           [[1, -5], 'red'], [[1, 1], 'red'],
                                           [[1, 7], 'red'], [[1, 4], 'red'],
                                           [[-3, -5], 'blue'], [[4, 1], 'blue']]),
                         [9, 3, 0, []])


def det_cal(a, b, c):
    return a[0]*b[1]-a[0]*c[1]-a[1]*b[0]+a[1]*c[0]+b[0]*c[1]-c[0]*b[1]


def count_col_triang(input_):
    triCnt, colors = {}, {}
    for item in input_:
        if item[-1] in colors.keys():
            colors[item[-1]].append(item[0])
        else:
            colors[item[-1]] = [item[0]]

    #TODO count triangles
    points, alltris, result = 0, 0, []
    for color_name, colorlst in colors.items():
        count = 0
        points += len(colorlst)
        for triangle in list(combinations(colorlst, 3)):
            if det_cal(triangle[0], triangle[1], triangle[2]) != 0:
                count += 1
        triCnt[color_name] = count
        alltris += count

    result.append(points)
    result.append(len(colors))
    result.append(alltris)
    if alltris == 0:
        result.append([])
    else:
        colormax = []
        maxTri = max(triCnt.values())
        for keyColor in triCnt.keys():
            if triCnt[keyColor] == maxTri:
                colormax.append(keyColor)
        colormax.sort()
        colormax.append(maxTri)
        result.append(colormax)

    return result 


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3']
    testOne = ['testcase1']
    suite = unittest.TestSuite(map(Test_ColouredLatticePoints, tests))
    unittest.TextTestRunner(verbosity=2).run(suite)