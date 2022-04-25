


def unused_digits_v1(*args):
    digits=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in args:
        for i in range(10):
            if str(i) in str(num) and i in digits:
                digits.remove(i)

    result = ""
    for x in digits:
        result += str(x)

    return result


def unused_digits(*args):
    return "".join(num for num in "0123456789" if num not in str(args))

print(unused_digits(12, 34, 56, 78))
