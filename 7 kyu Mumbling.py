st = 'abcd' # 'A-Bb-Ccc-Dddd'

def accum(st):
    mum = ''
    for i in range(len(st)):
        mum += st[i].upper() + st[i].lower()*i
        if i != len(st)-1:
            mum += '-'
    return mum

print(accum(st))