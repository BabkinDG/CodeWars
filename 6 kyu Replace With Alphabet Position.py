import string


text = "The sunset sets at twelve o' clock."
#  --> '20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11'


def alphabet_position(text):
    output_str = []
    for sym in text:
        if sym in string.ascii_letters:
            output_str.append(str(string.ascii_lowercase.index(sym.lower())+1))
    return ' '.join(output_str)


print(alphabet_position(text))
