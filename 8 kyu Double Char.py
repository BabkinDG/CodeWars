string = "Hello World"


def double_char(string):
    double_string = ''
    for i in string:
        double_string += i*2
    return double_string


print(double_char(string))