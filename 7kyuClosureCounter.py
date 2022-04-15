def counter():
    count = 0

    def new_counter():
        nonlocal count
        count += 1
        return count
    return new_counter


new_func = counter()
print(new_func())
print(new_func())
