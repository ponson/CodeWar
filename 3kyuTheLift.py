import unittest

class TestDinglemouse(unittest.TestCase):
    def test_case1(self):
        queues = ( (),   (),    (5,5,5), (),   (),    (),    () )
        lift = Dinglemouse(queues, 5)
        self.assertEqual(lift.theLift(), [0, 2, 5, 0])
        
    def test_case2(self):
        queues = ( (),   (),    (5,5,5), (),   (),    (),    () )
        lift = Dinglemouse(queues, 5)
        self.assertEqual(lift.theLift(), [0, 2, 5, 0])

    def test_case3(self):
        queues = ( (),   (3,),  (4,),    (),   (5,),  (),    () )
        lift = Dinglemouse(queues, 5)
        self.assertEqual(lift.theLift(), [0, 1, 2, 3, 4, 5, 0])

    def test_case4(self):
        queues = ((), (0, 0, 0, 6), (), (), (), (6, 6, 0, 0, 0, 6), ())
        lift = Dinglemouse(queues, 5)
        self.assertEqual(lift.theLift(), [0, 1, 5, 6, 5, 1, 0, 1, 0])

    def test_case5(self):
        queues = ((), (0, 0, 0, 6), (), (), (), (6, 6, 0, 0, 0, 6), ())
        lift = Dinglemouse(queues, 5)
        self.assertEqual(lift.theLift(), [0, 1, 5, 6, 5, 1, 0, 1, 0])

    def test_case6(self):
        queues = ((), (2,), (3, 3, 3), (1,), (), (), ())
        lift = Dinglemouse(queues, 1)
        self.assertEqual(lift.theLift(), [0, 1, 2, 3, 1, 2, 3, 2, 3, 0])


class Dinglemouse(object):

    def __init__(self, queues, capacity):
        print(f"queuse is: {queues} ")
        print(f"c is:{capacity}")
        self.trackRecord = [0]
        self.REVERSE = -1
        self.direction = 1
        self.floorMax = len(queues) - 1
        self.capacity = capacity
        self.queues = [list(l) for l in queues]
        self.waitingCnt = sum((len(l) for l in self.queues))
        self.curFloor = 0
        self.inBox = []
        
    def go(self):
        UP, DOWN = 1, -1
        while self.waitingCnt > 0 or len(self.inBox) > 0:
            #TODO 1 目前樓層有沒有人抵達目標
            if len([p for p in self.inBox if p == self.curFloor]):
                self.trackRecord.append(self.curFloor)
            self.inBox = [p for p in self.inBox if p != self.curFloor]
            
            #TODO 2 目前樓層有沒有人要進來
            curFloorWantIn = [f for f in self.queues[self.curFloor] if f*self.direction > self.curFloor*self.direction]
            if self.trackRecord[-1] != self.curFloor and curFloorWantIn:
                self.trackRecord.append(self.curFloor)

            while len(self.inBox) < self.capacity and curFloorWantIn:
                self.inBox.append(curFloorWantIn[0])
                self.queues[self.curFloor].remove(curFloorWantIn[0])
                curFloorWantIn.remove(curFloorWantIn[0])
                self.waitingCnt -= 1
                
            #TODO 3 目前樓層有沒有需要反向
            needReverse = True
            check1 = [f for f in range(self.curFloor+self.direction, (self.floorMax+self.floorMax*self.direction)//2+self.direction, self.direction) if len(self.queues[f]) > 0]
            check2 = [t for t in self.inBox if t*self.direction > self.curFloor*self.direction]
            if (self.direction == UP and self.curFloor < self.floorMax) or (self.direction == DOWN and self.curFloor > 0):
                if (len(self.inBox) == 0 and len(check1)) or len(check2): 
                    needReverse = False
            # #TODO 4 移動到下一層
            if needReverse:
                self.direction *= self.REVERSE
            else:
                self.curFloor += self.direction

        if self.trackRecord[-1] != 0:
            self.trackRecord.append(0)

        
    def theLift(self):
        self.go()
        return self.trackRecord


if __name__ == '__main__':
    unittest.main()