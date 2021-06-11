import requests


def currency_rates(val_code):
    url = r'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url).text.split('<NumCode>')

    date_start = response[0].find('ValCurs Date="') + 14
    date_finish = date_start + 10
    date = response[0][date_start:date_finish]

    result_dict = dict()

    for item in response[1:]:
        char_code_start = item.find('<CharCode>') + 10
        char_code_finish = item.find('</CharCode>')
        value_start = item.find('<Value>') + 7
        value_finish = item.find('</Value>')
        result_dict[item[char_code_start:char_code_finish]] = float(item[value_start:value_finish].replace(',', '.'))

    return date, result_dict.get(val_code.upper())


if __name__ == '__main__':
    result_1 = currency_rates('USD')
    result_2 = currency_rates('EUR')
    print(f'Курс доллара от {result_1[0]} составляет {result_1[1]} руб.')
    print(f'Курс евро от {result_2[0]} составляет {result_2[1]} руб.')
