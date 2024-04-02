customers = [10, 2, 3, 3]  # время необходимое каждому покупателю
number_oct = 2  # number_of_checkout_tills число касс


def queue_time(customers, noct):
    sc_time = []  # self-checkout time
    if not customers:
        return 0
    if noct > len(customers):
        noct = len(customers)
    for i in range(noct):
        sc_time.append(customers[i])
    for i in range(noct, len(customers)):
        sc_time[sc_time.index(min(sc_time))] += customers[i]
    return max(sc_time)


print(queue_time(customers, number_oct))