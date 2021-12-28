# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_list))
print(my_list)


def zero_plus_num(lst: list):
    """
    complements numbers up to two digits with zero

    :param lst: input list
    :return: lst: result list
    """
    for i, j in enumerate(lst):
        if ord("0") <= ord(j[0]) <= ord("9"):
            if len(j) < 2:
                lst[i] = "0" + lst[i]

        num = j[1:]
        if j[0] == "+" or j[0] == "-":
            if num.isdigit():
                if int(num) < 10:
                    lst[i] = j[0] + "0" + num
    return lst


def sep_num_sep(lst: list, sep='"'):
    """
        separating numbers with marks in list
        ...[sep="], [numb], [sep="]...

    :param lst: input list
    :param sep: separator
    :return: lst: a list with separate numbers
    """
    lst_idx = []
    for i in lst:
        num = i[1:]
        if i.isdigit() or num.isdigit():
            idx = lst.index(i)
            lst_idx.append(idx)
    lst_idx = lst_idx[::-1]
    for i in lst_idx:
        lst.insert(i + 1, sep)
        lst.insert(i, sep)
    return lst


zero_plus_num(my_list)
sep_num_sep(my_list)
i = 0
result = ""
while i < len(my_list):
    if my_list[i] == '"':
        result = result + ' ' + my_list[i] + my_list[i + 1] + my_list[i + 2]
        i = i + 3
    else:
        result = result + ' ' + my_list[i]
        i = i + 1

print(id(my_list))
print(my_list)
print(result)
