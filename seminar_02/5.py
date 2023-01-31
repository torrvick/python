# Задача 4. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input("Введите число: "))
if n == 0:
    print("[0]")
else:
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, n+1):
        fib.append(fib[i-2]+fib[i-1])

    fib_temp =[]
    for i in range(1,len(fib)):
        fib_temp.append(-fib[-i])

    fib = fib_temp + fib
    print(fib)

