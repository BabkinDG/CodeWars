names = ['Alex', 'Jacob', 'Mark', 'Max']


def likes(names):
    like_text = ''
    if names == []:
        like_text = 'no one likes this'
    if len(names) == 1:
        like_text = f'{names[0]} likes this'
    if len(names) == 2:
        like_text = f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        like_text = f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) > 3:
        like_text = f'{names[0]}, {names[1]} and {len(names)-2} others like this'
    return like_text


print(likes(names))
