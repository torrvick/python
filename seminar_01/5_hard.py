from decimal import Decimal

number = Decimal(input("Введите число: "))
if number < 0: number = -number
while number != int(number): number *= 10

summ = 0
while number != 0:
    summ += number % 10
    number //= 10

print(f"Сумма цифр этого числа равна {int(summ)}")