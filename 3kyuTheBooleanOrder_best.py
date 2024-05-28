from functools import lru_cache
from operator import and_, or_, xor

FUNCS = {'|': or_, '&': and_, '^': xor}


def solve(s, ops):

    @lru_cache(None)
    def evaluate(s, ops):
        c = [0, 0]
        if not ops:
            c[s == 't'] += 1
        else:
            for i in range(len(ops)):
                for v, n in enumerate(evaluate(s[:i+1], ops[:i])):
                    print(f"v={v}, n={n}")
                    for w, m in enumerate(evaluate(s[i+1:], ops[i+1:])):
                        print(f"w={w}, m={m}")
                        c[FUNCS[ops[i]](v, w)] += n*m
        return c

    return evaluate(s, ops)[True]


print(solve("tft", "^&"))
# print(solve("ttftff", "|&^&&"))