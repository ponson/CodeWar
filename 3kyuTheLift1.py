class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.Q = {k:[[p for p in q if (p > i if k == 'U' else p < i)][::-1] for i, q in enumerate(queues)] for k in 'UD'}
        self.floors = [f for f in range(len(queues))]
        self.capacity = capacity

    def theLift(self):
        f, d, lift, path = 0, 'U', [], [0]
        
        while sum(len(q) for q in self.Q['U']) + sum(len(q) for q in self.Q['D']) + len(lift) > 0:    
            if self.Q[d][f] or f in lift:
                if path[-1] != f: path.append(f)
                lift = [p for p in lift if p != f]
                while len(lift) < self.capacity and self.Q[d][f]: lift.append(self.Q[d][f].pop())

            f += {'U':1, 'D':-1}[d]
            if f not in self.floors:
                d = {'U':'D', 'D':'U'}[d]
                f += {'U':1, 'D':-1}[d]
                    
        return path if path[-1] == 0 else path + [0]


queues = ((6, 3, 5, 3), (3, 2, 3), (1, 6, 5, 1), (1,), (6, 6, 2, 0), (2, 2, 4, 1), (0, 5, 4, 5, 2))
lift = Dinglemouse(queues, 5)
print(lift.theLift()) #[0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 5, 6, 5, 4, 3, 1, 0]
queues = ((), (0,), (3,), (), ())
lift = Dinglemouse(queues, 2)
print(lift.theLift()) #