import sys
import requests


def currency_rates(*args):
    Currency_Valutes = {}
    Currency_Valutes_list = []
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.text
    Dates_curs = content.split('><ValCurs Date=')[1]
    Dates_curs = Dates_curs.split(' name=')[0]
    print("Курс на " + Dates_curs.replace('"', ''))
    for el in content.split('ID=')[1:]:
        Valutes = (el.split('</Value></Valute><Valute')[0])
        NM_Valute = Valutes.split('</NumCode><CharCode>')[1]
        NM_Valute = NM_Valute.split('</CharCode><Nominal>')[0]
        Valutes = Valutes.split('</CharCode>')[1]
        Valutes_Names = Valutes.split('</Nominal><Name>')[1]
        Valutes_Names = Valutes_Names.split('</Name><Value>')[0]
        Valutes_Nominal = Valutes.split('</Nominal><Name>')[0]
        Valutes_Nominal = Valutes_Nominal.split('<Nominal>')[1]
        Cur_Valute = Valutes.split('</Name><Value>')[1]
        Cur_Valute = Cur_Valute.split('</Value></Valute></ValCurs>')[0]
        Currency_Valutes_list.append(Valutes_Nominal)
        Currency_Valutes_list.append(Valutes_Names)
        Currency_Valutes_list.append(Cur_Valute)
        Currency_Valutes[NM_Valute] = NM_Valute
        Currency_Valutes[NM_Valute] = Currency_Valutes_list
        Currency_Valutes_list = []

    for elem in args:
        elem = elem.upper()
        for key, value in Currency_Valutes.items():
            if key == elem:
                print(value)


currency_rates("USD", "EUR", "KZT", "GBP")
