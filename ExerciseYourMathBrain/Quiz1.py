from decorators import timer
max = 10
n = 100
#cnt = 0

#花費時間 61 seconds
def check_v1(remain, pre, l):
    #global cnt
    cnt = 0
    if remain < 0:
        return 0
    if remain == 0:
        print(l)
        return 1
    # if remain == 1:
    #     return 0
    for i in range(pre, max+1):
        l.append(i)
        resp = check(remain - i, i, l)
        l.remove(i)
        cnt += resp
    
    return cnt

known_answers = {}


#花費時間 0.0021 seconds
def check(remain, pre, l):
    #global cnt
    cnt = 0
    if remain < 0:
        return 0
    if remain == 0:
        #print(l)
        return 1
    # if remain == 1:
    #     return 0
    for i in range(pre, max+1):
        l.append(i)
        if (remain - i, i) in known_answers:
            resp = known_answers[(remain - i, i)]
        else:
            resp = check(remain - i, i, l)
            known_answers[(remain - i, i)] = resp
        l.remove(i)
        cnt += resp
    
    return cnt

@timer
def show_time():
    theList = []
    print(check(n, 2, theList))

show_time()