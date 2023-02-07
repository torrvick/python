# Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# Команда:[Всегоигр Побед Ничьих Поражений Всегоочков]
#               0      1    2       3           4

games_count = int(input("Введите количество игр: "))
results = {}
for i in range(games_count):
    game = input("Введите результаты игры: ").split(";")

    if int(game[1]) > int(game[3]):
        winner = game[0]
    elif int(game[1]) < int(game[3]):
        winner = game[2]
    else:
        winner = ""

    for i in [0, 2]:
        if game[i] not in results.keys():
            results.update({game[i]: [0, 0, 0, 0, 0]})
        results.get(game[i])[0] += 1
        if game[i] == winner:
            results.get(game[i])[1] += 1
        if game[i] != winner:
            results.get(game[i])[3] += 1
        if winner == "":
            results.get(game[i])[2] += 1

for team in results.keys():
    results.get(team)[4] = results.get(team)[1] * 3

for team in results.keys():
    print(f"{team}:", end = " ")
    for i in range(5):
        print(results.get(team)[i], end = " ")
    print()
