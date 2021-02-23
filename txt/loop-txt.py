import glob
import re
import pandas as pd
import numpy as np
import csv


with open('1.csv', mode='w', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['artigo','citacoes','palavras-chave']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()


    for filepath in glob.iglob('*.txt'):

        nome = str(filepath).replace(".txt","")
        titulo = re.sub(r"\d+-", "", nome)

        with open (filepath, 'r', encoding="utf-8") as infile:
            arquivo = infile.read()
            citacoes = re.findall(r'[A-Z]+, \w+\.', arquivo)
            citacoes = str(citacoes).replace("[","")
            citacoes = str(citacoes).replace("]","")
            citacoes = str(citacoes).replace("\'","")
            citacoes = str(citacoes).replace("\"","")
            citacoes = re.sub(r"[a-z]+", "", citacoes)
            citacoes = str(citacoes).replace(".,",";")
            citacoes = str(citacoes).replace(".","")
            citacoes = str(citacoes).replace(", ;",";")
            citacoes = re.sub(r"\d{4}", "", citacoes)
            # intituicoes
            citacoes = re.sub(r"\w+, ;", "", citacoes)

        with open (filepath, 'r', encoding="utf-8") as infile:
            for line in infile:
                if re.search(r"^.*\b(Palavras-chave)\b.*$", line):
                    palavrasChave = line.replace(r"Palavras-chave: ","")
                    palavrasChave = palavrasChave.replace(".",",")
                    palavrasChave = palavrasChave.replace(";",",")
                    palavrasChave = re.sub(r"(,)[^,]*$", "", palavrasChave)   
                    writer.writerow({'artigo': titulo,'citacoes': citacoes,'palavras-chave': palavrasChave})
