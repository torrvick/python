# Задача 24: Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

from random import randint

n = int(input("Введите количество кустов: "))
gard = [randint(1,5) for _ in range(n)]
print(gard)
summ_near = 0

for i in range(n):
    gard.insert(0,gard.pop())
    if sum(gard[:3]) > summ_near: summ_near = sum(gard[:3])
print(f"Масксимально количество ягод: {summ_near}")