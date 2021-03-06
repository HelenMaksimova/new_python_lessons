# Дан список, содержащий искаженные данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду?
# Можно ли при этом не создавать новый список?

data_list = ['инженер-конструктор Игорь',
             'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй',
             'директор аэлита']

for item in data_list:
    name = item.split()[-1].lower().title()
    print(f'Привет, {name}!')
