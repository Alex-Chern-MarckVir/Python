# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# A) Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек
# (должно быть 07 коп или 00 коп).
# B) Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).
# C) Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# D) Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
lst = [57.8, 46.51, 97, 132.5, 265.9, 66.16, 46.1, 10.42, 0.06, 0.49]
print(lst)
print(" ", id(lst))

# A
print("A")
for i in lst:
    print(f'<{int(i//1)} руб {int((i * 100) % 100):02d} коп>', end=" ")
print("\n")

# B
lst.sort()
print("B - sort <")
for i in lst:
    print(f'<{int(i//1)} руб {int((i * 100) % 100):02d} коп>', end=" ")
print("\n", id(lst), "\n")

# C
lst2 = lst[::-1]
print("C - new list sort >")
for i in lst[::-1]:
    print(f'<{int(i//1)} руб {int((i * 100) % 100):02d} коп>', end=" ")
print("\n", id(lst2), "\n")

# D
print("D - sort 5 <")
for i in lst[-5:]:
    print(f'<{int(i//1)} руб {int((i * 100) % 100):02d} коп>', end=" ")
