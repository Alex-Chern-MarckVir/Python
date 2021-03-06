# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент 2 процента 3 процента 4 процента 5 процентов 6 процентов ... 100 процентов

word = "Процент"
word_end = ["", "а", "ов"]

for i in range(101):
    i = str(i)

    if i != "11" and i[-1] == "1":  # Число 11 и все числа заканчивающиеся на единицу
        print(i, word + word_end[0])  # Процент

    if (i[-1] == "2" or i[-1] == "3" or i[-1] == "4") \
            and i[0] != "1":  # Все числа заканчивающиеся на 2 <или> 3 <или> 4 <и> не начинающиеся на 1
        print(i, word + word_end[1], end=" ")  # Процент + а

    elif (i[0] == "1" and i != "1")\
            or i[-1] == "0" or i[-1] == "5" \
            or i[-1] == "6" or i[-1] == "7" \
            or i[-1] == "8" or i[-1] == "9":
        print(i, word + word_end[2], end=" ")  # Процент + ов
