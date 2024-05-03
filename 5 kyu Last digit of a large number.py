n1, n2 = 11011883462491756089908974347790812064465223659411481701995, 2677128457901190823644030365586554344751878449520096799796


def last_digit(n1, n2):
    if n1 == 0 and n2 == 0:
        return 1
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0
    elif n2 % 4 == 1:
        return int(str(n1)[-1:])
    elif n2 % 4 == 2:
        return int(str(int(str(n1)[-1:]) ** 2)[-1])
    elif n2 % 4 == 3:
        return int(str(int(str(n1)[-1:]) ** 3)[-1])
    elif n2 % 4 == 0 and n1 % 2 == 1 and int(str(n1)[-1:]) != 5:
        return 1
    elif n2 % 4 == 0 and n1 % 2 == 1 and int(str(n1)[-1:]) == 5:
        return 5
    elif n2 % 4 == 0 and n1 % 2 == 0 and int(str(n1)[-1:]) % 10 == 0:
        return 0
    elif n2 % 4 == 0 and n1 % 2 == 0:
        return 6


print(f'должно быть: {pow(n1, n2, 10)}')
print(n2 % 4)
print(int(str(n1)[-1:]))
print(last_digit(n1, n2))
