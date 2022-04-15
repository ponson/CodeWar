from itertools import accumulate


def make_coffee(order_remaining):
    cook_time = order_remaining[0]
    if len(order_remaining) > 1:
        cook_time = cook_time + 2 + make_coffee(order_remaining[1:])
        return cook_time
    else:
        return cook_time


def barista1(coffees):
    if not bool(coffees):
        return 0
    coffees.sort()
    total_time = 0
    for i in range(len(coffees)):
        total_time += make_coffee(coffees[:i+1])

    return total_time


def barista(coffees):
    return sum(accumulate( sorted(coffees), lambda a,c:a+2+c ))


def test_lambda(coffees):
    return sum(accumulate( sorted(coffees), lambda a,c:(print(f"a={a}, c={c}"),  a+2+c)))


print(barista([]))
print(barista([5]))
print(barista([20, 5]))
print(barista([4,3,2]))
print(barista([3, 2, 5, 10, 9]))


# print(test_lambda([5]))
print(test_lambda([20, 5]))
print(test_lambda([4,3,2]))
print(test_lambda([3, 2, 5, 10, 9]))
