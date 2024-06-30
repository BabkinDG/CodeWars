integers = [2, 4, 0, 100, 4, 11, 2602, 36]  # --> 11


def find_outlier(integers):
    odd, even = [], []
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        if i % 2 == 1:
            odd.append(i)
        if len(even) > 0 and len(odd) > 0 and (len(even) >= 2 or len(odd) >= 2):
            break
    if len(even) == 1:
        return even[0]
    if len(odd) == 1:
        return odd[0]


print(find_outlier(integers))
