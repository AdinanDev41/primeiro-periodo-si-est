#Faça um programa para determinar o número de dígitos de um
#número inteiro positivo. Não pode converter para string. ;-)

numero = int(input("Digite um numero: "))

if (numero < 0):
    print("Digite um numero positivo")

else:
    if numero == 0:
        digitos = 1

    else:
        cont = 0
        num = numero
        while num > 0:
            num = num // 10
            cont += 1
        digitos = cont

    print("O numero", numero, "tem", digitos, "digitos")