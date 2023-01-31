# Задача 3. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . 
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные, 
# проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени отработала программа. 
# В конце вывести результат проверки истинности этого утверждения.

from random import randint
import time

attempt_count = 100
correct_count = 0
start_time = 0
end_time = 0
start_time = time.time()
for attempt in range(attempt_count):
    pred_list = []
    for i in range(randint(5, 25)):
        pred_list.append(randint(0, 1))
    #print(pred_list)
    or_construct = pred_list[0]
    and_construct = not pred_list[0]
    for i in range(1, len(pred_list)):
        or_construct = or_construct or pred_list[i]
        and_construct = and_construct and not pred_list[i]
    or_construct = not or_construct
    if or_construct == and_construct:
        correct_count += 1
end_time = time.time()
if correct_count == attempt_count:
    print("Утверждение истинно")
print(f"Проверка заняла {round((end_time - start_time)*1000,3)} миллисекунд")
