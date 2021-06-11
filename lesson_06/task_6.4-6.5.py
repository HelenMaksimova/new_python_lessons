# * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Также реализовать парсинг данных из файлов - получить отдельно
# фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в
# какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор
# типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться
# данные, полученные в результате парсинга.
#
# ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать путь к обоим исходным файлам и путь к выходному файлу со словарём. Проверить
# работу скрипта для случая, когда все файлы находятся в разных папках.

import json
from sys import argv
import os

PATH_DICT = {
    'FILE_USERS_PATH': os.path.join(os.path.curdir, 'users.csv'),
    'FILE_HOBBY_PATH': os.path.join(os.path.curdir, 'hobby.csv'),
    'FILE_RESULT_PATH': os.path.join(os.path.curdir, 'users_hobby.json')
}

PATH_DICT.update(zip(('FILE_USERS_PATH', 'FILE_HOBBY_PATH', 'FILE_RESULT_PATH'), argv[1:]))

with open(PATH_DICT['FILE_USERS_PATH'], encoding='utf-8') as users_file:
    users_list = [line.strip().split(',') for line in users_file]

with open(PATH_DICT['FILE_HOBBY_PATH'], encoding='utf-8') as hobby_file:
    for item in users_list:
        line = hobby_file.readline().strip()
        item.append(line.split(',')) if line else item.append(None)

    if hobby_file.readline().strip():
        raise ValueError('Несоответствие количества строк в файлах!')

result_dict = {' '.join(item[:3]): dict(zip(('Фамилия', 'Имя', 'Отчество', 'Хобби'), item)) for item in users_list}

with open(PATH_DICT['FILE_RESULT_PATH'], 'w') as json_file:
    json.dump(result_dict, json_file)

with open(PATH_DICT['FILE_RESULT_PATH']) as json_file:
    users_hobby_dict = json.load(json_file)

for key, value in users_hobby_dict.items():
    print(f'{key}: {value}')
