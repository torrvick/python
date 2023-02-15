# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint

interval = list(map(int,input("Введите диапазон для поиска через пробел: ").split()))
interval_min = interval[0]
interval_max = interval[1]

sp = [randint(-10,10) for _ in range(15)]
sp_ind = []

for i in range(0,len(sp)):
    if interval_min < sp[i] < interval_max:
        sp_ind.append(i)

print(sp)
print(sp_ind)
