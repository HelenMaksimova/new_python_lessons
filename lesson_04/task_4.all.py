from sys import argv
from utils import currency_rates
if len(argv) > 1:
    _, val_code = argv
    print('Курс {2} от {1} составляет {0} руб.'.format(*currency_rates(val_code), val_code.upper()))
else:
    print('Курс венгерских форинтов от {1} составляет {0} руб.'.format(*currency_rates('huf')))
