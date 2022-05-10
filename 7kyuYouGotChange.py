def give_change(amount):
    coins = [100, 50, 20, 10, 5, 1]
    remain = amount
    result = []
    for x in coins:
        result.append(remain // x)
        remain = remain % x

    result.reverse()
    return result


print(give_change(365))