import tkinter as tk
from tkinter import filedialog
import pandas as pd
import Services.zip_code_validation as zcv

def attach_sheet(): 
    text = tk.Text(window)
    text.pack()

    file_type = [("Planilhas Excel", "*.xlsx")]

    file_path = filedialog.askopenfilename(filetypes=file_type)

    if file_path:
        try:
            sheet = pd.read_excel(file_path)
            text.insert(tk.END, "Planilha anexada com sucesso!\n")

            if 'CEP' in sheet.columns:
                zcv.zip_code_validation(sheet)  
                sheet.to_excel(file_path, index=False)
            else:
                text.insert(tk.END, "Erro! Coluna 'cep' não encontrada na planilha.\n")
        
        except Exception as e:
            text.insert(tk.END, f"Erro! Planilha NÃO anexada. \nMotivo: {str(e)}\n")

window = tk.Tk()
window.title("CepScan")

window.minsize(400, 200)
window.maxsize(500, 250)
window.configure(bg="#f0f0f0")  


title = tk.Label(window, text="Planilha", font=("Helvetica", 18), bg="#f0f0f0")
title.pack(pady=10)

attach_button = tk.Button(window, text="Anexar Planilha", font=("Helvetica", 12), command=attach_sheet)
attach_button.pack(pady=10)

window.mainloop()
