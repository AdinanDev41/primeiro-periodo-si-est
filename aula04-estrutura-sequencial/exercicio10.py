#Faça um algoritmo que receba o salário de um funcionário e o
#percentual de aumento, calcule e mostre o valor do aumento e o novo
#salário.

salario = float(input("Digite seu salario: "))
aumento = float(input("Digite o percentual de aumento: "))

novo_salario = salario + (salario * aumento)

print("Seu novo salario é:", novo_salario)
