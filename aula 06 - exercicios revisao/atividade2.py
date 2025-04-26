#Faça um programa que leia um número e, caso ele seja positivo,
#calcule e mostre: O número digitado ao quadrado e a raiz quadrada
#do número digitado

num = float(input("Digite um numero: "))

if (num >= 0):
    print("Seu numero ao quadrado é:", num ** 2)
    print("O quadrado do seu numero é:", num ** 0.5)

else:
    print("Numero invalido")
