# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
def compress(data):
    str_comp = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            if count == 1:
                str_comp += data[i-1]
            elif count > 1:
                str_comp += str(count)+data[i-1]
                count = 1
        if i == len(data) - 1:
            if count == 1:
                str_comp += data[i]
            elif count > 1:
                str_comp += str(count) + data[i]
    return str_comp


def decompress(data):
    str_decomp = ""
    count = ""
    for i in range(len(data)):
        if data[i].isdigit():
            count += data[i]
        else:
            if data[i-1].isdigit():
                str_decomp += data[i] * int(count)
                count = ""
            else:
                str_decomp += data[i]
    return str_decomp


origin_str = input("Введите строку для сжатия: ")
comp_string = compress(origin_str)
print(f"Результат сжатия: {comp_string}")
print(f"Результат восстановления:  {decompress(comp_string)}")
if origin_str == decompress(comp_string):
    print("Исходная и восстановленная строки идентичны")