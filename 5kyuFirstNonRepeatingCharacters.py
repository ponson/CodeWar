def first_non_repeating_letter(string):
    chars = []
    char_counts = []
    for c in string:
        if c.upper() not in chars or c.lower() not in chars:
            chars.append(c)
            char_counts.append(1)
        else:
            index = chars.index(c)
            char_counts[index] += 1

    idx = char_counts.index(1)
    return chars[idx]
    

print(first_non_repeating_letter("aabbccdeef"))