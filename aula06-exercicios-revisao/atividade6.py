#Faça um programa que receba a altura e o sexo de uma pessoa e
#calcule e mostre seu peso ideal, utilizando as seguintes fórmulas
#(onde h corresponde à altura):
# Homens: (72.7 ∗ h) − 58 e Mulheres: (62, 1 ∗ h) − 44, 7

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")
imc_homem = (72.7 * altura) - 58
imc_mulher = (62.1 * altura) - 44.7

if (sexo == "Homem"):
    print("Seu peso ideal é", imc_homem)

elif (sexo == "Mulher"):
    print("Seu peso ideal é", imc_mulher)

else:
    print("Erro")