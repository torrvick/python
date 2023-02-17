poem = input("Винни, жги: ").split()

vowel_count = [sum(1 for letter in phrase if letter in "уеыаоэяиюё") for phrase in poem]
if len(set(vowel_count)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")



