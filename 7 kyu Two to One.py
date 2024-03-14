a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"

def longest(a1, a2):
    a = "abcdefghijklmnopqrstuvwxyz"
    one = ''
    for i in a1:
        if i not in one:
            one += i
    for i in a2:
        if i not in one:
            one += i
    sorted_a = ''
    for i in a:
        if i in one:
            sorted_a += i
    return sorted_a

print(longest(a1, a2))
