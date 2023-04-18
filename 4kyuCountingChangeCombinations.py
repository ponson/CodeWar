def counting(money, coins, orig_item, answer):
    item = orig_item.copy()
    if len(coins) == 1:
        if money % coins[0] == 0:
            for _ in range(money //coins[0]):
                item.append(coins[0])
            if item not in answer:
                answer.append(item.copy())
            return 1
        else:
            return 0
    else:
        loops = money // coins[-1]
        for t in range(0, loops+1):
            for _ in range(t):
                item.append(coins[-1])
            
            result = counting(money - t*coins[-1], coins[:-1], item, answer)
            if result == 0:
                for _ in range(t):
                    item.remove(coins[-1])
            else:
                item = orig_item.copy()


    return result 

def count_change(money, coins):
    if money == 0:
        return 1
    coins.sort()
    answer = []
    for idx in range(len(coins)):
        if (money % coins[idx]) == 0:
            item = []
            for _ in range(money // coins[idx]):
                item.append(coins[idx])
            answer.append(item.copy())
        if idx > 0:
            item = [coins[idx]]
            counting(money - coins[idx], coins[:idx+1], item, answer)
    return len(answer)


print(count_change(1230, [120, 71, 82, 342]))
print(count_change(4, [1, 2]))# 3)
print(count_change(10, [5, 2, 3]))# 4)
print(count_change(11, [5, 7]))# 0)
print(count_change(0, [1, 2]))# 1)
