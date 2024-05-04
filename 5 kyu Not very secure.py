import string


password = "PassW0rd"  # --> True


def alphanumeric(password):
    if password == '':
        return False
    for i in set(password):
        if i not in string.ascii_uppercase and i not in string.ascii_lowercase and i not in string.digits:
            return False
    return True


print(alphanumeric(password))
