n_floors = 2  # --> [' * ', '***']


def tower_builder(n_floors):
    air = ''
    floor = ''
    home = []
    for i in range(1, n_floors+1):
        air = int(((n_floors*2 - (i*2-1)) - 1) / 2)
        floor = ' ' * air + '*' * (i*2-1) + ' ' * air
        home.append(floor)
    return home


print(tower_builder(n_floors))
