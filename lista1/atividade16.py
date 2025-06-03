#Escreva um programa que receba o número de horas trabalhadas e o valor
#do salário mínimo, calcule e mostre o salário a receber, seguindo estas
#regras:
#a. A hora trabalhada vale a metade do salário mínimo.
#b. O salário bruto equivale ao número de horas trabalhadas
#multiplicado pelo valor da hora trabalhada.
#c. O imposto equivale a 3% do salário bruto.
#d. O salário a receber equivale ao salário bruto menos o imposto.

salario_min = float(input("Digite o seu salario: "))
horas = float(input("Digite as horas trabalhadas: "))

horas_trab = salario_min / 2
salario_bruto = horas_trab * horas
imposto = salario_bruto * 0.03
salario_final = salario_bruto - imposto

print("Seu salario final é:", salario_final)