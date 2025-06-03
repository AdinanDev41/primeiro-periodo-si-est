#https://www.youtube.com/watch?v=u1aRkx4eqJY
#https://www.youtube.com/watch?v=q5uM4VKywbA
#https://www.youtube.com/watch?v=F8KB5_sEQH0

#python processar_notas.py "c/aulas/nota"

import csv

banco_dados_notas = [
    ['1', 'Introducao a Programacao de Computadores'],
    ['5.0', '1', '1', '1'],
    ['2024001', '5.9', '6.7', '7.9'],
    ['2024002', '7.9', '8.4', '1.6'],
    ['2024003', '9.5', '5.7', '8.2'],
    ['2024004', '3.7', '7.6', '1.9'],
    ['2024005', '5.9', '8.4', '3.3'],
]

with open('teste1.csv', 'w') as arquivo:
    for notas in banco_dados_notas:
        linha_p_escrita = ','.join(notas)
        arquivo.write(linha_p_escrita + '\n')

print(linha_p_escrita)

lista = [1, 2, 3, None]


        
        