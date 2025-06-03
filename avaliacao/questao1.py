#escreva um programa em python que le tres numeros distintos e: 
#em caso de algum numero repetido, exibe uma mensagem de erro e encerra
#imprima os tres em ordem crescente
#imprima a media aritmetica dos tres
#imprima a diferença entre o maior e menor

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))
num3 = float(input("Digite um numero: "))

if (num1 == num2) or (num1 == num3) or (num2 == num3):
    print("Erro")

else:
    if (num1 > num2 > num3):   #quando o num1 for o maior, o num2 for o intermediario e o num3 for o menor
        print(num3, num2, num1)

    elif (num1 > num3 > num2):   #quando o num1 for o maior, o num3 for o intermediario e o num2 for o menor
        print(num2, num3, num1)

    elif (num2 > num1 > num3):  #quando o num2 for o maior, o num1 for o intermediario e o num3 for o menor
        print(num3, num1, num2)

    elif (num2 > num3 > num1):  #quando o num2 for o maior, o num3 for o intermediario e o num1 for o menor
        print(num1, num3, num2)

    elif (num3 > num2 > num1): #quando o num3 for o maior, o num2 for o intermediario e o num1 for o menor
        print(num1, num2, num3)
    
    elif (num3 > num1 > num2):  #quando o num3 for o maior, o num1 for o intermediario e o num2 for o menor
        print(num2, num1, num3)

    media = (num1 + num2 + num3) / 3
    print("A media é:", round(media, 2))

    if (num1 > num2 > num3):   #quando o num1 for o maior, o num2 for o intermediario e o num3 for o menor
        print(num1 - num3)

    elif (num1 > num3 > num2):   #quando o num1 for o maior, o num3 for o intermediario e o num2 for o menor
        print(num1 - num2)

    elif (num2 > num1 > num3):  #quando o num2 for o maior, o num1 for o intermediario e o num3 for o menor
        print(num2 - num3)

    elif (num2 > num3 > num1):  #quando o num2 for o maior, o num3 for o intermediario e o num1 for o menor
        print(num2 - num1)

    elif (num3 > num2 > num1): #quando o num3 for o maior, o num2 for o intermediario e o num1 for o menor
        print(num3 - num1)
    
    elif (num3 > num1 > num2):  #quando o num3 for o maior, o num1 for o intermediario e o num2 for o menor
        print(num3 - num2)