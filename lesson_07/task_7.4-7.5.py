# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0)
#
# *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>,
# [<files_extensions_list>])

import os


def size_file(size, border, step):
    if size < border:
        return border
    return size_file(size, border * step, step)


def folder_statistic(folder):
    quantity_dict = dict()
    f_extensions = dict()
    for root, dirs, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            size = os.stat(path).st_size
            extension = path.rsplit('.', 1)[-1]
            border = size_file(size, 10, 10)
            if border not in quantity_dict:
                quantity_dict[border] = 0
                f_extensions[border] = set()
            quantity_dict[border] += 1
            f_extensions[border].add(extension)
    result_dict = {key: (quantity_dict[key], list(f_extensions[key])) for key in quantity_dict}

    return result_dict


user_path = input('Введите адрес папки:')
print(folder_statistic(user_path))
