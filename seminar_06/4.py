# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры), 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и только 
# один раз переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.
from random import randint
from random import choice

while True:
        sp_size = list(map(int,input("Введите размер массива через пробел (строки столбцы): ").split()))
        sp_rows = sp_size[0]
        sp_cols = sp_size[1]
        if (sp_rows*sp_cols)%2 == 0:
            break
        else:
            print("Количество элементов в массиве должно быть четным. Попробуйте еще раз")
        
sp = [[randint(0,99) for _ in range(sp_cols)] for _ in range(sp_rows)]
# for el in sp:
#     print(" ".join(list(map(str,el))))
def print_array(array):
    for row in array:
        for el in row:
            print("%3d" %(el), end = " ")
        print()

print()       
print("Исходный массив:")
print_array(sp)
print()

def gen_coord_table(array):
    coord_table = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            coord_table.append([i,j])
    return coord_table

def shake_array(array):
    coords = gen_coord_table(array)
    while coords:
        i, j = choice(coords)
        coords.remove([i,j])
        i2, j2 = choice(coords)
        coords.remove([i2, j2])
        array[i][j], array[i2][j2] = array[i2][j2], array[i][j]
    return(array)

print("Перемешанный массив: ")
print_array(shake_array(sp))
print()
