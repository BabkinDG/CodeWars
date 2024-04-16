input_str = ' Hello there thanks for trying my Kata'  # --> "#HelloThereThanksForTryingMyKata"


def generate_hashtag(input_str):
    hashtag = '#'
    for i in input_str.split():
        hashtag += i.capitalize()
    if input_str == '' or len(hashtag) > 140:
        return False
    return hashtag


print(generate_hashtag(input_str))
