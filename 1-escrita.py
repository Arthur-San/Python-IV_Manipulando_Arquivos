name = input('digite seu nome: \n')

"""
- Arquivos
1 - opção w - write
2 - opção a - apprend
3 - opção r - read
"""

# Alternativa 1
# file = open("names.txt", "a")
# file.write(f"\n{name}")
# file.close()

# Alternativa 2
with open("dados/names.txt", "a") as file:
    file.write(f"\n{name}")