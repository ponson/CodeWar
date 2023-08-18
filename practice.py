def list_test():
    print(len([0]))
    print(len([]))
    print(len([[1, 3, [4, 5], 6], 7]))

     

def list_test1():
    x = [1, 2, 3]
    x.insert(len(x), "Hello")
    print(x)

def sort_by_2nd(thel):
    return thel[1]

def list_sort_by2():
    l = [[2,5,8], [1,2,3], [2,1,3], [4,0,3]]
    l.sort(key=sort_by_2nd)
    return l

import itertools
def count_test():
    a = itertools.count(1)         # 設定 a 從 1 開始，間隔 1 無限循環
    b = itertools.count(5, 2)      # 設定 b 從 5 開始，間隔 2 無限循環
    for i in a:
        print(i, end=' ')          # 1 2 3 4 5 6 7 印出 a 裡的每個項目
        if i>6: break              # 如果超過 6 就停止
    print()
    for i in b:
        print(i, end=' ')          # 5 7 9 11 13 15 17 19 21 印出 b 裡的每個項目
        if i>20: break   
        
def accu_test():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = itertools.accumulate(a)
    c = itertools.accumulate(a, lambda x, y: x*y*2)  # 使用 lambda 匿名函式
    for i in b:
        print(i, end=' ')   # 1 3 6 10 15 21 28 36 45
    print()
    for i in c:
        print(i, end=' ')   # 1 2 6 24 120 720 5040 40320 362880
    
def groupby_test():
    a = 'AAaBbbCcCAbC'
    print('1st groupby')
    b = itertools.groupby(a)
    for key, val in b:
        print(key, list(val))

    # A ['A', 'A']
    # a ['a']
    # B ['B']
    # b ['b', 'b']
    # C ['C']
    # c ['c']
    # C ['C']

    print('2nd groupby')
    c = itertools.groupby(a, lambda x: x.upper())   # 轉換成大寫後分組
    for key, val in c:
        print(key, list(val))


def startmap_test():
    a = 'abcdefg'
    b = itertools.starmap(lambda x: x+'1', a)
    for i in b:
        print(i, end=' ')

def tee_test():
    a = 'abcde'
    b = itertools.tee(a, 5)
    for i in b:
        print(list(i))


def longest_test():
    a = 'abcde'
    b = ''
    c = itertools.zip_longest(a, b, fillvalue='?')
    for i in c:
        print(i)


def permutation_test():
    a = 'abc'
    r = itertools.permutations(a)
    for i in r:
        print(*i)


def combinations_test():
    a = 'abc'
    r = itertools.combinations(a, 2)
    for i in r:
        print(*i)


def cycle_test():
    a = itertools.cycle(['A', 'B', 'C'])
    for i in range(20):
        print(next(a), end=' ')

import uuid

def randomname_test():
    print(str(uuid.uuid4().hex))

def list_compare():
    a = [1, 2, 3]
    b = [1, 2, 3]
    if a == b:
        print('True')
    else:
        print('False')

list_compare()