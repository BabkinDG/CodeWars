lst = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1] # --> [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]


def move_zeros(lst):
    res_lst = []
    for i in range(len(lst)):
        if lst[i] != 0:
            res_lst.append(lst[i])
    res_lst += [0]*(len(lst)-len(res_lst))
    return res_lst


print(move_zeros(lst))
