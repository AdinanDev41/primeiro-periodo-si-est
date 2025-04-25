#Faça um programa que leia dois pontos num espaço
#bidimensional e calcule a distância entre esses pontos

x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))

x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

# Calcula a distância euclidiana
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
raiz_dist = distancia ** 0.5

# Exibe o resultado com duas casas decimais
print(round(raiz_dist), "cm")
