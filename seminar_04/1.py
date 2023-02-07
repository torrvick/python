# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

def spgenerate(size, min=0, max=10):
    return [randint(min, max) for _ in range(size)]

sp1 = spgenerate(int(input("Введите размер первого массива: ")))
sp2 = spgenerate(int(input("Введите размер второго массива: ")))
print(sp1)
print(sp2)

sp3 = [elem for elem in set(sp1) if elem in set(sp2)]
print(sp3)


