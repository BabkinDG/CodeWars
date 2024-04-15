r, g, b = 255, 255, 255  # --> 'FFFFFF'


def rgb(r, g, b):
    rgb_dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    def limit(x):
        if x < 0:
            x = 0
        elif x > 255:
            x = 255
        return x

    def hexadecimal(x):
        hexadecimal = ''
        hexadecimal += rgb_dic[x % 16]
        x = x // 16
        hexadecimal += rgb_dic[x % 16]
        return hexadecimal[::-1]

    return hexadecimal(limit(r)) + hexadecimal(limit(g)) + hexadecimal(limit(b))

print(rgb(r, g, b))
