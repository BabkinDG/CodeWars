arr = [1, 1, 1, 1]  # ==> 15


def binary_array_to_number(arr):
    degree = len(arr) - 1
    integer = 0
    for i in arr:
        integer += i * 2 ** degree
        degree += -1
    return integer


print(binary_array_to_number(arr))
