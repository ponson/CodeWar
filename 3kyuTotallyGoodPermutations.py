import unittest
import itertools


class Test_totally_good(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(totally_good('ABC',[]), 6)
        self.assertEqual(totally_good('ABCD',[]), 24)
        self.assertEqual(totally_good('ABCDE',[]), 120)
        self.assertEqual(totally_good('ABCD',['AB']), 18)
        self.assertEqual(totally_good('ABCD',['BA']), 18)
        self.assertEqual(totally_good('ABCD',['A']), 0)
        self.assertEqual(totally_good('ABC',['CA', 'AB']), 3)

    def testcase8(self):
        self.assertEqual(totally_good('ABCD',['A','BC']),0)
        self.assertEqual(totally_good('ABCD',['AB','CD']),14)
        self.assertEqual(totally_good('ABCDE',['AB','CD']),78)
        self.assertEqual(totally_good('ABCDE',['AB','CDE']),92)

    def testcase2(self):
        self.assertEqual(totally_good('ABCD',['A','AC']),0)
        self.assertEqual(totally_good('ABCDE',['AB','BC']),78)
        self.assertEqual(totally_good('ABCDE',['ABC','BE']),90)
        self.assertEqual(totally_good('ABCDEF',['FC','CAE']),582)
        self.assertEqual(totally_good('ABCDEF',['FC','BC','EC']),360)
        self.assertEqual(totally_good('ABCDEF',['FC','BC','EC','BE']),288)
        self.assertEqual(totally_good('ABCDEFGH',['FC','ABD','EHG']),34098)
        self.assertEqual(totally_good('ABCDEFGH',['ABCD','BCDE']),40104)
        self.assertEqual(totally_good('ABCDEFGH',['ABCD','BCDEFG']),40196)

    def testcase3(self):
        # self.assertEqual(totally_good('ABCDE',['ABC','CD','DEA']),89)
        # self.assertEqual(totally_good('ABCDEFGH',['ABCD','CDEFG','FGH']),39469)
        self.assertEqual(totally_good('ABCDEFGH',['AB','BCD','CDE','DEFG','GH']),29966)
        self.assertEqual(totally_good('ABCDEFGH',['ABCD','CDEF','EFGH','GHAB']),39864)

    def testcase4(self):
        # self.assertEqual(totally_good('ABCDE',['ABC','BE','ADC']),86)
        # self.assertEqual(totally_good('ABCDE',['ABC','BE','EA','CB']),60)
        self.assertEqual(totally_good('ABCDEFGH',['AB','BC','FG','GH']),24024)
        # self.assertEqual(totally_good('ABCDEFGH',['AB','BC','CDE','FG','GH']),23662)
        # self.assertEqual(totally_good('ABCDEFGH',['ABC','CD','DEFG','FGH']),34023)

    def testcase5(self):
        self.assertEqual(totally_good('ABCDEFGH',['ABCDE','BCD']),39600)
        self.assertEqual(totally_good('ABCDEFGH',['ABCDEF','BCDE','DE']),35280)
        self.assertEqual(totally_good('ABCDEFGH',['ABCDEF','BCDEF','BCDE','CDE','DE']),35280)
        self.assertEqual(totally_good('ABCDEFGH',['ABH','CH','DEH','FGH']),33120)
        self.assertEqual(totally_good('ABCDEFGH',['ABH','CBH','DEBH','FGBH']),38640)

    def testcase6(self):
        self.assertEqual(totally_good('ABCDEFG',['BCDE','CE','CF','CB','EB']),2376)
        # self.assertEqual(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH']),26761)
        # self.assertEqual(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH','EF']),23662)
        # self.assertEqual(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH','EF','HCBG']),23566)
        # self.assertEqual(totally_good('ABCDEFGH',['AB','BC','CDE','BCD','DEFG','GH','EF','HCBG','CB']),19942)
        # self.assertEqual(totally_good('ABCDEFGH',['BCDEFG','CDEF','DE','BCD','EFG','CD','EF','FEDC','ABC','ABCD']),26694)
        # self.assertEqual(totally_good('ABCDEFGH',['ABC','ACB','BAC','BCA','CAB','CBA']),36000)

    def testcase7(self):
        self.assertEqual(totally_good('ABCDEFGHIJKL',[]),479001600)
        self.assertEqual(totally_good('ABCDEFGHI',['AB','CD','EFGH','BC','FG','BH','ABCDE','DAC','ADG','IFBC']),194520)
        self.assertEqual(totally_good('ABCDEFGHI',['ABCDEF','CDFIBA','HIFDCA','GHFCAB','ABCDIHG','EFGCDA','IHEFDCA','HAIE','FEBHDA','ACHIEBF','CE','BADICE']),321678)
        self.assertEqual(totally_good('ABCDEFGHIJ',['AB','CD','EFGH','BC','FG','BH','ABCDE','DAC','ADG','IFBC']),2082240)


def nmulti(num):
    sum = 1
    for i in range(1, num+1):
        sum *= i
    return sum


def check_bad_counts(pbadlist, palllen):

    if len(pbadlist) == 1:
        return nmulti(palllen - len(pbadlist[0]) + 1)
    else: #handle >= 2 items cases
        alphabetset = set()
        alloflens = 0
        for i in range(len(pbadlist)):
            for n in pbadlist[i]:
                alphabetset.add(n)
            alloflens += len(pbadlist[i])
        if alloflens == len(alphabetset):
            return nmulti(palllen - alloflens + len(pbadlist))
        else:
            combineStr = ""
            strrr = ''.join(a for a in alphabetset)
            permutations = itertools.permutations(strrr)
            for perm in permutations:
                if all(sub in ''.join(perm) for sub in pbadlist):
                    combineStr = ''.join(perm)
                    break
            if combineStr:
                return nmulti(palllen - len(combineStr) + 1)
            else:
                return 0


def totally_good(alphabet, bads):           
    alphalen = len(alphabet)
    badcount = 0
    multiminus = 1
    badSorted = sorted(bads)
    candiSorted = badSorted.copy()
    print(badSorted)
    for idx in range(len(badSorted)-1):
        isSub = False
        for ref in range(idx+1,len(badSorted)):
            if len(badSorted[idx]) > len(badSorted[ref]):
                if badSorted[idx].find(badSorted[ref]) >= 0:
                    isSub = True
                    delThis = badSorted[idx]
                    break
            else:
                if badSorted[ref].find(badSorted[idx]) >= 0:
                    isSub = True
                    delThis = badSorted[ref]
                    break
        if isSub == True and delThis in candiSorted :
            candiSorted.remove(delThis)

    print(candiSorted)
    for round in range(1, len(candiSorted)+1):
        roundCnt = 0
        roundList = itertools.combinations(candiSorted, round)
        for b in roundList:
            roundCnt += check_bad_counts(b, alphalen)
        roundCnt *= multiminus
        badcount += roundCnt
        multiminus *= -1

    return nmulti(alphalen) - badcount


    


    # for bad in badSorted:
    #     badLen = len(bad)
    #     badcount += nmulti(ln-badLen+1)
    #     goodPartial = 
    return


if __name__ == '__main__':
    tests = ['testcase1', 'testcase2', 'testcase3', 'testcase4',
             'testcase5', 'testcase6', 'testcase7', 'testcase8']
    testOne = ['testcase3']
    suite = unittest.TestSuite(map(Test_totally_good, testOne))
    unittest.TextTestRunner(verbosity=2).run(suite)