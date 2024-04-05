import string


letter = 'The quick, brown fox jumps over the lazy dog!'


def is_pangram(latter):
    for i in string.ascii_lowercase:
        if latter.lower().count(i) < 1:
            return False
    else:
        return True


print(is_pangram(letter))