#Escreva um programa que receba dois números maiores que zero, calcule e
#mostre um elevado ao outro.

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))

ex = num1 ** num2

if num1 > 0 and num2 > 0:
    print("O seu resultado é:", ex)

else: 
    print("Numero invalido")