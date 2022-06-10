import requests
import json

var_dict1 = dict(Age=24, Name='Ally')  # создание словаря
print(var_dict1)

var_dict2 = {"Age": 24, "Name": 'Ally'}  # создание словаря
print(var_dict2)

var_dict3 = {}  # создание словаря
var_dict3["Age"] = 24
var_dict3["Name"] = 'Ally'
print(var_dict3)

var_dict4 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": {
        "streetAddress": "Московское ш., 101, кв.101",
        "city": "Ленинград",
        "postalCode": 101101
    },
    "phoneNumbers": [
        "812 123-1234",
        "916 123-4567"
    ]
}
print(type(var_dict4))

url = "https://api.instantwebtools.net/v1/airlines/1"
response = requests.get(url) # Возвращает объект response
# У response объекта есть статус код (ключ и значение)
if response.status_code == 200:
    print("Ok")
else:
    print("False")
json_data = response.content.decode() # Мы возвращаем результат функции (декодированные данные из байтов в строку)
airlines = json.loads(json_data) #
print(type(airlines))
print(json_data)

with open('data.json', 'w') as file:
    json.dump(json_data, file)
    # json.dumps()

# with open('src/dist/new_file.json', 'r') as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()