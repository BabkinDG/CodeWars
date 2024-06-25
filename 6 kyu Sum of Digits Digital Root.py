n = 132189  # -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6


def digital_root(n):
    while len(str(n)) > 1:
        n = sum([int(dit) for dit in str(n)])
    return n


print(digital_root(n))
