numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"  # return "42 -9"

def high_and_low(numbers):
    def list_split(split_sym, split_string):
        split_list = []
        split_str = ''
        for i in split_string:
            if i != split_sym:
                split_str += i
            elif i == split_sym:
                if split_str != '':
                    split_list.append(int(split_str))
                split_str = ''
        if split_str != '':
            split_list.append(int(split_str))
        return split_list

    print(list_split(' ', numbers))
    return f'{max(list_split(' ', numbers))} {min(list_split(' ', numbers))}'

print(high_and_low(numbers))
