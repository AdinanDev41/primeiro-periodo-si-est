#Leia o salário de um trabalhador e o valor da prestação de um
#empréstimo. Se a prestação for maior que 20% do salário imprima:
#Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.

salario = float(input("Digite o seu salario: "))
prest_emp = float(input("Digite o valor do emprestimo: "))

if (prest_emp > (salario * 0.2)):
    print("Emprestimo não concedido")

else:
    print("Emprestimo concedido")

