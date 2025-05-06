#Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos,
#para os quais fornece a quantidade de ração em gramas. A quantidade
#diária de ração fornecida para cada gato é sempre a mesma. Escreva um
#programa que receba o peso do saco de ração e a quantidade de ração
#fornecida para cada gato, calcule e mostre quanto restará de ração no saco
#após cinco dias.

racao = float(input("Digite a quantidade de ração em kg: "))
racao_gato = float(input("Digite a quantidade de ração para os gatos em grama: "))

racao_grama = racao * 1000

consumo_diario =  racao_gato * 2
consumo_total = consumo_diario * 5

resto = racao_grama - consumo_total

print(f"")