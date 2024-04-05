array = ['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']  # --> 'foo'


def find_uniq(array):

    array_list = []

    for i in array:
        if i.count(' ') == len(i) or i == '':
            array_list.append('EMPTY')
        elif i[0].lower() * len(i) == i.lower():
            array_list.append(i[0].lower())
        else:
            for n in i:
                array_list.append(n.lower())
    print(array_list)

    for i in set(array):
        if i.count(' ') == len(i) and array_list.count('EMPTY') == 1:
            return i
        else:
            for n in set(i.lower()):
                if array_list.count(n) == 1:
                    return i


print(find_uniq(array))
