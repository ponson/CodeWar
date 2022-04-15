


def swap_v1(string_):
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_str = capitals.lower()

    str_list = string_
    result_list = []
    for c in str_list:
        if c in capitals:
            result_list.append(c.lower())
        elif c in lower_str:
            result_list.append(c.upper())
        else:
            result_list.append(c)
    return "".join(result_list)


def swap_v2(string_):
    return string_.swapcase()


def swap_v3(string_):

    str_list = string_
    result_list = []
    for c in str_list:
        if c.isupper():
            result_list.append(c.lower())
        elif c.islower():
            result_list.append(c.upper())
        else:
            result_list.append(c)
    return "".join(result_list)


def swap(string_):

    return "".join(c.lower() if c.isupper() else c.upper() for c in string_)


print(swap("This is a Book."))