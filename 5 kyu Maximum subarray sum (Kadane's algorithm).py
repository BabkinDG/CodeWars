numbers = [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]
# --> should be 155: [7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]


def max_sequence(numbers):
    sum, max_sum = 0, 0
    for x in numbers:
        sum = max(0, sum + x)
        max_sum = max(max_sum, sum)
    return max_sum


print(max_sequence(numbers))
