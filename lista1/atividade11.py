#Escreva um programa que receba um número positivo e maior que zero,
#calcule e mostre:
#a. O número digitado ao quadrado;
#b. O número digitado ao cubo;
#c. A raiz quadrada do número digitado;

num = float(input("Digite um numero: "))

a = num ** 2
b = num ** 3
c = num ** 0.5

if num > 0:
    print("O seu numero ao quadrado é:", a)
    print("O seu numero ao cubo é:", b)
    print("A raiz quadrada do seu numero é:", c)

else:
    print("Numero invalido")








