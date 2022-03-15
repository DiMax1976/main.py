import requests
import datetime


def utils(my_list: list):
    Currency_Valutes = {}
    Currency_Valutes_list = []
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    content = response.text
    Dates_curs = content.split('><ValCurs Date=')[1]
    Dates_curs = Dates_curs.split(' name=')[0].replace('"', '')
    Dates_curs = datetime.datetime(year=int(Dates_curs.split('.')[2]), month=int(Dates_curs.split('.')[1]),
                                   day=int(Dates_curs.split('.')[0]))

    for el in content.split('ID=')[1:]:
        Valutes = (el.split('</Value></Valute><Valute')[0])
        NM_Valute = Valutes.split('</NumCode><CharCode>')[1]
        NM_Valute = NM_Valute.split('</CharCode><Nominal>')[0]
        Valutes = Valutes.split('</CharCode>')[1]
        Valutes_Names = Valutes.split('</Nominal><Name>')[1]
        Valutes_Names = Valutes_Names.split('</Name><Value>')[0]
        Valutes_Nominal = Valutes.split('</Nominal><Name>')[0]
        Valutes_Nominal = int(Valutes_Nominal.split('<Nominal>')[1])
        Cur_Valute = Valutes.split('</Name><Value>')[1]
        Cur_Valute = Cur_Valute.replace(',', '.')
        Cur_Valute = round(float(Cur_Valute.split('</Value></Valute></ValCurs>')[0]), 2)
        # Cur_Valute_RUB=str((round(Cur_Valute))) + " руб. " + str((round(Cur_Valute%1*100)))+ " коп."
        # Cur_Valute_RUB='.'.join(Cur_Valute_RUB)
        # Cur_Valute1 = Decimal(Cur_Valute) #Decimal совсем не годится!
        # print(Cur_Valute1)
        Currency_Valutes_list.append("за")
        Currency_Valutes_list.append(Valutes_Nominal)
        Currency_Valutes_list.append(Valutes_Names)
        Currency_Valutes_list.append(Cur_Valute)
        Currency_Valutes[NM_Valute] = NM_Valute
        Currency_Valutes[NM_Valute] = Currency_Valutes_list
        Currency_Valutes_list = []

    for elem in range(len(my_list)):
        elem_sp = my_list[elem].upper()
        for key, value in Currency_Valutes.items():
            if key == elem_sp:
                print(*value, ",", Dates_curs.date(), sep=' ')


if __name__ == '__maim__':
    print(utils())
