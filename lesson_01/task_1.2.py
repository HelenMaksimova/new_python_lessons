# Создать список, состоящий и кубов нечётных чисел от 0 до 100
# a. вычислить сумму тех значений из этого списка, сумма цифр которых делятся нацело на 7 (арифметическими действиями)
# b. к каждому значению списка добавить 17 и заново вычислить сумму тех значений,
# сумма цифр которых делятся нацело на 7 (не пересоздавая список)


# Решение без использования списковых включений и функций, с использованием арифметических операций:

number_list = []
for item in range(101):
    if item % 2:
        number_list.append(item ** 3)

result_sum = 0

for number in number_list:
    number_sum = 0
    item = number
    while number:
        number_sum += number % 10
        number = number // 10
    if number_sum % 7 == 0:
        result_sum += item

print(*number_list)

print(f'\nСумма кубов чисел от 0 до 100, сумма цифр которых делится на семь, равна {result_sum}\n')

result_sum = 0

for idx in range(len(number_list)):
    number_sum = 0
    number_list[idx] += 17
    item = number_list[idx]
    while item:
        number_sum += item % 10
        item = item // 10
    if number_sum % 7 == 0:
        result_sum += number_list[idx]

print(*number_list)

print(f'\nСумма кубов чисел от 0 до 100 (+17), сумма цифр которых делится на семь, равна {result_sum}\n')


# Более короткое и оптимальное решение, но с функцией, списковыми включениями и
# сумма цифр определяется не арифметическими действиями:

def sum_list(data_list: list) -> int:
    result = 0
    for element in data_list:
        sum_element = sum([int(elem) for elem in str(element)])
        if not sum_element % 7:
            result += element
    return result


number_list = [num ** 3 for num in range(101) if num % 2]

print(*number_list)

print(f'\nСумма кубов чисел от 0 до 100, сумма цифр которых делится на семь, равна {sum_list(number_list)}\n')

for idx in range(len(number_list)):
    number_list[idx] += 17

print(*number_list)

print(f'\nСумма кубов чисел от 0 до 100, сумма цифр которых делится на семь, равна {sum_list(number_list)}\n')
