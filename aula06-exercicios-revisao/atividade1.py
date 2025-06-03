#1)Leia um número real. Se o número for positivo imprima a raiz
#quadrada. Do contrário, imprima o número ao quadrado.

num = float(input("Digite um numero: "))

if (num >= 0):
    print("A raiz quadrada do seu numero é:", num **0.5)

else:
    print("Seu numero ao quadrado é:", num ** 2)