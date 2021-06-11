# Создать список, содержащий цены на товары (10 – 20 товаров), например:
# [57.8, 46.51, 97, ...]

# A. Вывести на экран эти цены через запятую в одну строку,
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

# B. Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же).

# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.

# D. Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

from random import random

prices = [round(random()*100, 2) for _ in range(21)]

# Задание A:

for price in prices:
    str_price = str(price).split('.')
    print(f'{str_price[0]} руб {int(str_price[1]):0>2d} коп', end=', ')

print('\nid cписка prices: ', (id(prices)))

# Задание B:

print()

prices.sort()

for price in prices:
    str_price = str(price).split('.')
    print(f'{str_price[0]} руб {int(str_price[1]):0>2d} коп', end=', ')

print('\nid отсортированного cписка prices: ', (id(prices)))

# Задание C:

print()

new_prices = sorted(prices.copy(), reverse=True)

for price in new_prices:
    str_price = str(price).split('.')
    print(f'{str_price[0]} руб {int(str_price[1]):0>2d} коп', end=', ')

print('\nid отсортированного cписка new_prices: ', (id(new_prices)))

# Задание D:

print()

for price in new_prices[:5]:
    str_price = str(price).split('.')
    print(f'{str_price[0]} руб {int(str_price[1]):0>2d} коп', end=', ')

print()

for price in sorted(new_prices[:5]):
    str_price = str(price).split('.')
    print(f'{str_price[0]} руб {int(str_price[1]):0>2d} коп', end=', ')

