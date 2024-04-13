seconds = 359999  # --> 99:59:59


def make_readable(seconds):
    HH = str(seconds // (60*60))
    if HH == '0':
        HH = '00'
    if len(HH) == 1:
        HH = '0' + HH
    MM = str(seconds % (60*60) // 60)
    if MM == '0':
        MM = '00'
    if len(MM) == 1:
        MM = '0' + MM
    SS = str((seconds % (60*60)) % 60)
    if SS == '0':
        SS = '00'
    if len(SS) == 1:
        SS = '0' + SS
    result = HH + ':' + MM + ':' + SS
    return result


print(make_readable(seconds))