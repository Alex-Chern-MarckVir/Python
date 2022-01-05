def num_translate(eng_number):
    """
    ENG-RU translator for numbers
    :param eng_number: input ENG number in string form
    :return: ru_number: output RU number in string form
    """
    ru_numbers = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять"]
    eng_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    for i, j in enumerate(eng_numbers):
        if j == eng_number:
            return ru_numbers[i]
    return None
