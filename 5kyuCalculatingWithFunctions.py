def zero(*args): #your code here
    if not args:
        return 0
    else:
        if args[0][0] == '+':
            return 0 + args[0][1]
        elif args[0][0] == '-':
            return 0 - args[0][1]
        elif args[0][0] == '*':
            return 0 * args[0][1]
        elif args[0][0] == '/':
            return 0 // args[0][1]


def one(*args): #your code here
    if not args:
        return 1
    else:
        if args[0][0] == '+':
            return 1 + args[0][1]
        elif args[0][0] == '-':
            return 1 - args[0][1]
        elif args[0][0] == '*':
            return 1 * args[0][1]
        elif args[0][0] == '/':
            return 1 // args[0][1]


def two(*args): #your code here
    if not args:
        return 2
    else:
        if args[0][0] == '+':
            return 2 + args[0][1]
        elif args[0][0] == '-':
            return 2 - args[0][1]
        elif args[0][0] == '*':
            return 2 * args[0][1]
        elif args[0][0] == '/':
            return 2 // args[0][1]


def three(*args): #your code here
    if not args:
        return 3
    else:
        if args[0][0] == '+':
            return 3 + args[0][1]
        elif args[0][0] == '-':
            return 3 - args[0][1]
        elif args[0][0] == '*':
            return 3 * args[0][1]
        elif args[0][0] == '/':
            return 3 // args[0][1]


def four(*args): #your code here
    if not args:
        return 4
    else:
        if args[0][0] == '+':
            return 4 + args[0][1]
        elif args[0][0] == '-':
            return 4 - args[0][1]
        elif args[0][0] == '*':
            return 4 * args[0][1]
        elif args[0][0] == '/':
            return 4 // args[0][1]


def five(*args): #your code here
    if not args:
        return 5
    else:
        if args[0][0] == '+':
            return 5 + args[0][1]
        elif args[0][0] == '-':
            return 5 - args[0][1]
        elif args[0][0] == '*':
            return 5 * args[0][1]
        elif args[0][0] == '/':
            return 5 // args[0][1]


def six(*args): #your code here
    if not args:
        return 6
    else:
        if args[0][0] == '+':
            return 6 + args[0][1]
        elif args[0][0] == '-':
            return 6 - args[0][1]
        elif args[0][0] == '*':
            return 6 * args[0][1]
        elif args[0][0] == '/':
            return 6 // args[0][1]


def seven(*args): #your code here
    if not args:
        return 7
    else:
        if args[0][0] == '+':
            return 7 + args[1]
        elif args[0][0] == '-':
            return 7 - args[1]
        elif args[0][0] == '*':
            return 7 * args[1]
        elif args[0][0] == '/':
            return 7 // args[1]


def eight(*args): #your code here
    if not args:
        return 8
    else:
        if args[0][0] == '+':
            return 8 + args[0][1]
        elif args[0][0] == '-':
            return 8 - args[0][1]
        elif args[0][0] == '*':
            return 8 * args[0][1]
        elif args[0][0] == '/':
            return 8 // args[0][1]


def nine(*args): #your code here
    if not args:
        return 9
    else:
        if args[0][0] == '+':
            return 9 + args[0][1]
        elif args[0][0] == '-':
            return 9 - args[0][1]
        elif args[0][0] == '*':
            return 9 * args[0][1]
        elif args[0][0] == '/':
            return 9 // args[0][1]

def plus(num): #your code here
    return '+', num


def minus(num): #your code here
    return '-', num

def times(num): #your code here
    return '*', num


def divided_by(num): #your code here
    return '/', num

print(three(times(seven())))
