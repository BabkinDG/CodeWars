def find_needle(haystack):
    for i in range(0, len(haystack)):
        if haystack[i] == 'needle':
            return f'found the needle at position {i}'

haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print(find_needle(haystack))