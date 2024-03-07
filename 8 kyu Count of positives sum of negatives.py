def count_positives_sum_negatives(arr):
    count_p = 0
    sum_n = 0
    result = []
    if arr != []:
        for n in arr:
            if n < 0:
                sum_n += n
            elif n > 0:
                count_p += 1
        result.append(count_p)
        result.append(sum_n)
        return result
    else:
        return result

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(arr))