# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

seq_start = int(input("Введите первый элемент прогрессии: "))
seq_step = int(input("Введите шаг прогрессии: "))
seq_size = int(input("Введите количество элементов: "))
seq = []

for el in range(seq_size):
    seq.append(seq_start+el*seq_step)

print(seq)
