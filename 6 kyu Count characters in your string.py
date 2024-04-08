string = 'aba'  # --> {'a': 2, 'b': 1}


def count(string):
    dictionary = {}
    for i in string:
        if i not in dictionary:
            dictionary.update({str(i): string.count(i)})
    return dictionary


print(count(string))
