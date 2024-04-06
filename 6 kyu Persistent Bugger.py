num = 999 # --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)


def persistence(num):
    number_of_times = 0
    while len(str(num)) > 1:
        per_num = 1
        number_of_times += 1
        for i in str(num):
            per_num *= int(i)
        num = per_num
    return number_of_times


print(persistence(num))
