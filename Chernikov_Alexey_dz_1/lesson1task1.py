# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input(" duration = "))

if 0 < duration >= 60:
    minutes = duration // 60
    seconds = duration % 60
    if 0 < minutes >= 60:
        h = minutes // 60
        minutes = minutes % 60
        if 0 < h >= 60:
            days = h // 24
            h = h % 24
            print(days)
            print(h)
        print(minutes)
    print(seconds)
