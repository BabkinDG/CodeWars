word = 'Success'  # --> ')())())'


def duplicate_encode(word):
    encode_str = ''
    for w in word:
        if word.lower().count(w.lower()) == 1:
            encode_str += '('
        else:
            encode_str += ')'
    return encode_str


print(duplicate_encode(word))
