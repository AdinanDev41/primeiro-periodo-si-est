import sys
import os

# Caminho da pasta onde estão os arquivos CSV
caminho_pasta = sys.argv[1]

# Lista os arquivos CSV da pasta
arquivos = []
for nome in os.listdir(caminho_pasta):
    if nome.endswith(".csv"):
        arquivos.append(os.path.join(caminho_pasta, nome))

# Abre o arquivo de resultado
saida = open("resultado.txt", "w", encoding="utf-8")

# Variáveis globais
total_alunos = 0
soma_medias = 0
total_aprovados = 0
alunos_info = {}  # matricula: lista de (media, aprovado, nome_disciplina)
disciplinas_taxa = {}  # nome_disciplina: taxa_aprovacao

for arquivo in arquivos:
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

        # Linha 1: código e nome
        cod, nome_materia = linhas[0].strip().split(",")

        # Linha 2: média mínima e pesos
        mmin, p1, p2, p3 = linhas[1].strip().split(",")
        mmin = float(mmin)
        p1, p2, p3 = int(p1), int(p2), int(p3)
        soma_pesos = p1 + p2 + p3

        # Variáveis por turma
        alunos = 0
        aprovados = 0
        medias = []

        for linha in linhas[2:]:
            coluna = linha.strip().split(",")
            mat = coluna[0]
            n1, n2, n3 = float(coluna[1]), float(coluna[2]), float(coluna[3])
            media = (n1*p1 + n2*p2 + n3*p3) / soma_pesos
            aprovado = media >= mmin

            medias.append(media)
            alunos += 1
            if aprovado:
                aprovados += 1

            if mat not in alunos_info:
                alunos_info[mat] = []
            alunos_info[mat].append((media, aprovado, nome_materia))

        media_turma = sum(medias) / alunos
        acima_media = sum(1 for m in medias if m > media_turma)

        # Estatísticas globais
        total_alunos += alunos
        soma_medias += sum(medias)
        total_aprovados += aprovados
        taxa_aprov = (aprovados / alunos) * 100
        disciplinas_taxa[nome_materia] = taxa_aprov

        # Escreve estatísticas da turma
        saida.write(f"Turma {cod} - {nome_materia}\n")
        saida.write(f"Alunos: {alunos}\n")
        saida.write(f"Aprovados: {taxa_aprov:.2f}%\n")
        saida.write(f"Média da turma: {media_turma:.2f}\n")
        saida.write(f"Acima da média: {acima_media}\n")
        saida.write(f"Maior: {max(medias):.2f} | Menor: {min(medias):.2f}\n\n")

# Estatísticas globais
media_geral = soma_medias / total_alunos
aprov_geral = (total_aprovados / total_alunos) * 100
mais_2_disc = 0
aprovados_todas = 0

saida.write("ESTATÍSTICAS GLOBAIS\n")
saida.write(f"Média global: {media_geral:.2f}\n")
saida.write(f"Aprovação global: {aprov_geral:.2f}%\n")

for mat, dados in alunos_info.items():
    if len(dados) > 2:
        mais_2_disc += 1
    if all(d[1] for d in dados):
        aprovados_todas += 1

saida.write(f"Alunos com >2 disciplinas: {mais_2_disc}\n")
saida.write(f"Aprovados em todas: {aprovados_todas} ({(aprovados_todas / len(alunos_info))*100:.2f}%)\n")

maior_disc = max(disciplinas_taxa, key=disciplinas_taxa.get)
menor_disc = min(disciplinas_taxa, key=disciplinas_taxa.get)
saida.write(f"Maior taxa de aprovação: {maior_disc} ({disciplinas_taxa[maior_disc]:.2f}%)\n")
saida.write(f"Menor taxa de aprovação: {menor_disc} ({disciplinas_taxa[menor_disc]:.2f}%)\n\n")

# Estatísticas por aluno
saida.write("ESTATÍSTICAS POR ALUNO\n")
for mat, dados in alunos_info.items():
    aprov = sum(1 for d in dados if d[1])
    taxa = (aprov / len(dados)) * 100
    melhor = max(dados, key=lambda x: x[0])
    pior = min(dados, key=lambda x: x[0])

    saida.write(f"Aluno {mat}\n")
    saida.write(f"Taxa de aprovação: {taxa:.2f}%\n")
    saida.write(f"Melhor: {melhor[2]} ({melhor[0]:.2f})\n")
    saida.write(f"Pior: {pior[2]} ({pior[0]:.2f})\n\n")

saida.close()
print("Arquivo resultado.txt criado com sucesso.")