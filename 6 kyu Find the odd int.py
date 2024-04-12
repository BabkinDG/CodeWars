seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5] # --> should return 5 (because it appears 3 times)


def find_it(seq):
    num = 0
    for i in set(seq):
        if abs(seq.count(i) % 2) == 1:
            num = i
    return num


print(find_it(seq))
