# Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
# виде словаря. Если адрес не валиден, выбросить исключение ValueError.

import re

RE_E_MAIL = re.compile(r'(^[\w-]+)@([\w-]+\.[\w-]+$)')


def parse_e_mail(mail):
    result = RE_E_MAIL.findall(mail)
    if not result:
        raise ValueError(f'wrong email: {mail}')
    result_dict = dict(zip(('username', 'domain'), result[0]))
    return result_dict


e_mails = [
    'lala@tralala.com',
    'la-la@tra_lala.com',
    'lala@tra.lala.com'
]

for e_mail in e_mails:
    print(parse_e_mail(e_mail))
