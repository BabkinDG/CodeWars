array = [1, 1, 1, 2, 1, 1]  # --> 2


def find_uniq(array):
    for uniq in set(array):
        if array.count(uniq) == 1:
            return uniq


print(find_uniq(array))
