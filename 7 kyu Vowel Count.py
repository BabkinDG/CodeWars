sentence = 'abracadabra'
def get_count(sentence):
    vowels = 'aeiou'
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count

print(get_count(sentence))