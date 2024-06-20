s = "turns out random test cases are easier than writing out basic ones"


def find_short(s):
    return min([len(word) for word in s.split()])


print(find_short(s))
