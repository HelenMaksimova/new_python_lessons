# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

# * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

def odd_nums(num):
    for odd_num in range(1, num + 1, 2):
        yield odd_num


num_n = int(input('Введите число: '))

odd_nums_gen = (number for number in range(1, num_n + 1, 2))  # задание со *

odd_nums_func = odd_nums(num_n)

while True:
    try:
        print('Функция-генератор:', next(odd_nums_func))
        print('Генераторное выражение:', next(odd_nums_gen), '\n')
    except StopIteration:
        print('Генераторы исчерпаны')
        break
