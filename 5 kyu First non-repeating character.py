str = 'sTreSS'


def first_non_repeating_letter(str):
    for i in str:
        if str.lower().count(i.lower()) == 1:
            return i
    return ''


print(first_non_repeating_letter(str))
