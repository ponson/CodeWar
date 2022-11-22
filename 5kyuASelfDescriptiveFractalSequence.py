from PonsonModules.decorators import timer


def check_rules(curlist, trimm, count):
    if curlist[:len(trimm)] == trimm and curlist[len(trimm)] == count:
        return count
    return 0

@timer
def a112382(n):
    output = [1]
    up_trimm = []
    new_num_start = 2
    new_num_count = 1
    for i in range(n):
        num = check_rules(output, up_trimm, new_num_count)
        if  num > 0:
            output.append(num)
            up_trimm.append(num)
            new_num_count = 0
        else:
            output.append(new_num_start)
            new_num_start += 1
            new_num_count += 1

    return output[n] 

print(a112382(100000))