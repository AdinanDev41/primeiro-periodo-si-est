#Sabe-se que:
#• pé = 12 polegadas
#• 1 jarda = 3 pés
#• 1 milha = 1,760 jarda
#Escreva um programa que receba uma medida em pés, faça as
#conversões a seguir e mostre os resultados.
#a) polegadas;
#b) jardas;
#c) milhas.

pes = float(input("Digite a quantidade de pés: "))

a = pes * 12
print("A medida em polegadas é:", a)

b = pes / 3
print("A sua medida em jardas é:", b)

c = b / 1760
print("A sua medida em milhas é:", c)