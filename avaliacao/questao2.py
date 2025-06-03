#escreva um programa em python que leia os dados de 3 alunos,
#contendo a altura e o codigo do sexo de cada um
#1 == masculino, 2 == feminino
#imprima a media de altura das mulheres
#a menor altura das mulheres
#imprima a media de altura dos homens
#a menor altura dos homens

aluno1_altura = float(input("Digite a altura do aluno 1: "))
aluno1_sexo = int(input("Digite o código do sexo do aluno 1 : "))
aluno2_altura = float(input("Digite a altura do aluno 2: "))
aluno2_sexo = int(input("Digite o código do sexo do aluno 2: "))
aluno3_altura = float(input("Digite a altura do aluno 3: "))
aluno3_sexo = int(input("Digite o código do sexo do aluno 3: "))

media_mulher = (aluno1_altura + aluno2_altura + aluno3_altura) / 3
media_homem = (aluno1_altura + aluno2_altura + aluno3_altura) / 3

if (aluno1_sexo == 2 and aluno2_sexo == 2 and aluno3_sexo == 2):
    print("A media das mulheres são:", round(media_mulher, 2))

    if (aluno1_altura < aluno2_altura and aluno1_altura < aluno3_altura):
        print("A menor aluna é:", aluno1_altura)

    elif (aluno2_altura < aluno1_altura and aluno2_altura < aluno3_altura):
        print("A menor aluna é:", aluno2_altura)

    elif (aluno3_altura < aluno2_altura and aluno3_altura < aluno1_altura):
        print("A menor aluna é:", aluno3_altura)



elif (aluno1_sexo == 1 and aluno2_sexo == 1 and aluno3_sexo == 1):
    print("A media dos homens é:", round(media_homem, 2))

    if (aluno1_altura > aluno2_altura and aluno1_altura > aluno3_altura):
        print("O maior aluno é:", aluno1_altura)

    elif (aluno2_altura > aluno1_altura and aluno2_altura > aluno3_altura):
        print("O maior aluno é:", aluno2_altura)

    elif (aluno3_altura > aluno2_altura and aluno3_altura > aluno1_altura):
        print("O maior aluno é:", aluno3_altura)

else:
    print("So pode alunos do mesmo sexo :p")