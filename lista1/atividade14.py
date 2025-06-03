#Escreva um programa que receba o ano de nascimento de uma pessoa e o
#ano atual, calcule e mostre:
#a. A idade dessa pessoa;
#b. Quantos anos ela terá em 2050.

ano_nasc = int(input("Digite o ano em que vc nasceu: "))

a = 2025 - ano_nasc
b = 2050 - ano_nasc

print("Sua idade atual é:", a)
print("Sua idade em 2050 é:", b)