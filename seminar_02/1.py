# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
from random import randint

n = int(input("Введите количество монет: "))
coins = []
for i in range(n):
    coins.append(randint(0, 1))
print(coins)
summ = 0
for i in range(n):
    summ += coins[i]

if summ > n/2:
    print(f"Достаточно перевернуть {n - summ} монет")
else:
    print(f"Достаточно перевернуть {summ} монет")