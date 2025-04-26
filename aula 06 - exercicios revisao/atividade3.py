#3)Escreva um programa que leia um número fornecido pelo usuário.
#Se esse número for positivo, calcule a raiz quadrada do número. Se
#o número for negativo, mostre uma mensagem dizendo que o
#número é inválido.

num = float(input("Digite um numero: "))

if (num > 0):
    print("A raiz quadrada do seu numero é:", num ** 0.5)

else:
    print("Numero invalido")
    