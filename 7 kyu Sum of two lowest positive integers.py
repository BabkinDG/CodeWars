def sum_two_smallest_numbers(numbers):
    min1 = min(numbers)
    numbers.remove(min(numbers))
    min2 = min(numbers)
    return min1+min2

numbers = [10, 343445353, 3453445, 3453545353453]
res = sum_two_smallest_numbers(numbers)
print(f'{res}')