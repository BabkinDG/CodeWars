text = 'O tempora o mores !'  # --> Oay emporatay oay oresmay !


def pig_it(text):
    text_lst = text.split(' ')
    for i in range(len(text_lst)):
        text_lst[i] = text_lst[i][1:] + text_lst[i][0]
        if text_lst[i] != '!' and text_lst[i] != '?':
            text_lst[i] += 'ay'
    text = ' '.join(text_lst)
    return text


print(pig_it(text))