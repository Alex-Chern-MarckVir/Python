import random


def get_jokes(n=1, flag=True):
    """
    Функция get_jokes() возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков
    :param n: количество шуток
    :param flag: флаг, разрешающий или запрещающий повторы слов в шутках
    :return: строка с шутками
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = ""
    for i in range(n):
        if len(nouns) == 0:
            return result

        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)

        if not flag:
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
        result = result + " " + noun + " " + adverb + " " + adjective + "\n"
    return result


print(get_jokes(5))
print()
print(get_jokes(40, False))
