# Задача HARD SORT необязательная.
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
# Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

from random import randint

sp_size = list(map(int,input("Введите размер массива через пробел (строки столбцы): ").split()))
sp_rows = sp_size[0]
sp_cols = sp_size[1]
sp = [[randint(0,10) for _ in range(sp_cols)] for _ in range(sp_rows)]
# for el in sp:
#     print(" ".join(list(map(str,el))))
def print_array(array):
    for row in array:
        for el in row:
            print("%3d" %(el), end = " ")
        print()
        
print("Исходный массив:")
print_array(sp)
print()

def sort_array(array):
    array_temp = []
    rows = len(array)
    cols = len(array[0])
    for row in array:
        for el in row:
            array_temp.append(el)
    array_temp.sort()

    index_temp = 0
    for i in range(rows):
        for j in range(cols):
            array[i][j] = array_temp[index_temp]
            index_temp += 1
    return array

print("Отсортированный массив:")
print_array(sort_array(sp))