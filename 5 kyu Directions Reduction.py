arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # --> ['WEST']


def dir_reduc(arr):
    for i in range(len(arr)):
        try:
            if [arr[i], arr[i + 1]] in [["NORTH", "SOUTH"], ["SOUTH", "NORTH"], ["WEST", "EAST"], ["EAST", "WEST"]]:
                arr.pop(i)
                arr.pop(i)
                dir_reduc(arr)
        except IndexError:
            continue
    return arr


print(dir_reduc(arr))
