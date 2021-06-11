# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#     |--settings
#     |--mainapp
#     |--adminapp
#     |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как
# лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
# папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
# данные о вложенных папках и файлах (добавлять детали)?

import os


def create_folder_tree(folders: dict, root_dir: str):
    name_dir = root_dir
    for folder in folders:
        name_dir = os.path.join(name_dir, folder)
        if folders[folder]:
            create_folder_tree(folders[folder], name_dir)
        if not os.path.exists(name_dir):
            os.makedirs(name_dir)
        name_dir = root_dir


root_name = 'my_project'

dir_names = {
    'settings': dict(),
    'mainapp': dict(),
    'adminapp': dict(),
    'authapp': dict()
}

cur_dir_path = os.path.curdir

root = os.path.join(cur_dir_path, root_name)

create_folder_tree(dir_names, root)






