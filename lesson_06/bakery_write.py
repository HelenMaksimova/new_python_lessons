# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
# скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
# записанных данных. При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
#     - просто запуск скрипта — выводить все записи;
#     - запуск скрипта с одним параметром-числом — выводить все записи с номера, равного
#     этому числу, до конца;
#     - запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
# первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
#
# *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
# обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер
# записи, которой не существует.

# Скрипт записи данных:

from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as file_bakery:
    if len(argv) > 1:
        for value in argv[1:]:
            value.replace(',', '.')
            if '.' not in value:
                value += '.00'
            base, penny = value.split('.')
            file_bakery.write(f'{int(base):07d},{int(penny):02d}\n')
        print('Запись произведена успешно!')
    else:
        print('Необходимо передать значение суммы (сумм) продаж!')

