# Задача HARD необязательная. Имеется список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

from random import randint
n = int(input("Введите количество элементов: "))
sp = [randint(0, 10) for _ in range(n)]
# sp = [1, 5, 3, 4, 1, 7, 8, 15, 1]
print(sp)

interval, interval_temp = [], []

for i in range(min(sp), max(sp)+1):
    if i in sp:
        interval.append(i)
    else:
        if len(interval) >= len(interval_temp):
            interval_temp = interval
        interval = []
if len(interval_temp) > len(interval):
    interval = interval_temp
sp_res = [min(interval), max(interval)]

if sp_res[1] - sp_res[0] == 0:
    print("Последовательности не найдены")
else:
    print(f"Границы максимальной последовательности: {sp_res}")