def solution(args):
    output = []
    buf = []
    for num in args:
        if len(buf) == 0:
            buf.append(num)
        else:
            if buf[-1]+1 == num:
                buf.append(num)
            else:
                if len(buf) < 3:
                    for i in buf:
                        output.append(str(i))
                else:
                    output.append(f"{buf[0]}-{buf[-1]}")
                buf.clear()
                buf.append(num)
    if len(buf) < 3:
        for i in buf:
            output.append(str(i))
    else:
        output.append(f"{buf[0]}-{buf[-1]}")
    buf.clear()

    return ','.join(output)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
#'-6,-3-1,3-5,7-11,14,15,17-20'
print(solution([-3,-2,-1,2,10,15,16,18,19,20]))
#'-3--1,2,10,15,16,18-20'
