from decorators import timer, count_calls, cache


def fibonacci_time_out(n):
    fibonacci_list = [0, 1]
    if n < 2:
        return fibonacci_list[n]
    for i in range(2, n+1):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])

    return fibonacci_list[n]

def memorized(f):

    cache = {}

    def wrapped(n):
        ans = cache.get(n)
        if ans is None:
            cache[n] = f(n)
        return cache[n]
    return wrapped


# @cache
# @count_calls
@memorized
def fibonacci(n):

    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer
def test_time_usage(func_name, times):
    func_name(times)

fibonacci(30)
test_time_usage(fibonacci, 30)
# print(fibonacci(70))
# print(fibonacci(60))
# print(fibonacci(50))
