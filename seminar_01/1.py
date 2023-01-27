# Задача 2: Найдите сумму цифр трехзначного числа

number = 0
while number <100 or number > 999:
    number = int(input("Введите трехзначное число: "))

summ = 0
while number != 0:
    summ += number % 10
    number //= 10

print(f"Сумма цифр этого числа равна {summ}")
