def points(games):
    sum_p = 0
    for i in range(len(games)):
        if int(games[i][0]) > int(games[i][2]):
            sum_p += 3
        elif int(games[i][0]) == int(games[i][2]):
            sum_p += 1
    return sum_p

games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
print(points(games))