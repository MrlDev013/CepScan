import pandas as pd

def create_sheet_column_result(sheet, data):
    new_column = 'Resultado'

    for index, row in sheet.iterrows():
        cep_value = row['CEP']  

        if cep_value.replace('-', '') in data or cep_value in data:
            result = data[cep_value.replace('-', '') or cep_value]
            sheet.loc[index, new_column] = result  
        else:
            sheet.loc[index, new_column] = 'CEP não encontrado'  

    return sheet

    