import re
def solution(s):
    m = re.findall('[A-Z]', s)
    if m:
        cur_idx = 0
        result = []
        add_cap = ''
        for capital in m:
            r_string = s[cur_idx:] 
            f_idx = r_string.find(capital)
            result.append(add_cap + r_string[:f_idx])
            add_cap = capital
            cur_idx += f_idx + 1
        if cur_idx < len(s):
            end_idx = len(s)
            result.append(add_cap + s[cur_idx: end_idx])
        elif cur_idx == len(s):
            result.append(add_cap)
        res_str = " ".join(result)
        return res_str.strip()
    else:
        return s


def retest():
    source = "Young Frankenstein"
    m = re.findall('[A-Z]', source)
    if m:
        print(m)

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
print(solution("ABCDE"))
print(solution("allcharislowercase"))
