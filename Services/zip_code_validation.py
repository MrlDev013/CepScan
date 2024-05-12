import requests

def zip_code_validation(sheet):

    column_name = 'CEP'
    column = sheet[column_name]

    for indice, valor in column.items():
        url = f'https://viacep.com.br/ws/{valor}/json/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(f"Erro na requisição:{response.status_code} | Valor: {valor}")

    