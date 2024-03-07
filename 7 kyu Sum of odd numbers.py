n = 5

def row_sum_odd_numbers(n):
    a = 1
    for i1 in range(1, n+1):
        list_n = []
        for i2 in range(i1):
            list_n.append(a)
            a += 2
        print(list_n)
    return sum(list_n)

print(row_sum_odd_numbers(n))

