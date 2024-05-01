import string


strng = 'fo99obar99'  # --> 'fo99obar100'


def increment_string(strng):
    num = []
    for i in strng[::-1]:
        if i in string.digits:
            num.append(i)
        else:
            break
    if len(num) == 0:
        return strng + '1'
    last_num_str = str(int(''.join(num[::-1]))+1)
    strng = strng[:len(strng)-len(num)] + '0'*(len(num)-len(last_num_str)) + last_num_str
    return strng


print(increment_string(strng))
