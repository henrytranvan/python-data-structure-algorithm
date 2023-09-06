def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n -1)
        result = n * recurse
        return result


print(factorial(10))


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n -2)


for i in range(100):
    print(fibonacci(i))