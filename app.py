
import requests
import openpyxl

wb = openpyxl.Workbook()

planilha = wb.active

planilha['A1'] = 'Id' # 6,70
planilha['B1'] = 'Símbolo' #2,45
planilha['C1'] = 'Nome' # 6,75



url = 'https://api.coingecko.com/api/v3/coins/list'

response = requests.get(url=url)

if response.status_code == 200:
    dados_excel = []

    dados = response.json()


    for item in dados:
        tupla_aux = (item['id'] , item['symbol'] , item['name'])
        dados_excel.append(tupla_aux)
        # print(item)


else:
    print("Erro")


for i in dados_excel:
    planilha.append(i)

wb.save('cripto_db.xlsx')

