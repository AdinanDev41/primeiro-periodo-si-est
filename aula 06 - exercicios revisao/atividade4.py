#Faça um programa que leia 2 notas de um aluno, verifique se as
#notas são válidas e exiba na tela a média destas notas. Uma nota
#válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde
#caso a nota não possua um valor válido, este fato deve ser
#informado ao usuário e o programa termina.

nota1 = float(input("Informe a primeira nota: "))
if (nota1 < 0 or nota1 > 10):
    print("A nota", nota1, "é invalida")
    quit(1)

nota2 = float(input("Informe a segunda nota: "))
if (nota2 < 0 or nota2 > 10):
    print("A nota", nota2, "é invalida")
    quit(1)

media = (nota1 + nota2) / 2

print("Sua media é:", round(media, 2))

