# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

a = int(input("Введите A: "))
b = int(input("Введите B: "))

def rec_pow(a, b):
    if b == 1:
        return a
    else:
        return a*rec_pow(a,b-1)
    
print(f"{a} в степени {b} равно {rec_pow(a,b)}")
