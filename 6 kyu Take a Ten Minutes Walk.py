walk_arr = ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']  # --> True


def is_valid_walk(walk_arr):
    walk_sum = [0, 0, 0, 0]
    for i in walk_arr:
        if i == 'n':
            walk_sum[0] += 1
        elif i == 's':
            walk_sum[1] += 1
        elif i == 'w':
            walk_sum[2] += 1
        elif i == 'e':
            walk_sum[3] += 1
    if sum(walk_sum) == 10 and walk_sum[0] - walk_sum[1] == 0 and walk_sum[2] - walk_sum[3] == 0:
        return True
    else:
        return False


print(is_valid_walk(walk_arr))
