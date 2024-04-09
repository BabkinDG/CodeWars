roman_num = 'MCMXCIV' # --> 1994


def solution(roman_num : str) -> int:
    integer = 0
    roman_num = ' ' + roman_num + ' '
    for i in range(1, len(roman_num)-1):
        if roman_num[i] == 'I' and roman_num[i+1] != 'V' and roman_num[i+1] != 'X':
            integer += 1
        elif roman_num[i] == 'V' and roman_num[i-1] != 'I':
            integer += 5
        elif roman_num[i] == 'V' and roman_num[i-1] == 'I':
            integer += 4
        elif roman_num[i] == 'X' and roman_num[i-1] != 'I' and roman_num[i+1] != 'L' and roman_num[i+1] != 'C':
            integer += 10
        elif roman_num[i] == 'X' and roman_num[i-1] == 'I' and roman_num[i+1] != 'L' and roman_num[i+1] != 'C':
            integer += 9
        elif roman_num[i] == 'L' and roman_num[i-1] != 'X':
            integer += 50
        elif roman_num[i] == 'L' and roman_num[i-1] == 'X':
            integer += 40
        elif roman_num[i] == 'C' and roman_num[i-1] != 'X' and roman_num[i+1] != 'D' and roman_num[i+1] != 'M':
            integer += 100
        elif roman_num[i] == 'C' and roman_num[i-1] == 'X' and roman_num[i+1] != 'D' and roman_num[i+1] != 'M':
            integer += 90
        elif roman_num[i] == 'D' and roman_num[i-1] != 'C':
            integer += 500
        elif roman_num[i] == 'D' and roman_num[i-1] == 'C':
            integer += 400
        elif roman_num[i] == 'M' and roman_num[i-1] != 'C':
            integer += 1000
        elif roman_num[i] == 'M' and roman_num[i-1] == 'C':
            integer += 900
    return integer


print(solution(roman_num))
