class Dinglemouse:
    def __init__(self, queues, capacity): 
        self.queues, self.floor, self.capacity, self.li = queues, (l := len(queues)), capacity, lambda: [[] for _ in range(l)]
    def list_(self, queues) -> list[list[int]]: return (up_ := self.li(), down_ := self.li(), [[(up_ if _ > __ else down_)[__].append(_) for _ in _] for __, _ in enumerate(queues)], [_ for _ in up_[:-1]] + [_ for _ in down_][1:][::-1])[-1]
    def theLift(self):
        road, lift, f_, n, q = [0], [], (f := self.floor) * 2 - 2, self.capacity, self.list_(self.queues)
        while [_ for _ in q if _]:
            for _, __ in (enumerate(q), q := [])[0]: (k := (j := _ if _ < f else f_ - _) in lift, lift := [i for i in lift if i != j], lift.extend(__[:(i := min(n-len(lift), l := len(__)))]), q.append(__[i:]), road.append(j) if (i or k or l) and road[-1] != j else None)
        return road + [0] if road[-1] else road



queues = ((6, 3, 5, 3), (3, 2, 3), (1, 6, 5, 1), (1,), (6, 6, 2, 0), (2, 2, 4, 1), (0, 5, 4, 5, 2))
lift = Dinglemouse(queues, 5)
print(lift.theLift()) #[0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 5, 6, 5, 4, 3, 1, 0]