def first_non_repeating_letter(string):
    chars = []
    char_counts = []
    for c in string:
        if c.upper() not in chars and c.lower() not in chars:
            chars.append(c)
            char_counts.append(1)
        else:
            try:
                index = chars.index(c)
            except ValueError:
                if c.isupper():
                    index = chars.index(c.lower())
                else:
                    index = chars.index(c.upper())
            char_counts[index] += 1

    try:
        idx = char_counts.index(1)
    except ValueError:
        return ""
    return chars[idx]
    

# print(first_non_repeating_letter("aabbccdeef"))
# print(first_non_repeating_letter("aabbccee"))
# print(first_non_repeating_letter(""))
print(first_non_repeating_letter("sTreSS"))
print(first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))
