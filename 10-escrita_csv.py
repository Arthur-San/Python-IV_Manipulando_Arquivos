import csv

name = input('informe o nome da linguagem que deseja aprender\n')
category = input('qual categoria que a linguagem se encaixa?\n')


with open("dados/courses.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow([name, category])