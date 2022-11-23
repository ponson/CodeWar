from PonsonModules.decorators import timer


def check_rules(curlist, trimm, count):
    if curlist[:len(trimm)] == trimm and curlist[len(trimm)] == count:
        return count
    return 0

@timer
def a112382(n):
    output = [1] 
    new_num_start = 2
    trimm_idx = 0
    while len(output) <= n:
        output.append(output[trimm_idx])
        trimm_idx += 1
        for nc in range(output[trimm_idx]):
            output.append(new_num_start)
            new_num_start += 1

    return output[n] 

print(a112382(100000))