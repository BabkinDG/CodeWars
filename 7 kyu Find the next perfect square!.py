from math import sqrt
sq = 121


def find_next_square(sq):
    if sqrt(sq) % 1 == 0:
        return (sqrt(sq) + 1) ** 2
    else:
        return -1

print(find_next_square(sq))