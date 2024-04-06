source_array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # --> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


def sort_array(source_array):
    for i1 in range(0, len(source_array)):
        for i2 in range(i1 + 1, len(source_array)):
            if source_array[i1] > source_array[i2] and source_array[i1] % 2 == 1 and source_array[i2] % 2 == 1:
                source_array[i1], source_array[i2] = source_array[i2], source_array[i1]
    return source_array


print(sort_array(source_array))