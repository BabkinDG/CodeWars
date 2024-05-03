strng = "2000 10003 1234000 44444444 9999 11 11 22 123"  # --> "11 11 2000 10003 22 123 1234000 44444444 9999"


def order_weight(strng):
    strng_list = strng.split()
    n_list = []
    strng.split()
    for i in strng_list:
        n_sum = 0
        for n in i:
            n_sum += int(n)
        n_list.append(n_sum)
    for i1 in range(len(n_list)):
        for i2 in range(i1 + 1, len(n_list)):
            if n_list[i1] > n_list[i2]:
                n_list[i1], n_list[i2] = n_list[i2], n_list[i1]
                strng_list[i1], strng_list[i2] = strng_list[i2], strng_list[i1]
            elif n_list[i1] == n_list[i2] and str(strng_list[i1]) > str(strng_list[i2]):
                n_list[i1], n_list[i2] = n_list[i2], n_list[i1]
                strng_list[i1], strng_list[i2] = strng_list[i2], strng_list[i1]
    return ' '.join(strng_list)


print(order_weight(strng))
