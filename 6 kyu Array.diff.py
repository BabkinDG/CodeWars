list_a = [1, 2, 2, 2, 5, 6, 7]
list_b = [1, 2]


def array_diff(a, b):
    if a == [] or b == []:
        return a
    for i in b:
        while i in a:
            a.remove(i)
    return a


print(array_diff(list_a, list_b))
