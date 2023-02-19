import json 
import random

def load_base():
    with open("base.json", "r", encoding="utf-8") as base:
        global music 
        music = json.load(base) 

def save_base():
    with open("base.json", "w", encoding="utf-8") as base:
        base.write(json.dumps(music,ensure_ascii=False))

try:
    load_base()
except:
    print()
    print("--- Ошибка загрузки файла данных ---")
    exit()

def show_bands():
    for band in music:
        print(band["Name"])

def show_styles():
    styles = []
    for band in music:
        styles.append(band["Style"])
    print(("\n").join(set(styles)))

def show_countries():
    countries = []
    for band in music:
        countries.append(band["Country"])
    print(("\n").join(set(countries)))

def select_songs(band_n = "", country_n = "", style_n = "", rnd = ""):
    print("Твой плейлист:")

    def gen_playlist_by(filt,filt_value):
        playlist = []
        for band in music:
            if band[filt] == filt_value:
                for song in band["Songs"]:
                    playlist.append([band["Name"],song])
        return(playlist)
    
    def print_playlist(playlist):
        for song in playlist:
            print(f"{song[0]} - {song[1]}")

    if band_n != "":
        pl = gen_playlist_by("Name", band_n)
        print_playlist(pl)
        
    if country_n != "":
        pl = gen_playlist_by("Country", country_n)
        print_playlist(pl)

    if style_n != "":
        pl = gen_playlist_by("Style", style_n)
        print_playlist(pl)
        
    if rnd != "":
        rnd = int(rnd)
        playlist = []
        for band in music:
            for song in band["Songs"]:
                playlist.append([band["Name"],song])
        random.shuffle(playlist)
        playlist = playlist[:rnd]
        print_playlist(playlist)
        
    input("Нажми Enter для возвращения в меню выбора")


main_commands_available = ["/start","/stop", "/help", "/bands", "/countries", "/styles", "/play", "/add", "/show_base"]
play_commands_available = ["/name", "/style", "/country", "/random", "/exit"]
print()
print("Привет! Я - музыкальный бот")
while True:
    command = input("|Главное меню| / Введи команду: ")
    if command not in main_commands_available:
        print("Я пока не знаю такой команды. Для списка доступных набери /help")
    if command == "/help":
        print("Вот команды, которые я знаю:")
        print(("\n").join(main_commands_available))
    if command == "/start":
        print("Бот уже запущен")
    if command == "/stop":
        print("Всего хорошего. Возвращайся ;)")
        break
    if command == "/bands":
        print("В моей базе есть такие группы:")
        show_bands()
    if command == "/countries":
        print("В моей базе есть группы из этих стран:")
        show_countries()
    if command == "/styles":
        print("В моей базе есть группы таких стилей:")
        show_styles()
    if command == "/play":
        while True:
            print()
            print("По какому критерию ты хочешь выбрать?")
            print("/name - по названию")
            print("/style - по стилю")
            print("/country - по стране")
            print("/random х - случайно выбрать x песен")
            print("/exit - выход из меню проигрывания")
            print()
            command = input("|Меню проигрывания| / Введи команду: ")
            if command.split()[0] not in play_commands_available:
                print("Неверная команда")
            if command == "/exit":
                break
            if command == "/name":
                show_bands()
                band = input("Введите название группы: ")
                select_songs(band_n = band)
            if command == "/style":
                show_styles()
                style = input("Введите название стиля: ")
                select_songs(style_n = style)
            if command == "/country":
                show_countries()
                country = input("Введите страну: ")
                select_songs(country_n = country)
            if command.split()[0] == "/random":
                select_songs(rnd = command.split()[1])
    if command == "/add":
        print("Добавление новой группы")
        name = input("Введите название группы: ")
        style = input("В каком стиле они играют? ")
        country = input("Откуда эти ребята? ")
        print("Добавьте их песни. Для окончания ввода введите пустую строку")
        songs = []
        while True:
            song = input()
            if song == "": break
            else:
                songs.append(song)
        music.append({"Name": name, "Style": style, "Country": country, "Songs": songs})
        try:
            save_base()
            print("Новая группа добавлена")
        except:
            print("Ошибка записи")
    


    if command == "/show_base":
        print(json.dumps(music, indent=4))
