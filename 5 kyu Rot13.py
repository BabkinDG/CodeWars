import string


message = 'aA bB zZ 1234 *!?%'  # --> 'nN oO mM 1234 *!?%'


def rot13(message):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    rot13_message = ''
    for i in message:
        if i in string.ascii_lowercase:
            rot13_message += lower[(lower.index(i) + 13) % 26]
        elif i in upper:
            rot13_message += upper[(upper.index(i) + 13) % 26]
        else:
            rot13_message += i
    return rot13_message


print(rot13(message))
