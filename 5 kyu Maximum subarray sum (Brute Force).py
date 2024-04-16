arr = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
# --> should be 155: [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]


def max_sequence(arr):
    max_sum = 0
    for i1 in range(len(arr)):
        if arr[i1] > 0:
            for i2 in range(i1+1, len(arr)+1):
                if arr[i2-1] > 0:
                    if sum(arr[i1:i2]) > max_sum:
                        max_sum = sum(arr[i1:i2])
    return max_sum


print(max_sequence(arr))
