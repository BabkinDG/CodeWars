dice = [5, 5, 5, 3, 3]  # --> 500


def score(dice):
    points = 0
    if dice.count(1) >= 3:
        points += 1000 + (dice.count(1) - 3) * 100
    if dice.count(1) < 3:
        points += dice.count(1) * 100
    if dice.count(5) >= 3:
        points += (dice.count(5) - 3) * 50
    if dice.count(5) < 3:
        points += dice.count(5) * 50
    for i in [2, 3, 4, 5, 6]:
        if dice.count(i) >= 3:
            points += i * 100
    return points


print(score(dice))
