import unittest

class Test_sudoku(unittest.TestCase):
    
    def testcase1(self):
        self.assertEqual(sudoku(puzzle), solution)

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]


boxes = [(0,0), (0,3), (0,6),
         (3,0), (3,3), (3,6),
         (6,0), (6,3), (6,6),]
        
offset = [(0,0), (0,1), (0,2),
          (1,0), (1,1), (1,2),
          (2,0), (2,1), (2,2)]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sudoku(puzzle):
    #TODO 1: Parsing the puzzle
    #Count the empty quantity
    emptyCells = {}
    for ridx, row in enumerate(puzzle):
        notyetNums = nums.copy()
        for cidx, num in enumerate(row):
            if num == 0:
                emptyCells[(ridx, cidx)] = []
            else:
                notyetNums.remove(num)

        for key in emptyCells.keys():
            if key[0] == ridx:
                emptyCells[key] = notyetNums.copy()

    #Check eacl col init status
    for cidx in range(9):
        notyetNums = nums.copy()
        for ridx in range(9):
            if puzzle[ridx][cidx]:
                notyetNums.remove(puzzle[ridx][cidx])
        for key in emptyCells.keys():
            if key[1] == cidx:
                emptyCells[key] = list(set(emptyCells[key]) & set(notyetNums))

    # print(f"emptyCells={emptyCells}")
    while len(emptyCells) > 0:
        #Rule 1: check 9 boxes, each has number 1~9
        for box in boxes:
            notyetNums = nums.copy()
            emptyInBox = []
            for dt in offset:
                if puzzle[box[0]+dt[0]][box[1]+dt[1]] in notyetNums:
                    notyetNums.remove(puzzle[box[0]+dt[0]][box[1]+dt[1]])
                elif puzzle[box[0]+dt[0]][box[1]+dt[1]] == 0:
                    emptyInBox.append((box[0]+dt[0], box[1]+dt[1]))

            for cell in emptyInBox:
                emptyCells[cell] = list(set(emptyCells[cell]) & set(notyetNums))

        #Rule 2: check each empty cell's candidate if only one
        foundAnsCells = {}
        for cell in emptyCells.keys():
            if len(emptyCells[cell]) == 1: # Got answer
                puzzle[cell[0]][cell[1]] = emptyCells[cell][0]
                foundAnsCells[cell] = emptyCells[cell][0]

        for cell in foundAnsCells.keys():
            emptyCells.pop(cell)
            
        #Check Row/Col rule 0-9
        for cell in foundAnsCells.keys():
            foundNum = foundAnsCells[cell]
            for etyCell in emptyCells.keys():
                if (etyCell[0] == cell[0] or etyCell[1] == cell[1]) and foundNum in emptyCells[etyCell]:
                    emptyCells[etyCell].remove(foundNum)


    return puzzle





if __name__ == '__main__':
    tests = ['testcase1']
    testOne = ['testcase1']
    # suite = unittest.TestSuite(map(Test_sudoku, tests))
    suite = unittest.TestSuite(map(Test_sudoku, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)