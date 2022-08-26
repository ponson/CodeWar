def duplicate_count(text):
    low_text = text.lower()
    chars = set(low_text)
    result = 0
    for char in chars:
        if low_text.count(char) > 1:
            result += 1
    
    return result


print(duplicate_count("")) # 0)
print(duplicate_count("abcde")) # 0)
print(duplicate_count("abcdeaa")) # 1)
print(duplicate_count("abcdeaB")) # 2)
print(duplicate_count("Indivisibilities")) # 2)