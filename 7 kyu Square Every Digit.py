num = 9119

def square_digits(num):
    res = ''
    for i in str(num):
        res += str(int(i)**2)
    return int(res)

print(square_digits(num))