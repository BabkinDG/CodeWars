s = "aaaxbbbbyyhwawiwjjjwwm"

def printer_error(s):
    er = 0
    r_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    for i in s:
        if i not in r_s:
            er += 1
    return f'{er}/{len(s)}'

print(printer_error(s))
