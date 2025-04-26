#Escreva um programa que receba três notas, calcule e mostre a média
#aritmética.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("Sua média é:", round(media, 2))