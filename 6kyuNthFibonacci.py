def nth_fib(n):
    fibonacci = [0, 1]
    if n < 3:
        return fibonacci[n-1]
    for i in range(1, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i])

    return fibonacci[n-1]


print(nth_fib(1))
print(nth_fib(2))
print(nth_fib(3))
print(nth_fib(4))
print(nth_fib(5))
print(nth_fib(6))
print(nth_fib(40))
print(nth_fib(50))
print(nth_fib(51))
