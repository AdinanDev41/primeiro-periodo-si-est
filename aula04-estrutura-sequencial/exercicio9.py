#Faça um algoritmo que receba o salário de um funcionário, calcule e
#mostre o novo salário, sabendo-se que este sofreu um aumento de
#25%.

salario = float(input("Digite seu salario: "))
print("Seu salario é:", salario)

salario_novo = salario + (salario * 0.25)

print("Seu novo salario é:", salario_novo)