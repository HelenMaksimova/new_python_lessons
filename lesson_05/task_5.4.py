# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.
from random import randint

num_lst = [randint(1, 100) for _ in range(20)]

print(num_lst)

result = (num_lst[idx] for idx in range(1, len(num_lst)) if num_lst[idx] > num_lst[idx - 1])

print(*result, sep=', ')

