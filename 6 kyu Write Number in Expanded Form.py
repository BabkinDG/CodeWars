num = 603240  # --> '600000 + 3000 + 200 + 40'


def expanded_form(num):
    string = ''
    degree = len(str(num)) - 1
    for i in str(num):
        if i != '0':
            string += str(int(i) * 10 ** degree) + ' + '
        degree += -1
    return string[:-3]


print(expanded_form(num))
