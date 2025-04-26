#Escreva um programa que leia um inteiro entre 1 e 7 e imprima o
#dia da semana correspondente a este número. Isto é, domingo se
#1, segunda-feira se 2, e assim por diante. Trate número inválido.

num = int(input("Digite um numero: "))

if (num >= 1 and num <= 7):
    if (num == 1):
        print("Domingo")
    elif (num == 2):
        print("Segunda feira")
    elif (num == 3):
        print("Terça feira")
    elif (num == 4):
        print("Quarta feira")
    elif (num == 5):
        print("Quinta feira")
    elif (num == 6):
        print("Sexta feira")
    elif (num == 7):
        print("Domingo")

else:
    print("Numero invalido")