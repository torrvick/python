# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. Напишите программу", "которая вычисляет стоимость введенного пользователем слова.

costs = {1:["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
         2:["D", "G", "Д", "К", "Л", "М", "П", "У"],
         3:["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"],
         4:["F", "H", "V", "W", "Y", "Й", "Ы"],
         5:["K", "Ж", "З", "Х", "Ц", "Ч"],
         8:["J", "X", "Ш", "Э", "Ю"],
         9:["Q", "Z", "Ф", "Щ", "Ъ"]}
# print(costs.keys())
cost = 0
for l in ("ноутбук"):
    for i in costs.keys():
        if l.upper() in costs[i]:
            cost += i
print(cost)
