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

def first_non_repeating_letter2(string):
    string_lower = string.lower()
    job1 = enumerate(string_lower)
    print(type(job1))
    print(list(job1))
    for i, letter in job1: 
        if string_lower.count(letter) == 1:
            return string[i]
            
    return ""

# print(first_non_repeating_letter("aabbccdeef"))
# print(first_non_repeating_letter("aabbccee"))
# print(first_non_repeating_letter(""))
# print(first_non_repeating_letter("sTreSS"))
# print(first_non_repeating_letter("Go hang a salami, I\'m a lasagna hog!"))

print(first_non_repeating_letter2("sTreSS"))
# l1 = ["eat", "sleep", "repeat"]
# obj1 = enumerate(l1)
# print ("Return type:", type(obj1))
# print (list(obj1))