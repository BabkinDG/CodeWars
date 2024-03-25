arr = [0, 1, 3]


def odd_or_even(arr):
    if arr == [0] or arr == []:
        return [0]
    elif sum(arr) % 2 == 0:
        return 'even'
    elif sum(arr) % 2 == 1 or sum(arr) // 2 == -1:
        return 'odd'


print(odd_or_even(arr))