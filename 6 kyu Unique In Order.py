sequence = 'AAAABBBCCDAABBB'  # --> ["A", "B", "C", "D", "A", "B"]


def unique_in_order(sequence):
    arr = []
    if len(sequence) == 1:
        arr.append(sequence[0])
        return arr
    for i in range(0, len(sequence)):
        try:
            if sequence[i] != sequence[i+1]:
                arr.append(sequence[i])
        except IndexError:
            if sequence[i] != arr[-1:]:
                arr.append(sequence[i])
    return arr


print(unique_in_order(sequence))