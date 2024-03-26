begin_number, end_number, step = 2, 6, 2 # --> 12


def sequence_sum(begin_number, end_number, step):
    sequence = []
    if begin_number < end_number:
        while begin_number <= end_number:
            sequence.append(begin_number)
            begin_number += step
        return sum(sequence)
    elif begin_number > end_number:
        return 0
    elif begin_number == end_number:
        return begin_number


print(sequence_sum(begin_number, end_number, step))