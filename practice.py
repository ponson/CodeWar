import uuid
import itertools
import datetime
import calendar
import re
import os
import fnmatch
import gzip
import bz2
import re
import sys
from sympy import Symbol, series



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
    l = [[2, 5, 8], [1, 2, 3], [2, 1, 3], [4, 0, 3]]
    l.sort(key=sort_by_2nd)
    return l


def count_test():
    a = itertools.count(1)         # 設定 a 從 1 開始，間隔 1 無限循環
    b = itertools.count(5, 2)      # 設定 b 從 5 開始，間隔 2 無限循環
    for i in a:
        print(i, end=' ')          # 1 2 3 4 5 6 7 印出 a 裡的每個項目
        if i > 6:
            break              # 如果超過 6 就停止
    print()
    for i in b:
        print(i, end=' ')          # 5 7 9 11 13 15 17 19 21 印出 b 裡的每個項目
        if i > 20:
            break


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


def randomname_test():
    print(str(uuid.uuid4().hex))


def list_compare():
    a = [1, 2, 3]
    b = [1, 2, 3]
    if a == b:
        print('True')
    else:
        print('False')

# list_compare()

# print(f"I'm learning Visual Studio Code")


a = '   abcdefg   '
b = 'k'
r = a + (b * 4)

# print(r)


def keytest():
    print("best key word edit and test")
    print("The  time Required to complete the tutor is 25-30 minutes.")


def ordtest():
    x1 = '孫'
    print(hex(ord(x1)))
    x1 = '鵬'
    print(hex(ord(x1)))
    x1 = '宗'
    print(hex(ord(x1)))
    # print(ord(x1))


def roundTest():
    x = 1.23456
    print(f"{x}")
    print(format(x, '0.2f'))
    y = round(x, 3)
    print(y)


def fTest():
    x = 1234.56789
    print(format(x, ','))
    print(format(x, '0.2f'))
    print(format(x, '>10.1f'))
    print(format(x, '<10.1f'))
    print(format(x, '^10.1f'))


def minusTest():
    x = -1234
    print(format(x, 'b'))
    print(format(2**32+x, 'b'))


def dtTest():
    a = datetime.timedelta(days=2, hours=6)
    b = datetime.timedelta(hours=4.5)
    c = a + b
    print(f"c={c}")
    print(f"c.days={c.days}")
    print(f"c.seconds={c.seconds}")
    print(f"c.total_seconds={c.total_seconds()}")


def get_month_range(start_date=None):
    if start_date is None:
        start_date = datetime.date.today()
        print(f"start_date={start_date}")
        start_date = datetime.date.today().replace(day=1)
        print(f"start_date={start_date}")
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    print(f"days_in_month={days_in_month}")
    end_date = start_date + datetime.timedelta(days=days_in_month)
    return (start_date, end_date)


def oneMonthRange():
    a_day = datetime.timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day


def tuble_sub():
    x, y = (-1, -2)
    print((x, y))


Tokens = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'}
axis = {'A': (-1, -1), 'B': (-1, 0), 'C': (-1, 1), 'D': (0, -1),
        'E': (0, 0), 'F': (0, 1), 'G': (1, -1), 'H': (1, 0), 'I': (1, 1)}
tokenFromAxis = {(-1, -1): 'A', (-1, 0): 'B', (-1, 1): 'C', (0, -1): 'D',
                 (0, 0): 'E', (0, 1): 'F',  (1, -1): 'G', (1, 0): 'H', (1, 1): 'I'}


def halfDistanceTest():
    x, y = axis['C']
    dx, dy = (2, 0)
    nextOne = (x+(dx/2), y+(dy/2))
    print(f"next is {nextOne}")
    if nextOne in tokenFromAxis.keys():
        print(f"{tokenFromAxis[nextOne]}")
        if tokenFromAxis[nextOne] in Tokens:
            print("Found")
        else:
            print("Not Found")
    else:
        print("The key not found")


def setDictionary():
    EQUIV_PTS = {same: src for src, seq in (
        ('A', 'CGI'), ('B', 'DFH')) for same in seq}
    print(EQUIV_PTS)


def listidx():

    fruits = [4, 55, 64, 32, 16, 32]
    x = fruits.pop(1)
    x = fruits.pop(1)
    print(fruits)


def long_function_name(
        var_one, var_two,
        var_three, var_four):
    print("Test long function name")
    return 1


def regex_remove_pattern():
    txt = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x = re.split("[aeiouAEIOU]", txt)
    print(''.join(x))


def gen_find(filepat, top):

    x = 5
    y = 6

    for path, dirlist, filelist in os.walk(top):
        print(f"path={path}")
        print(f"dirlist={dirlist}")
        print(f"filelist={filelist}")
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):

    for filename in filenames:
        print(f"filename={filename}")
        f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        # print(f"line={str(line)}")
        if pat.search(line):
            yield line


def pipechain():
    logNames = gen_find('access-log*', 'www')
    files = gen_opener(logNames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)


# logNames = gen_find('access-log*', 'www')
# pipechain()
# gen_find('access-log*', 'www')


def foo1(g):
    for i in g:
        yield i + 1


def foo2(g):
    for i in g:
        yield 10 + i


def foo3(g):
    for i in g:
        yield 'foo3:' + str(i)

# res = foo3(foo2(foo1(range(0, 5))))

# for i in res:
    # print(i)

# logNames = gen_find('access-log*', 'www')
# files = gen_opener(logNames)
# lines = gen_concatenate(files)
# # pylines = gen_grep('(?i)python', lines)
# pylines = gen_grep('(?i)python', gen_concatenate(gen_opener(gen_find('access-log*', 'www'))))
# for line in pylines:
#     print(line)


def getDefaultEncode():
    print(sys.getdefaultencoding())


def checklist():
    l = list(range(10))
    # l = range(10)
    print(l)


def permute():
    r = itertools.permutations(range(2))
    for i in r:
        print(i)


def eval_test():

    a = 'True'
    b = 'False'
    c = '^'

    print(eval(a+c+b))


def checktype(test):
    print(type(test))

    if type(test) == int:
        return print(True)
    else:
        return print(False)


def checknumber(value):
    print(value.isdigit())
    print(value.isnumeric())
    print(value.isdecimal())


def re_practice():
    # phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phoneNumber = re.compile(r'\d{3}-\d{3}-\d{4}')
    mo = phoneNumber.search('My number is 415-555-4242.')
    print('Phone number found: '+ mo.group())


def re_practice1():
    # phoneNumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    phoneNumber = re.compile(r'Batman|Tina Fey')
    mo = phoneNumber.search('Batman and Tina Fey')
    print(mo.group())
    mo = phoneNumber.search('Tina Fey and Batman')
    print(mo.group())

def re_practice2():
    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo = batRegex.search("Batmobile lost a wheel")
    print(mo.group())
    print(mo.group(1))

def re_practice3():
    batRegex = re.compile(r'Bat(wo)?man')
    mo = batRegex.search("The adventure of Batman")
    print(mo.group())
    mo = batRegex.search("The adventure of Batwoman")
    print(mo.group())
    
def re_practice4():
    greedyHaRegex = re.compile(r'(Ha){3,5}')
    mo1 = greedyHaRegex.search('HaHaHaHaHa')
    print(mo1.group())

    greedyHaRegex = re.compile(r'(Ha){3,5}?')
    mo1 = greedyHaRegex.search('HaHaHaHaHa')
    print(mo1.group())

def re_practice5():
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print(phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000'))

def re_practice6():
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
    print(phoneNumRegex.findall('Cell: 415-555-9999, Work: 212-555-0000'))

def re_practice7():
    beginWithHello = re.compile(r'^Hello')
    # print(beginWithHello.search('Hello World'))
    print(beginWithHello.search('She said: Hello World'))

def re_practice8():
    endWithNumber = re.compile(r'\d$')
    print(endWithNumber.search('Your number is 42'))
    print(endWithNumber.search('Your number is 42'))

def re_practice9():
    atRegex = re.compile(r'.at')
    print(atRegex.findall('The cat in the hat sat on flatmat'))

def re_practice10():
    nameRegex = re.compile(r'First Name:(.*) Last Name:\s*(\S*)')
    mo = nameRegex.search('First Name:Al Last Name: Spencer')
    print(mo.group(1))
    print(mo.group(2))

def re_practice11():
    agentNameRegex = re.compile(r'Agent (\w)\w*')
    print(agentNameRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

def re_split():
    code = '''\
mov   a, 11           ; value1
mov   b, 3            ; value2
call  mod_func
msg   'mod(', a, ', ', b, ') = ', d        ; output
end

; Mod function
mod_func:
    mov   c, a        ; temp1
    div   c, b
    mul   c, b
    mov   d, a        ; temp2
    sub   d, c
    ret
'''
    codeRegex = re.compile(r'\n\s*')
    resultList = codeRegex.split(code)
    print(resultList)

def re_split2():
    code = 'abcdefgabcdefgabcdefg'
    codeRegex = re.compile(r'd')
    resultList = codeRegex.split(code)
    print(resultList)


fruits = ['apple', 'banana', 'cherry']
def listpop(lst):

    lst.pop()

    return lst

def listslice(lst):

    slice = lst[0:2]
    print(f"slice={slice}, lst={lst}")
    slice[0] = 'orange'
    print(f"slice={slice}, lst={lst}")

    return lst

print(listslice(fruits))