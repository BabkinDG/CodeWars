customers = [10, 2, 3, 3]  # время необходимое каждому покупателю
number_of_checkout_tills = 2  # число касс


def queue_time(customers, number_of_checkout_tills):
    self_checkout_time = []
    if not customers:
        return 0
    if number_of_checkout_tills > len(customers):
        number_of_checkout_tills = len(customers)
    for i in range(number_of_checkout_tills):
        self_checkout_time.append(customers[i])
    for i in range(number_of_checkout_tills, len(customers)):
        self_checkout_time[self_checkout_time.index(min(self_checkout_time))] += customers[i]
    return max(self_checkout_time)


print(queue_time(customers, number_of_checkout_tills))