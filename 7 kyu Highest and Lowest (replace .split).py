numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4" # return "42 -9"

def high_and_low(numbers):

    def list_split(sym_split, split_string):
        sym_split_list = []
        splited_str = ''
        for i in split_string:
            if i != sym_split:
                splited_str += i
            elif i == sym_split:
                if splited_str != '':
                    sym_split_list.append(splited_str)
                splited_str = ''
        if splited_str != '':
            sym_split_list.append(splited_str)
        return sym_split_list

    list = []
    for i in list_split(' ', numbers):
        list.append(int(i))
    print(list)
    return f'{max(list)} {min(list)}'

print(high_and_low(numbers))