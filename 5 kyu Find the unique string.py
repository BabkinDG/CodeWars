array_list = ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']  # --> 'BbBb'


def find_uniq(array_list):

    array = []

    for i in array_list:
        if i.count(' ') == len(i) or i == '':
            array.append('EMPTY')
        elif i[0].lower() * len(i) == i.lower():
            array.append(i[0].lower())
        else:
            for n in i:
                array.append(n.lower())
    print(array)

    for i in set(array_list):
        if i.count(' ') == len(i) and array.count('EMPTY') == 1:
            return i
        else:
            for n in set(i.lower()):
                if array.count(n) == 1:
                    return i


print(find_uniq(array_list))
