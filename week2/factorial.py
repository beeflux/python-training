def factorial(n):
    i = 1
    f = 1
    while i<=n:
        f *= i
        i += 1
    return f

print(factorial(4))
