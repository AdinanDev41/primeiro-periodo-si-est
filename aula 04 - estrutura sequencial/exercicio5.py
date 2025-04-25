valor = int(input("Digite o valor em centavos: "))

moeda1 = 100
moeda2 = 50
moeda3 = 25
moeda4 = 10
moeda5 = 5
moeda6 = 1

# Cálculo da quantidade de cada moeda
qtd1 = valor // moeda1
valor = valor - (qtd1 * moeda1)

qtd2 = valor // moeda2
valor = valor - (qtd2 * moeda2)

qtd3 = valor // moeda3
valor = valor - (qtd3 * moeda3)

qtd4 = valor // moeda4
valor = valor - (qtd4 * moeda4)

qtd5 = valor // moeda5
valor = valor - (qtd5 * moeda5)

qtd6 = valor // moeda6
valor = valor - (qtd6 * moeda6)

print("Menor quantidade de moedas necessárias:")
if qtd1 > 0:
    print(qtd1, "moeda(s) de 1 real")
if qtd2 > 0:
    print(qtd2, "moeda(s) de 50 centavos")
if qtd3 > 0:
    print(qtd3, "moeda(s) de 25 centavos")
if qtd4 > 0:
    print(qtd4, "moeda(s) de 10 centavos")
if qtd5 > 0:
    print(qtd5, "moeda(s) de 5 centavos")
if qtd6 > 0:
    print(qtd6, "moeda(s) de 1 centavo")
