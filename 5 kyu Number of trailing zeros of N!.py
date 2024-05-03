n = 1000


def factorial(n):
    res, dev = 0, 5
    while n // dev > 0:
        res += n // dev
        dev *= 5
    return res


print(n, factorial(n))
