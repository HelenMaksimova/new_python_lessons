# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.


# * Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы - результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

numbers_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'zero': 'ноль',
    }


def num_translate(number: str) -> str:
    return numbers_dict.get(number.lower())


def num_translate_adv(number: str) -> str:
    return numbers_dict.get(number.lower()).title() if number[0].isupper() else numbers_dict.get(number.lower())


test_list = [item if len(item) <= 3 else item.title() for item in numbers_dict]

print('Работа функции num_translate')
for key in test_list:
    print(f'{key} - {num_translate(key)}')

print('\nРабота функции num_translate_adv')
for key in test_list:
    print(f'{key} - {num_translate_adv(key)}')
