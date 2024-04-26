sentence = 'Hey fellow warriors'  # --> 'Hey wollef sroirraw'


def spin_words(sentence):
    res_sentence = []
    for i in sentence.split():
        if len(i) >= 5:
            res_sentence.append(i[::-1])
        else:
            res_sentence.append(i)
    return ' '.join(res_sentence)


print(spin_words(sentence))
