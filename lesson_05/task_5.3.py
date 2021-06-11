# Есть два списка:
#
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей',
#     'Дмитрий', 'Борис', 'Елена'
# ]
#
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
#
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде:
# (<tutor>, None),
# например:
# ('Станислав', None)
#
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б']


def pupils_gen(tutors_lst, klasses_lst):
    if len(tutors_lst) > len(klasses_lst):
        klasses_lst.extend([None] * (len(tutors_lst) - len(klasses_lst)))
    for item in zip(tutors_lst, klasses_lst):
        yield item


pupils_generator = pupils_gen(tutors, klasses)

print('Класс объекта pupils_generator: ', type(pupils_generator))

print('\nПолучены следующие элементы:')
print(*pupils_generator, sep='\n')
