import re


def reg_test1():
    xx = "guru99,education is fun"
    r1 = re.findall(r"^\w+", xx)
    print(r1)
    print((re.split(r'\s','we are splitting the words')))
    print((re.split(r's','split the words')))
    return

def reg_test2():
    #list = ["guru99 get", "guru99 give", "guru Selenium"]
    list = ["guru", "guru99 give", "guru Selenium"]
    for element in list:
        # z = re.match("(g\w+)\W(g\w+)", element)
        z = re.match("(g\w+\Wg\w+)", element)
        if z:
            print((z.groups()))
            print(z)

    return


def reg_test3():
    str_txt = "guru99 get guru99 give guru Selenium"
    z = re.match("(g\w+)\W(g\w+)", str_txt)
    if z:
        print((z.groups()))
        #print(z)

def reg_test4():
    str_txt = "guru99 get guru99"
    z = re.match("(g\w+)\W(g\w+)", str_txt)
    if z:
        print((z.groups()))
        # print(z)

def reg_test5():
    patterns = ['software testing', 'guru99']
    text = 'software testing is fun? guru99 has fun'

    for pattern in patterns:
        print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')

        if re.search(pattern, text):
            print('found a match!')
        else:
            print('no match')

    return


def reg_test6():
    print(re.search("I am 25 years old", "I am 25 years old and I live in HsinChu. My classmate said I am 25 years old too.").group())
    return


def reg_test7():
    print(re.search('\w\w\w', 'A2_').group())
    print(re.search('\w+', 'A2_b_6_C').group())
    print(re.search('\w+', '你好').group())
    return

def reg_test8():
    text = 'https://matters.news/@CHWang'
    text1 = 'matters.news'
    print(re.match('https', text))
    print(re.match('https', text).span())
    print(re.match('matters', text))
    print(re.match('matters', text1))
    print(re.match('matters', text1, flags=re.I))
    return


def reg_test9():
    text = 'Jack lives in HsinChu and he is 25 years old, but ...'

    match_result = re.match(r'(.*) lives in ([a-z]*) and he is (\d+).*', text, re.I)

    print(match_result.group())
    print(match_result.group(1))
    print(match_result.group(2))
    print(match_result.group(3))

    print(type(match_result.groups()))
    print(match_result.groups())
    return


def reg_test10():
    text = 'https://medium.com/@chwang12341'
    text1 = 'Medium.Com'

    print(re.search('https://', text))
    print(re.search('dium', text))
    print(re.search('medium', text).span())

    print(re.search('co', text1))
    print(re.search('co', text1, flags=re.I).span())
    return


def reg_test11():
    text = 'Jen likes to eat cake and drink coke, but ...'

    match_result = re.search('(.*) likes to eat (\w+) and drink ([a-z]*)', text, re.I | re.M)

    print(match_result.group())
    print(match_result.group(1))
    print(match_result.group(2))
    print(match_result.group(3))

    print(match_result.groups())
    return


def reg_test12():
    find_pattern = re.compile(r'[a-z]+', re.I)

    match_result1 = find_pattern.findall('good 66 day Tom_28 Yep')
    match_result2 = find_pattern.findall('good98MMorning66 Jen666 Yeah', 6, 20)

    print(match_result1)
    print(match_result2)
    return

def reg_test13():
    text = 'Jack/25/1993 and Jen/23/1995'

    ## 把中間的and與空格拿掉，用&替換
    sub_result1 = re.sub('\sand\s', '&', text)
    print(sub_result1)

    ## 狀況一: 再把/拿掉
    sub_result2 = re.sub('/', '', sub_result1)
    print(sub_result2)

    ## 狀況二: 再把/拿掉，但只要拿掉前兩個
    sub_result3 = re.sub('/', '', sub_result1, 2)
    print(sub_result3)
    return


def reg_test14():
    text = 'Jack66Jen58Ken2,Cathy38'


    ## 將匹配好的數字做平方計算
    def square(match_result):
        num = int(match_result.group('number'))

        return str(num ** 3)


    ## 給定我們匹配值一個名稱，用?P<name>
    final_result = re.sub('(?P<number>\d+)', square, text)

    print(final_result)
    return


def reg_test15():
    text = '68Jack66Jen58Ken28,Cathy38'

    ## 匹配字母，並忽略大小寫
    pattern = re.compile(r'([a-z]+)', re.I)

    ## match預設從第一個位置開始匹配
    compile_result1 = pattern.match(text)
    print(compile_result1)  ## None，因為match會從第一個位置開始匹配，如果不通過就會返回none

    ## 從第3個位置開始匹配
    compile_result2 = pattern.match(text, 2, 20)
    print(compile_result2)


    print(compile_result2.group(0))
    print(compile_result2.start(0))
    print(compile_result2.end(0))
    print(compile_result2.span())
    return


def reg_test16():
    match_result = re.finditer(r'[a-z]+', '68Jack66Jen58Ken28,Cathy38', re.I)


    for name in match_result:
        #  print(name)
        print(name.group())
    return


def reg_test17():
    text = 'Jack66Jen58Ken28Cathy'

    ## 用數字來做為分隔依據
    print(re.split('\d+', text))

    ## 分隔，並將數字也傳進陣列
    print(re.split('(\d+)', text))

    ## 如果匹配的一句剛好在前後的位置，就會傳回空值
    text1 = '66Jack66Jen58Ken28Cathy38'
    print(re.split('\d+', text1))

    ## 如果找不到匹配會回串全部字串
    #commit again
    print(re.split('\s+', text1))
    return

def reg_test18():
    m = re.match("([abc])+", "abefg")
    print(m.groups())
    m = re.match("(?:[abc])+", "abefg")
    print(m.groups())


def reg_test19():
    p = re.compile(r'(?P<word>\b\w+\b)')
    m = p.search('(((( Lots of punctuation )))')
    print(m.group('word'))
    print(m.group(1))
    print(m.groups())

reg_test19()