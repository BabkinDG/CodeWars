import string


string_of_words = 'man i need a taxi up to ubud'  # --> 'taxi'


def high(string_of_words):
    sum_of_numbers = []
    list_of_words = string_of_words.split(' ')
    for i1 in list_of_words:
        number = 0
        for i2 in i1:
            number += string.ascii_lowercase.index(i2) + 1
        sum_of_numbers.append(number)
    return list_of_words[sum_of_numbers.index(max(sum_of_numbers))]


print(high(string_of_words))