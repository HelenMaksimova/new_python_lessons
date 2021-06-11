# Написать скрипт, создающий из config.yaml стартер для проекта со следующей
# структурой:
# |--my_project
#     |--settings
#         | |--__init__.py
#         | |--dev.py
#         | |--prod.py
#     |--mainapp
#         | |--__init__.py
#         | |--models.py
#         | |--views.py
#         | |--templates
#             | |--mainapp
#                 | |--base.html
#                 | |--index.html
#     |--authapp
#         | |--__init__.py
#         | |--models.py
#         | |--views.py
#         | |--templates
#             | |--authapp
#                 | |--base.html
#                 | |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
# текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
# ситуации, библиотеки использовать нельзя.

import os


def create_folder(item, last_dir):
    if item[0].endswith(':'):
        name_dir = os.path.join(os.getcwd(), item[0].rstrip(':'))
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        last_dir = name_dir
    else:
        name_file = os.path.join(os.getcwd(), item[0])
        if not os.path.exists(name_file):
            with open(name_file, 'w') as f:
                pass
    return last_dir


def create_tree(data_list):
    position = data_list[0][1]
    last_dir = os.getcwd()
    last_position = position
    for item in data_list:
        if item[1] > position:
            os.chdir(last_dir)
            last_position += 1
            last_dir = create_folder(item, last_dir)
        elif item[1] < position:
            steps = last_position - item[1]
            last_position = last_position - item[1]
            for _ in range(steps):
                os.chdir('..')
            last_dir = create_folder(item, last_dir)
        else:
            last_dir = create_folder(item, last_dir)
        position = item[1]


if __name__ == '__main__':

    with open('config.yaml') as file:
        data = []
        for line in file:
            line_list = line.rstrip('\n').split('    ')
            data.append((line_list[-1].lstrip('- '), len(line_list) - 1))

    create_tree(data)
