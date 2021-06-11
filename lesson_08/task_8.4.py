# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
# значения функции и выбрасывать исключение ValueError, если что-то не так
# Примечание: сможете ли вы замаскировать работу декоратора?

from math import log, e
from functools import wraps


def validate(*args):
    for item in args:
        if isinstance(item, str):
            return 'Аргумент является строкой!'
        if item <= 0:
            return 'Аргумент меньше либо равен нулю!'


def decorate(val_func):
    def _decorate(func):
        @wraps(func)
        def wrapper(*args):
            val_res = val_func(*args)
            if val_res is not None:
                raise ValueError(val_res)
            result = func(*args)
            return result
        return wrapper
    return _decorate


@decorate(validate)
def ln(number):
    return log(number, e)


print(ln(10))
print(ln('10'))
