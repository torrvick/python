# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. 

from random import randint
n = int(input("Введите количество элементов: "))
sp = [randint(0, 10) for _ in range(n)]

print(sp)
x = int(input("Введите число: "))
number_found = None
if x > max(sp):
    number_found = max(sp)
elif x < min(sp):
    number_found = min(sp)
elif x in sp:
    print(f"Само число {x} уже присутствует в массиве")
    exit()
else:
    sp.append(x)
    sp.sort()
    for i in range(len(sp)):
        if sp[i] == x:
            if (sp[i+1]+sp[i-1])/2 > sp[i]:
                number_found = sp[i-1]
            elif (sp[i+1]+sp[i-1])/2 < sp[i]:
                number_found = sp[i+1]
            else:
                print(f"Ближайшими к числу {x} являются числа {sp[i-1]} и {sp[i+1]}")
                exit()  
print(f"Ближайшим к числу {x} является число {number_found}")