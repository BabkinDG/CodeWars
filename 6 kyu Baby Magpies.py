bird1 = "BWBWBW"
bird2 = "BWBWBB"
bird3 = "WWWWBB"


def child(bird1, bird2):
    difference_list = []
    for i in range(len(bird1)):
        difference_list.append(bird1[i] == bird2[i])
    if bird1 == bird2:
        return False
    elif difference_list.count(False) <= 2:
        return True
    else:
        return False


def grandchild(bird1, bird2):
    difference_list = []
    for i in range(len(bird1)):
        difference_list.append(bird1[i] == bird2[i])
    if bird1 != bird2 and len(bird1) == 1:
        return False
    elif difference_list.count(False) <= 4:
        return True
    else:
        return False


print(child(bird1, bird2))
print(grandchild(bird2, bird3))
