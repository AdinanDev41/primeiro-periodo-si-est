#O custo ao consumidor de um carro novo é a soma do preço de fábrica com
#o percentual de lucro do distribuidor e dos impostos aplicados ao preço de
#fábrica. Escreva um programa que receba o preço de fábrica de um veículo,
#o percentual de lucro do distribuidor e o percentual de impostos, calcule e
#mostre:
#a. O valor correspondente ao lucro do distribuidor;
#b. O valor correspondente aos impostos;
#c. O preço final do veículo.

preco_fab = float(input("Digite o preço de fábrica do carro: "))
preco_perc = float(input("Digite o percentual de lucro: "))
imposto = float(input("Digite o valor do imposto: "))

valor_luc = preco_fab * (preco_perc / 100)
valor_imp = preco_fab * (imposto / 100)
preco_final = preco_fab + valor_luc + valor_imp

print("O valor do lucro do distribuidor é:", valor_luc)
print("O valor do imposto é:", valor_imp)
print("O valor do carro final é:", preco_final)