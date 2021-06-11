# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке

from random import randint

num_lst = [randint(1, 10) for _ in range(15)]

uniq_nums = set()
tmp = set()
for item in num_lst:
    if item not in tmp:
        uniq_nums.add(item)
    else:
        uniq_nums.discard(item)
    tmp.add(item)

result = [element for element in num_lst if element in uniq_nums]

print(num_lst)
print(result)
