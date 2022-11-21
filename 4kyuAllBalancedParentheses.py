
def analyze_parens_v1(l, r, temp):
    ans = []
    if l == 0:
        temp = temp + ')' * r
        ans.append("".join(temp))
    
    elif r > l:
        result_l = analyze_parens(l-1, r, temp+"(")
        print(f"result_l={result_l}")
        for i in result_l:
            ans.append(i)
        result_r = analyze_parens(l, r-1, temp+")")
        print(f"result_r={result_r}")
        for i in result_r:
            ans.append(i)
    elif r == l:
        result = analyze_parens(l-1, r, temp+"(")
        print(f"result={result}")
        for i in result:
            ans.append(i)
    return ans

def analyze_parens(l, r, temp):
    ans = []
    if l == 0:
        temp = temp + ')' * r
        ans.append("".join(temp))
    
    elif r > l:
        result_l = analyze_parens(l-1, r, temp+"(")
        for i in result_l:
            ans.append(i)
        result_r = analyze_parens(l, r-1, temp+")")
        for i in result_r:
            ans.append(i)
    elif r == l:
        result = analyze_parens(l-1, r, temp+"(")
        for i in result:
            ans.append(i)
    return ans

def balanced_parens(n):
    result = analyze_parens(n, n, "")
    return result


def flat_list():
    a = ['ABC']
    b = ['DEF', 'Hi']
    c = ['Jkl', 'Mn']
    d = ['opq', 'RStu']
    a.extend(b)
    c.extend(d)
    print(a)
    print(c)

#flat_list()
print(balanced_parens(3))
