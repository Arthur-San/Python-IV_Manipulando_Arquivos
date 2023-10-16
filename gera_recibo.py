from fpdf import FPDF
from datetime import date
import tkinter as tk

def gerar_recibo():
    cliente_nome = cliente_entry.get()
    consulta_tipo = consulta_entry.get()
    valor = float(vlr_entry.get())
    
    vlr_msg = f"{valor} reais"
    # Calcular valor por extenso aqui, se necessário
    
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 20)
    pdf.image("dados/rec.jpg", x=0, y=0)
    pdf.text(162, 45, vlr_msg)
    pdf.text(80, 86, cliente_nome)
    # Incluir o valor por extenso se necessário
    pdf.text(80, 135, consulta_tipo)

    pdf.set_text_color(255, 255, 255)
    pdf.text(30, 193, str(dia))
    pdf.text(50, 193, str(mes))
    pdf.text(70, 193, str(ano))

    nome_arquivo = f"{cliente_nome.strip()}_{dia}_{mes}_{ano}"

    pdf.output(f"{nome_arquivo}.pdf")
    print("Recibo gerado!")

window = tk.Tk()
window.geometry("400x250")
window.title('Gerador de Recibos')

frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

cliente_label = tk.Label(frame, text='Informe o nome do cliente: ')
cliente_label.pack(fill='x', expand=True)
cliente_entry = tk.Entry(frame)
cliente_entry.pack(fill='x', expand=True)

consulta_label = tk.Label(frame, text='Informe o tipo de consulta: ')
consulta_label.pack(fill='x', expand=True)
consulta_entry = tk.Entry(frame)
consulta_entry.pack(fill='x', expand=True)

vlr_label = tk.Label(frame, text='Informe o valor da consulta: ')
vlr_label.pack(fill='x', expand=True)
vlr_entry = tk.Entry(frame)
vlr_entry.pack(fill='x', expand=True)

gerar_button = tk.Button(frame, text="Gerar Recibo", command=gerar_recibo)
gerar_button.pack()

window.mainloop()
