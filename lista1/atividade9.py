#Faça um algoritmo que calcule e mostre a área de um triângulo. Sabe-se
#que area = (base * altura)/2

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area = (base * altura) / 2

print("A area de seu triangulo é:", round(area, 2), "cm²")