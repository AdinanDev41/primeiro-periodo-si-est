#Escreva um programa que receba quatro notas de um aluno, calcule e
#mostre a média aritmética das notas e a mensagem de aprovado ou
#reprovado, considerando para aprovação média 6,0.

n1 = int(input("Digite sua nota: "))
n2 = int(input("Digite sua nota: "))
n3 = int(input("Digite sua nota: "))
n4 = int(input("Digite sua nota: "))

media = (n1 + n2 + n3 + n4) / 4

if (n1 > 10) or (n2 > 10) or (n3 > 10) or (n4 > 10):
    print("Nota invalida")

elif (media < 6):
    print("Reprovado :(, sua media é:", media)

else:
    print("Passouuuu, sua media é:", media)