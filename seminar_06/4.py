# задача 2 HARD необязательная
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры), 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и только 
# один раз переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.
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

def shake_array(array):
    array_temp = []
    for row in array:
        for el in row:
            array_temp.append(str(el))

    print(array_temp)
    count_cicles = 0
    count_mix = 0
    for i in range(len(array_temp)):
        el_ind = randint(0,len(array_temp)-1)
        if array_temp[el_ind].find("_") == -1:
            el_ind2 = randint(0,len(array_temp)-1)
            if array_temp[el_ind2].find("_") == -1:
                array_temp[el_ind],array_temp[el_ind2] = "_" + array_temp[el_ind2], "_" + array_temp[el_ind]
                count_mix += 1
        count_cicles += 1
    print(array_temp)
    print(count_cicles)
    print(count_mix)
shake_array(sp)