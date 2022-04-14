
def solution_v1(number):
    if number < 0:
        return 0

    list_3_5 = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            list_3_5.append(i)

    print(list_3_5)

    return sum(list_3_5)


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


print(solution(-5))
print(solution(10))
print(solution(2))
print(solution(15))
print(solution(159))
