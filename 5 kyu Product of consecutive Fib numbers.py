prod = 4895  # --> [55, 89, True]


def product_fib(prod):
    fib_list = [0, 1]
    i = 2
    while fib_list[i - 1] * fib_list[i - 2] <= prod:
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        if fib_list[i - 1] * fib_list[i - 2] == prod:
            return [fib_list[i - 2], fib_list[i - 1], True]
        i += 1
    return [fib_list[i - 2], fib_list[i - 1], False]


print(product_fib(prod))
