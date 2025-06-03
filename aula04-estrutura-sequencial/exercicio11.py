#Faça um algoritmo que receba o salário base de um funcionário, calcule
#e mostre o salário a receber, sabendo-se que o funcionário tem
#gratificação de 5% sobre o salário base e paga imposto de 7% também
#sobre o salário base.

salario = float(input("Digite seu salario: "))
gratificacao = 0.05

novo_salario = (salario + (salario * gratificacao))
desct_salario = novo_salario - (salario * 0.07)

print("Seu salario é:", desct_salario)

