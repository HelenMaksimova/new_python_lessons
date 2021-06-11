import requests
import xml.etree.ElementTree as Et
import datetime


def currency_rates(val_code):
    url = r'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url).text
    root = Et.fromstring(response)

    for child in root.findall('Valute'):
        char_code = child.find('CharCode').text
        if char_code == val_code.upper():
            data_list = [int(elem) for elem in root.attrib['Date'].split('.')[::-1]]
            data = datetime.date(*data_list)
            result = child.find('Value').text.replace(',', '.')
            return float(result), str(data)


if __name__ == '__main__':
    print('Курс доллара от {1} составляет {0} руб.'.format(*currency_rates('USD')))
    print('Курс евро от {1} составляет {0} руб.'.format(*currency_rates('EUR')))
