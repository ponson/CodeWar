def xo(s):
    lower_str = s.lower()
    count_x = lower_str.count('x')
    count_o = lower_str.count('o')
    if count_x == count_o:
        return True
    else:
        return False

print(xo("True expected"))
print(xo("oue expected"))
