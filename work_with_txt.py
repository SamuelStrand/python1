
# with open('C:/Project/Github_Projects/python1/src/file.txt') as file:  # alias - псевдоним - Абсолютный путь
# with open('src/file.txt') as file:  # alias - псевдоним - Относительный путь к файлу в папке в текущей директории
# with open('file.txt') as file:  # alias - псевдоним - Относительный путь к файлу в текущей папке
with open('src/dist/file.txt', "r", encoding='utf-8') as file:  # alias - псевдоним - Относительный путь к файлу в текущей папке
    # text = file.readline()  # читает выбранную строку
    # print(text)
    old_list = file.readlines()  # читает все строки - выдаёт нам массив(list - список)
    # print(text)

    print("Hello\nWorld!")

    print(old_list)
    new_list = []  # чистый список
    for line in old_list:
        if len(line) > 1:
            new_list.append(line[0:-1:1])  # добавление нового объекта в "list"(список) в конец
            # print(line[0:-1:1])
    print(new_list)
    # text1 = text[начало:конец:шаг]

    # text = "Pellentesque"
    # text1 = text[0::2]  # Обрезает строку в обычной последовательно от 3 символа и до конца
    # print(text1)
    #
    # text = "Pellentesque"
    # text1 = text[3:10:-1]  # Обрезает строку в обычной последовательно от 3 символа и до 10 символа
    #
    # text = "Pellentesque"
    # text1 = text[1:-3:1]  # Обрезает строку в обратной последовательно


    # var_list = ["Almaty", "Nur-Sultan", "Taraz", "Ekibastuz", "Almaty", "Nur-Sultan", "Taraz", "Ekibastuz"]
    # # var_list1 = var_list[-3:-1:1]
    # var_list1 = var_list[0:7:1]
    # print(var_list1)

    # for line in text:
    #
    #     print(line)

    # text = file.write()
    # text = file.read()

# тут файл уже будет закрыт


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


# with open('src/dist/new_file.txt', "a", encoding='utf-8') as file:
#     var_list = ["Almaty", "Nur-Sultan", "Taraz", "Ekibastuz", "Almaty", "Nur-Sultan", "Taraz", "Ekibastuz"]
#     for city in var_list:
#         file.write(f"{city} \n")
#     # file.writelines(var_list)





text = "Ekibastuz Ekibastuz Ekibastuz"
index = 0
for char in text:
    index = index + 1
    new = 

# newlist = [x for x in fruits if "a" in x]
#
# print(newlist)