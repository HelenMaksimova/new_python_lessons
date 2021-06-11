# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

import random


def get_jokes(number=1, repeat=True) -> list:
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if repeat:
        jokes = [[random.choice(nouns), random.choice(adverbs), random.choice(adjectives)] for _ in range(number)]
        result = [' '.join(joke) for joke in jokes]
    else:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        jokes = zip(nouns[:number], adverbs[:number], adjectives[:number])
        result = [' '.join(joke) for joke in jokes]
    return result


print(get_jokes())

print(get_jokes(7))

print(get_jokes(number=7, repeat=False))
