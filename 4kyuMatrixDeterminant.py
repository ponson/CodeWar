import unittest

class Test_MatrixDeterminant(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(determinant([[5]]), 5)
    
    def testcase2(self):
        self.assertEqual(determinant([[4, 6], [3, 8]]), 14)

    def testcase3(self):
        self.assertEqual(determinant([[2, 4, 2], [3, 1, 1], [1, 2, 0]]), 10)
        

def determ(matRowIdx, matColIdx, matrix):
    if len(matRowIdx) == 1:
        return matrix[matRowIdx[0]][matColIdx[0]]
    elif len(matRowIdx) == 2:
        return matrix[matRowIdx[0]][matColIdx[0]] * matrix[matRowIdx[1]][matColIdx[1]] - matrix[matRowIdx[1]][matColIdx[0]] * matrix[matRowIdx[0]][matColIdx[1]]
    else:
        det = 0
        mRowIdx = matRowIdx.copy()
        mRowIdx.pop(0)
        for i in range(len(matRowIdx)):
            mColIdx = matColIdx.copy()
            mColIdx.pop(i)
            det += (matrix[matRowIdx[0]][matColIdx[i]] * (-1)**i * determ(mRowIdx, mColIdx, matrix))
        return det


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    else:
        matRowIdx = []
        matColIdx = []
        for i in range(len(matrix)):
            matRowIdx.append(i)
            matColIdx.append(i)
        return determ(matRowIdx, matColIdx, matrix)


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3']
    testOne = ['testcase3']
    suite = unittest.TestSuite(map(Test_MatrixDeterminant, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)