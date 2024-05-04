dice = [5, 5, 5, 3, 3]  # --> 500


def score(dice):
    points = 0
    if dice.count(1) >= 3:
        points += 1000 + (dice.count(1) - 3) * 100
    if dice.count(1) < 3:
        points += dice.count(1) * 100
    if dice.count(6) >= 3:
        points += 600
    if dice.count(5) >= 3:
        points += 500 + (dice.count(5) - 3) * 50
    if dice.count(5) < 3:
        points += dice.count(5) * 50
    if dice.count(4) >= 3:
        points += 400
    if dice.count(3) >= 3:
        points += 300
    if dice.count(2) >= 3:
        points += 200
    return points


print(score(dice))
