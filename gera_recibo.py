from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Variáveis
cliente = input("informe o nome do cliente: ")
consulta = input('informe o tipo de consulta: ')
vlr = input('informe o valor da consulta: ')
vlr_msg = f"{vlr} reais"
vlr_extenso = num2words(float(vlr), lang='pt-br')
vlr_extenso_msg = f"{vlr_extenso} reais"

data = date.today()
dia = data.day
mes = data.month
ano = data.year


# 2- layout do recibo

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.image("dados/rec.jpg", x=0, y=0)
pdf.text(162, 45, vlr_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 108, vlr_extenso_msg)
pdf.text(80, 135, consulta)

pdf.set_text_color(255,255,255)

pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))

nome_arquivo = f"{cliente.strip()}_{dia}_{mes}_{ano}"

pdf.output(f"{nome_arquivo}.pdf")
print("recibo gerado!")
