import sys
import csv

if len(sys.argv) < 2:
    print("Uso: python script.py <caminho_do_arquivo.csv>")
    sys.exit(1)

caminho_arquivo = sys.argv[1]
with open(caminho_arquivo, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)