# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].

from random import randint
n = int(input("Введите количество элементов: "))
sp = [randint(0,10) for _ in range(n)]
print(sp)

count = 0
x = int(input("Какое число ищем? "))
for elem in sp: 
    if elem == x: 
        count +=1
print(f"Число {x} встречается {count} раз")