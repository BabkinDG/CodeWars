numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4" # return "42 -9"

def high_and_low(numbers):
    list = []
    for i in numbers.split(' '):
        list.append(int(i))
    print(list)
    return f'{max(list)} {min(list)}'

print(high_and_low(numbers))