# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.

import json

with open('users.csv', encoding='utf-8') as users_file:
    users_list = [' '.join(line.strip().split(',')) for line in users_file]

with open('hobby.csv', encoding='utf-8') as hobby_file:
    hobby_list = [line.strip().split(',') for line in hobby_file]


if len(users_list) < len(hobby_list):
    raise ValueError('Несоответствие количества строк в файлах!')

result_dict = dict.fromkeys(users_list)

result_dict.update(zip(users_list, hobby_list))

with open('users_hobby.json', 'w') as json_file:
    json.dump(result_dict, json_file)

with open('users_hobby.json') as json_file:
    users_hobby_dict = json.load(json_file)

print(users_hobby_dict, type(users_hobby_dict))
