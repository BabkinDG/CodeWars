arr = ["Telescopes", "Glasses", "Eyes", "Monocles"] # -->["Eyes", "Glasses", "Monocles", "Telescopes"]


def sort_by_length(arr):
    for i1 in range(0, len(arr)):
        for i2 in range(i1+1, len(arr)):
            if len(arr[i1]) > len(arr[i2]):
                arr[i1], arr[i2] = arr[i2], arr[i1]
    return arr
    # return sorted(arr, key=len)

print(sort_by_length(arr))