#Faça um algoritmo que receba o valor de um depósito e o valor da
#taxa de juros, calcule e mostre o valor do rendimento e o valor total
#depois do rendimento.

deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))

# Cálculo do rendimento (convertendo a taxa de juros para decimal)
rendimento = deposito * (taxa_juros / 100)

# Cálculo do valor total após o rendimento
total = deposito + rendimento

print(f"Rendimento: R$", rendimento)
print(f"Total após rendimento: R$", total)
