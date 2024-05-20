s1 = 'cedewaraaossoqqyt'
s2 = 'codewars'  # --> True


def scramble(s1, s2):
    for i in set(s2):
        if s2.count(i) > s1.count(i):
            return False
    return True


print(scramble(s1, s2))
