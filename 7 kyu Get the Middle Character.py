s = 'test'  # --> 'es'


def get_middle(s):
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    elif len(s) % 2 == 0:
        return s[len(s) // 2 - 1] + s[len(s) // 2]


print(get_middle(s))
