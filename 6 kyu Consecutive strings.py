strarr = ["zone", "abigail", "theta", "form", "libe", "zas"] # --> "abigailtheta"
k = 2


def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''
    len_sum = 0
    max_i = 0
    res_str = ''
    for i in range(len(strarr)+1-k):
        current_len_sum = 0
        for n in range(k):
            current_len_sum += len(strarr[i + n])
        if current_len_sum > len_sum:
            len_sum = current_len_sum
            max_i = i
    for i in range(k):
        res_str += strarr[max_i+i]
    return res_str


print(longest_consec(strarr, k))
