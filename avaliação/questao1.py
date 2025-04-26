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
    nums = [num1, num2, num3]  #num sei fazer sem lista :(
    nums.sort()
    print("Números em ordem crescente:", nums)
    media = (num1 + num2 + num3) / 3
    print("Média aritmética:", round(media, 2))
    print("Diferença entre o maior e o menor:", nums[-1] - nums[0])


