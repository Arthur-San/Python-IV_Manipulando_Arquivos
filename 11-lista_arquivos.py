import glob, os, zipfile

# 1 - diretório de trabalho atual
os.getcwd()

# 2 - listar todos os arquivos .txt
for file in glob.glob("dados/*.txt"):
    print(file)

# 3 - listar todos os arquivos .csv
for file in glob.glob("dados/*.csv"):
    print(file)

# 4 - compactar arquivos .txt
with zipfile.ZipFile("names_txt.zip", "w") as zip:
    for file in glob.glob("dados/*.txt"):
        zip.write(file)

# 5 - compactar arquivos .csv
with zipfile.ZipFile("courses_csv.zip", "w") as zip:
    for file in glob.glob("dados/*.csv"):
        zip.write(file)

# 6 - compactar todos arquivos 
with zipfile.ZipFile("courses_csv_txt.zip", "w") as zip:
    for file in glob.glob("dados/*"):
        zip.write(file)
