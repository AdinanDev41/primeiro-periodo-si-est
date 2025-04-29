#Faça um programa para imprimir a tabuada de multiplicação de 1 a
#10. (ex: 1x1=1, 1x2=2 etc).

for num1 in range(1, 11):
    print("Tabuada de:", num1)

    for num2 in range(1, 11):
        result = num1 * num2
        print(num1, "x", num2, "=", result)