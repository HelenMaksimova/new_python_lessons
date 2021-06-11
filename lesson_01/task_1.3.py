# Реализовать склонение слова процент для чисел до 20. Вывести все склонения для проверки.

from random import randint


# Простая реализация чётко по заданию:

for number in range(21):

    if number == 1:
        result_str = 'процент'
    elif 1 < number <= 4:
        result_str = 'процента'
    else:
        result_str = 'процентов'

    print(f'{number} {result_str}')

print(f'\n{" * " * 10}\n')


# Реализация для любых чилел:


def percent(num: int) -> str:
    str_num = str(num)
    if len(str_num) >= 2:
        if str_num[-2] == '1':
            result = 'процентов'
        else:
            if str_num[-1] == '1':
                result = 'процент'
            elif str_num[-1] in ('2', '3', '4'):
                result = 'процента'
            else:
                result = 'процентов'
    else:
        if str_num[-1] == '1':
            result = 'процент'
        elif str_num[-1] in ('2', '3', '4'):
            result = 'процента'
        else:
            result = 'процентов'
    return f'{num} {result}'


test_gen = (randint(0, 1000) for _ in range(21))

for item in test_gen:
    print(percent(item))
