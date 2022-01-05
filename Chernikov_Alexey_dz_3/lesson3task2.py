def num_translate_adv(number):
    """
    ENG-RU translator for numbers
    :param number: input ENG number in string form
    :return: number: output RU number in string form
    """

    numbers = {
        "ноль": "zero", "Ноль": "Zero",  "zero": "ноль", "Zero": "Zero",
        "один": "one", "Один": "One",  "one": "один", "OneОдин": "Один",
        "два": "two", "Два": "Two", "two": "два", "Two": "Два",
        "три": "three", "Три": "Three",   "three": "три", "Three": "Three",
        "четыре": "four", "Четыре": "Four",  "four": "четыре", "Four": "Четыре",
        "пять": "five", "Пять": "Five",  "five": "пять", "Five": "Пять",
        "шесть": "six", "Шесть": "Six",   "six": "шесть", "Six": "Шесть",
        "семь": "seven", "Семь": "Seven",  "seven": "семь", "Seven": "Семь",
        "восемь": "eight", "Восемь": "Eight",  "eight": "восемь", "Eight": "Восемь",
        "девять": "nine", "Девять": "Nine",  "nine": "девять", "Nine": "Девять",
        "десять": "ten", "Десять": "Ten",   "ten": "десять", "Ten": "Десять"
    }
    if number in numbers:
        return numbers[number]
    return None
