def analyze_parens(l, r, temp):
    ans = []
    if l == 0:
        for i in range(r):
            temp+")"
        return temp
    
    if r > l:
        ans.append(analyze_parens(l-1, r, temp+"("))
        ans.append(analyze_parens(l, r-1, temp+")"))

    return ans
def balanced_parens(n):
    result = analyze_parens(n, n, "")
    return result

balanced_parens(3)
