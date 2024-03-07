def digitize(n):
    number_rev_list = []
    for i in range(1, len(str(n))+1):
        number_rev_list.append(int(str(n)[len(str(n)) - i]))
    # for i in string(n)[::-1]:            # альтернативный код
    #     number_rev_list.append(i)     # альтернативный код
    return number_rev_list

number = int(input('Enter the number: '))
print(digitize(number))