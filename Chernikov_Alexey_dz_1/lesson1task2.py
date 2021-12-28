# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#     Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#     Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

integer_list = []


def list3(lst: list):
    """ list3 заполняет список кубами нечетных чисел и выводит его """
    for i in range(1, 1000, 2):
        lst.append(i**3)
    print(lst)


def in_sum_if_division7(lst: list):
    """ """
    all_sum = 0
    for i, value in enumerate(lst):
        int_sum = 0
        while value != 0:
            int_sum += value % 10
            value //= 10
        if int_sum % 7 == 0:
            all_sum += lst[i]
            print(i, ":", lst[i], ",", end=" ")
    print("\nСумма =", all_sum)


def in_list_plus_17(lst: list):
    """ in_list_plus_17 прибавляет 17 к каждому элементу списка """
    for i in range(len(lst)):
        lst[i] = lst[i] + 17
    print(lst)
    pass


list3(integer_list)
in_sum_if_division7(integer_list)
in_list_plus_17(integer_list)
in_sum_if_division7(integer_list)
