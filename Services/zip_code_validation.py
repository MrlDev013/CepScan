import requests
import Services.sheet_add_column_result as scr

def zip_code_validation(sheet):

    column_name = 'CEP'
    column = sheet[column_name]

    for index, value in column.items():
        url = f'https://viacep.com.br/ws/{value}/json/'
        response = requests.get(url)
        data = None

        if response.status_code == 200:
            data = response.json()
            scr.create_sheet_column_result(sheet, data)
            print(data)
        else:
            print(f"Erro na requisição:{response.status_code} | Resultado: {value}")

    return sheet