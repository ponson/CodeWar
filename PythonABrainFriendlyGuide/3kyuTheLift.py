class Dinglemouse(object):

    def __init__(self, queues, capacity):
        print(f"queuse is: {queues} ")
        print(f"c is:{capacity}")
        self.trackRecord = [0]
        self.REVERSE = -1
        self.direction = 1
        self.floorMax = len(queues) - 1
        self.capacity = capacity
        self.queues = list(queues)
        self.waitingCnt = 0
        for i, f in enumerate(queues):
            self.queues[i] = list(f)
            self.waitingCnt += len(f)
        self.curFloor = 0
        self.inBox = []
        self.go()
        
    def go(self):
        UP, DOWN = 1, -1
        while self.waitingCnt > 0 or len(self.inBox) > 0:
            #TODO 1 目前樓層有沒有人抵達目標
            loaded = len(self.inBox)
            tempQ = list.copy(self.inBox)
            for p in self.inBox:
                if p == self.curFloor:
                    tempQ.remove(p)
            self.inBox = tempQ
            if loaded > len(self.inBox):
                self.trackRecord.append(self.curFloor)
            #TODO 2 目前樓層有沒有人要進來
            loaded = len(self.inBox)
            tempQ = list.copy(self.queues[self.curFloor])
            if self.direction == UP:
                waitCntInDirection = sum([len(q) for q in self.queues[self.curFloor+1:]])
                for w in self.queues[self.curFloor]:
                    if len(self.inBox) < self.capacity:
                        if w > self.curFloor or waitCntInDirection == 0:
                            tempQ.remove(w)
                            self.waitingCnt -= 1
                            self.inBox.append(w)
                    else:
                        if self.trackRecord[-1] != self.curFloor:
                            self.trackRecord.append(self.curFloor)
                        break
                if loaded < len(self.inBox) and self.trackRecord[-1] != self.curFloor:
                    self.trackRecord.append(self.curFloor)
            else: #DOWN
                waitCntInDirection = sum([len(q) for q in self.queues[0:self.curFloor]])
                for w in self.queues[self.curFloor]:
                    if len(self.inBox) < self.capacity:
                        if w < self.curFloor or waitCntInDirection == 0:
                            tempQ.remove(w)
                            self.waitingCnt -= 1
                            self.inBox.append(w)
                    else:
                        if self.trackRecord[-1] != self.curFloor:
                            self.trackRecord.append(self.curFloor)
                        break
                if loaded < len(self.inBox) and self.trackRecord[-1] != self.curFloor:
                    self.trackRecord.append(self.curFloor)
            
            self.queues[self.curFloor] = tempQ
            #TODO 3 目前樓層有沒有需要反向
            needReverse = True
            if self.direction == UP and self.curFloor < self.floorMax:
                if len(self.inBox) == 0:
                    for f in range(self.curFloor+1, self.floorMax+1):
                        if len(self.queues[f]) > 0:
                            needReverse = False
                            break
                else:
                    for t in self.inBox:
                        if t > self.curFloor:
                            needReverse = False
                            break
            elif self.direction == DOWN and self.curFloor > 0:
                if len(self.inBox) == 0:
                    for f in range(self.curFloor-1, -1, -1):
                        if len(self.queues[f]) > 0:
                            needReverse = False
                            break
                else:
                    for t in self.inBox:
                        if t < self.curFloor:
                            needReverse = False
                            break
            if needReverse:
                self.direction *= self.REVERSE
                
            #TODO 4 移動到下一層
            self.curFloor += self.direction

        if self.trackRecord[-1] != 0:
            self.trackRecord.append(0)

        
    def theLift(self):
        return self.trackRecord


# queues = ( (),   (),    (5,5,5), (),   (),    (),    () )
# lift = Dinglemouse(queues, 5)
# print(lift.theLift()) #[0, 2, 5, 0]
# queues = ( (),   (),    (1,1),   (),   (),    (),    () )
# lift = Dinglemouse(queues, 5)
# print(lift.theLift()) #[0, 2, 1, 0]
# queues = ( (),   (3,),  (4,),    (),   (5,),  (),    () )
# lift = Dinglemouse(queues, 5)
# print(lift.theLift()) #[0, 1, 2, 3, 4, 5, 0]
# queues = ( (),   (0,),  (),      (),   (2,),  (3,),  () )
# lift = Dinglemouse(queues, 5)
# print(lift.theLift()) #[0, 5, 4, 3, 2, 1, 0]
# queues = ((3,), (2,), (0,), (2,), (), (), (5,))
# lift = Dinglemouse(queues, 5)
# print(lift.theLift()) #[0, 1, 2, 3, 6, 5, 3, 2, 0]
queues = ((), (0, 0, 0, 6), (), (), (), (6, 6, 0, 0, 0, 6), ())
lift = Dinglemouse(queues, 5)
print(lift.theLift()) #[0, 1, 5, 6, 5, 1, 0, 1, 0]