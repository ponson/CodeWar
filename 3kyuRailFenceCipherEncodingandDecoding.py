import itertools


def encode_rail_fence_cipher(string, n):
    y_idx, y_delta = 0, 1
    cipher_parts = [[] for _ in range(n)]
    for c in string:
        cipher_parts[y_idx].append(c)
        if (y_idx == 0 and y_delta == -1) or (y_idx == n-1 and y_delta == 1):
            y_delta *= -1
        y_idx += y_delta
    
    result = ''
    result += ''.join("".join(x) for x in cipher_parts)

    return result


def decode_rail_fence_cipher(string, n):
    str_len = len(string)
    parts_index_lst =[[] for _ in range(n)]
    r = list(range(n))
    rails_idx = itertools.cycle(r + r[-2:0:-1])

    for i in range(str_len):
        parts_index_lst[next(rails_idx)].append(i)

    full_index = list(itertools.chain(*parts_index_lst))
    print(full_index)

    return ''.join(sorted(string, key=lambda x: full_index.pop(0)))
    

print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3)) #"WECRLTEERDSOEEFEAOCAIVDEN"
print(encode_rail_fence_cipher("Hello, World!", 3)) #"Hoo!el,Wrdl l"
print(encode_rail_fence_cipher("Hello, World!", 4)) #"H !e,Wdloollr"
print(encode_rail_fence_cipher("", 3)) #""

print(decode_rail_fence_cipher("H !e,Wdloollr", 4))   #"Hello, World!"
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))  # "WEAREDISCOVEREDFLEEATONCE"
print(decode_rail_fence_cipher("", 3))  #""
