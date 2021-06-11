# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates


import os
import shutil


def create_templates(root_folder):
    path_to_copy = set()
    for root, dirs, files in os.walk(root_folder):
        if root.endswith('templates'):
            path_to_copy.add(root)
    name_dir = os.path.join(root_folder, 'templates')
    print(path_to_copy)
    if name_dir in path_to_copy:
        path_to_copy.remove(name_dir)
    if not os.path.exists(name_dir):
        os.makedirs(name_dir)
    for path in list(path_to_copy):
        shutil.copytree(path, name_dir, dirs_exist_ok=True)


root_path = os.path.join(os.getcwd(), 'my_project')

create_templates(root_path)
