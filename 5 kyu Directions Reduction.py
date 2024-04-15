arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # --> ['WEST']


def dir_reduc(arr):
    while ' ' in arr:
        arr.remove(' ')
    for i in range(len(arr)):
        try:
            if [arr[i], arr[i + 1]] == ["NORTH", "SOUTH"]:
                arr[i] = ' '
                arr[i + 1] = ' '
                dir_reduc(arr)
            elif [arr[i], arr[i + 1]] == ["SOUTH", "NORTH"]:
                arr[i] = ' '
                arr[i + 1] = ' '
                dir_reduc(arr)
            elif [arr[i], arr[i + 1]] == ["WEST", "EAST"]:
                arr[i] = ' '
                arr[i + 1] = ' '
                dir_reduc(arr)
            elif [arr[i], arr[i + 1]] == ["EAST", "WEST"]:
                arr[i] = ' '
                arr[i + 1] = ' '
                dir_reduc(arr)
        except IndexError:
            continue
    return arr


print(dir_reduc(arr))
