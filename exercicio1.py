## Lendo n linhas de um arquivo

# Escreva um programa Python para ler as primeiras n linhas de um arquivo.

# 1. O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.

def file_read_from_line(fname, nlines):
        from itertools import islice
        with open(fname, encoding="utf-8") as f:
                for line in islice(f, nlines):
                        print(line.rstrip())

file_read_from_line('dados/texto.txt', 6)
    
    

