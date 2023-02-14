def encode_rail_fence_cipher(string, n):
    y_idx = 0
    y_delta = 1
    cipher_parts = [] 
    for _ in range(n):
        cipher_parts.append([])
    for c in string:
        cipher_parts[y_idx].append(c)
        if y_idx == 0:
            y_delta = 1
        elif y_idx == n-1:
            y_delta = -1

        y_idx += y_delta

    result = ''
    for str_part in cipher_parts:
        result += ''.join(str_part)

    return result



def decode_rail_fence_cipher(string, n):
    str_len = len(string)
    parts_lens = []
    parts_strs = []
    for _ in range(n):
        parts_lens.append(0)
        parts_strs.append([])

    y_idx = 0
    y_delta = 1
    for _ in range(str_len):
        parts_lens[y_idx] += 1
        if y_idx == 0:
            y_delta = 1
        elif y_idx == n-1:
            y_delta = -1
        
        y_idx += y_delta

    index = 0
    for i in range(n):
        parts_strs[i] = list(string[index:parts_lens[i]+index])
        index += parts_lens[i]
        # print(f"line {i+1} len is: {parts_lens[i]}")
        # print(f"line {i+1} is: {parts_strs[i]}")

    final_str = ''
    y_idx = 0
    y_delta = 1
    for _ in range(str_len):
        final_str += parts_strs[y_idx].pop(0)
        if y_idx == 0:
            y_delta = 1
        elif y_idx == n-1:
            y_delta = -1

        y_idx += y_delta

    return final_str
# print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3)) #"WECRLTEERDSOEEFEAOCAIVDEN"
# print(encode_rail_fence_cipher("Hello, World!", 3)) #"Hoo!el,Wrdl l"
# print(encode_rail_fence_cipher("Hello, World!", 4)) #"H !e,Wdloollr"
# print(encode_rail_fence_cipher("", 3)) #""

print(decode_rail_fence_cipher("H !e,Wdloollr", 4))   #"Hello, World!"
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))  # "WEAREDISCOVEREDFLEEATONCE"
print(decode_rail_fence_cipher("", 3))  #""
