#Faça um algoritmo que receba três notas e seus respectivos pesos,
#calcule e mostre a média ponderada.

nota1 = float(input("Digite a nota de sua primeira atividade: "))
nota2 = float(input("Digite a nota de sua segunda atividade: "))
nota3 = float(input("Digite a nota de sua terceira atividade: "))

peso1 = int(input("Digite o peso da primeira nota: "))
peso2 = int(input("Digite o peso da segunda nota: "))
peso3 = int(input("Digite o peso da terceira nota: "))

media_p = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) // peso1 + peso2 + peso3

print("Sua média é:", media_p)