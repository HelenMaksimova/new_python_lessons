# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
# логов web-сервера nginx_logs.txt
# — получить список кортежей вида: (<remote_addr>, <request_type>,
# <requested_resource>).
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ
# компьютера.
# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.

with open('nginx_logs.txt') as log_file:
    data_list = []
    for line in log_file:
        item = line.split()
        data_list.append((item[0], item[5].strip('"'), item[6]))

print('Первые 20 кортежей:')
print(*data_list[:20], sep='\n')

# *

ip_list = list({element[0] for element in data_list})

ip_dict = dict().fromkeys(ip_list, 0)

for el in data_list:
    ip_dict[el[0]] += 1

result = max(ip_list, key=lambda x: ip_dict[x])

print(f'\nС ip-адреса {result} было направлено запросов: {ip_dict[result]}')
