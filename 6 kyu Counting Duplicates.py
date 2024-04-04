input_string = 'mDVYaQzWvtNahqVMWwvjcHNhsdJuu9k5ieIN0NLhsBUsZdbuQenYC07WhaqkwuN0FLj0' # --> 20


def duplicate_count(input_string):
    duplicates = 0
    input_string_list = []
    duplicates_list = []
    for i in input_string:
        input_string_list.append(i.lower())
    for i in input_string_list:
        if input_string_list.count(i) >= 2 and i not in duplicates_list:
            duplicates_list.append(i)
            duplicates += 1
    return duplicates


print(duplicate_count(input_string))