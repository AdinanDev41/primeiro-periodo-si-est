#Faça um programa que informe a distância em quilômetros de
#um raio para o observador
#O observador deve informar o tempo (em segundos)
#transcorrido entre ver o raio e ouvir o trovão
#Assuma que a velocidade do som é 340 m/s

temp_seg = float(input("Informe o tempo (em segundos) entre ver o raio e ouvir o trovão: "))

# Velocidade do som em m/s
v_som = 340

# Calcula a distância em metros
dist_m = temp_seg * v_som

# Converte a distância para quilômetros
dist_km = dist_m / 1000

print(round(dist_km, 2), "km")