#Faça um algoritmo que receba o salário base de um funcionário, calcule
#e mostre seu salário a receber, sabendo-se que o funcionário tem
#gratificação de R$ 50 e paga imposto de 10% sobre o salário base.

salario = float(input("Digite seu salario: "))
gratificacao = 50

novo_salario = salario + gratificacao
desct_salario = novo_salario - (salario * 0.10)

print("Seu salario é:", desct_salario)