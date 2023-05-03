import re

def solve_runes(runes):
    for i in range(10):
        if str(i) in runes:
            continue
        else:
            candidate = runes.replace('?', str(i))
            if re.search(r"([^\d]|\b)0\d+", candidate):
                continue
            items = candidate.split("=")
            if int(items[1]) == eval(items[0]):
                return i

    return -1
    
    
# print(solve_runes("123?45*?=?"))   #0
# print(solve_runes("?*123?45=?"))   #0
# print(solve_runes("??+??=??"))     #-1
print(solve_runes("-?56373--9216=-?47157"))   #8
# print(solve_runes("1+1=?")) #2
# print(solve_runes("123*45?=5?088")) #6
# print(solve_runes("-5?*-1=5?")) #0
# print(solve_runes("19--45=5?")) #-1
# print(solve_runes("??*??=302?")) #5
# print(solve_runes("?*11=??")) #2
# print(solve_runes("??*1=??")) #2
