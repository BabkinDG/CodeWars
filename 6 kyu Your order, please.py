sentence = '4of Fo1r pe6ople g3ood th5e the2'  # --> "Fo1r the2 g3ood 4of th5e pe6ople"


def order(sentence):
    if sentence == '':
        return ''
    sen_list = sentence.split(' ')
    res_list = [0]*len(sen_list)
    res_str = ''
    for i in sen_list:
        for n in range(len(sen_list)):
            if str(n+1) in i:
                res_list[n] = i
    res_str = ' '.join(res_list)
    return res_str


print(order(sentence))