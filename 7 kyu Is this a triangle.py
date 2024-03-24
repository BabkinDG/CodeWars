a, b, c = 7, 2, 2  # --> True


def is_triangle(a, b, c):
    if a < (b + c) and b < (a + c) and c < (b + a):
        return True
    else:
        return False


print(is_triangle(a, b, c))
