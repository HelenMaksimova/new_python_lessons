# Написать декоратор для логирования типов позиционных аргументов функции
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
# ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
# аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
# функции?

from functools import wraps


def log_type(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_str_args = (f'{arg}: {type(arg)}' for arg in args)
        log_str_kwargs = (f'{key, kwargs[key]}: {type(kwargs[key])}' for key in kwargs)
        result = func(*args, **kwargs)
        print(f'{func.__name__}({", ".join(log_str_args)}{", ".join(log_str_kwargs)}, '
              f'function value type: {type(result)})')
        return result
    return wrapper


@log_type
def cub_nums(*args):
    return [arg**3 for arg in args]


@log_type
def max_var(**kwargs):
    return max(kwargs, key=lambda x: kwargs[x])


print(cub_nums(1, 2, 3))

print(max_var(a=1, b=2, c=3))
