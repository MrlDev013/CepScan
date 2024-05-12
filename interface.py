import tkinter as tk
from tkinter import filedialog
import pandas as pd
import Services.zip_code_validation as zcv

def attach_sheet(): 
    text = tk.Text(janela_principal)
    text.pack()

    file_type = [("Planilhas Excel", "*.xlsx")]

    file_path = filedialog.askopenfilename(filetypes=file_type)

    if file_path:
        try:
            sheet = pd.read_excel(file_path)
            text.insert(tk.END, "Planilha anexada com sucesso!\n")

            if 'CEP' in sheet.columns:
                zcv.zip_code_validation(sheet)  
            else:
                text.insert(tk.END, "Erro! Coluna 'cep' não encontrada na planilha.\n")
        
        except Exception as e:
            text.insert(tk.END, f"Erro! Planilha NÃO anexada. \nMotivo: {str(e)}\n")

janela_principal = tk.Tk()
janela_principal.title("CepScan")

janela_principal.minsize(400, 200)
janela_principal.maxsize(500, 250)
janela_principal.configure(bg="#f0f0f0")  


titulo_label = tk.Label(janela_principal, text="Planilha", font=("Helvetica", 18), bg="#f0f0f0")
titulo_label.pack(pady=10)

botao_anexar = tk.Button(janela_principal, text="Anexar Planilha", font=("Helvetica", 12), command=attach_sheet)
botao_anexar.pack(pady=10)

janela_principal.mainloop()
