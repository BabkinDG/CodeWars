n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # --> '(123) 456-7890'


def create_phone_number(n):
    number = ''
    for num in range(len(n)):
        if num == 0:
            number += '('
        if num == 3:
            number += ') '
        if num == 6:
            number += '-'
        number += str(n[num])
    return number


print(create_phone_number(n))
