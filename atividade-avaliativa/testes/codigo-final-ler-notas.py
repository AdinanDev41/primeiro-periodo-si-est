import sys
import os

# Pega o caminho da pasta informado pelo terminal
caminho_pasta = sys.argv[1]

# Vao listar os arquivos .csv
arquivos = []
for nome in os.listdir(caminho_pasta):
    if nome.endswith(".csv"):
        arquivos.append(os.path.join(caminho_pasta, nome))

# Abre o arquivo resultado.txt para escrita
saida = open("resultado.txt", "w", encoding="utf-8")

# Variáveis globais
alunos_info = {}  # matricula: lista de (media, aprovado, nome_disciplina, turma)
disciplinas_taxa = {}
total_alunos_por_matricula = set()
total_alunos_por_disciplina = 0
total_aprovados = 0
soma_geral = 0

# Processa cada CSV
for arq in arquivos:
    with open(arq, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    cod, nome_disc = linhas[0].strip().split(",")
    mmin, p1, p2, p3 = linhas[1].strip().split(",")
    mmin, p1, p2, p3 = float(mmin), int(p1), int(p2), int(p3)
    soma_pesos = p1 + p2 + p3

    qtd_alunos = 0
    aprovados = 0
    medias = []
    acima_media = 0
    notas_aluno = []

    for linha in linhas[2:]:
        coluna = linha.strip().split(",")
        mat = coluna[0]
        n1, n2, n3 = float(coluna[1]), float(coluna[2]), float(coluna[3])
        media = (n1*p1 + n2*p2 + n3*p3) / soma_pesos
        status = media >= mmin

        total_alunos_por_matricula.add(mat)
        alunos_info.setdefault(mat, []).append((media, status, nome_disc, cod))

        qtd_alunos += 1
        medias.append(media)
        if status:
            aprovados += 1
        notas_aluno.append((mat, media))

    media_turma = sum(medias) / qtd_alunos
    acima_media = sum(1 for m in medias if m > media_turma)
    menor = min(medias)
    maior = max(medias)

    taxa_aprov = (aprovados / qtd_alunos) * 100
    disciplinas_taxa[f"{nome_disc} ({cod})"] = taxa_aprov
    total_aprovados += aprovados
    soma_geral += sum(medias)
    total_alunos_por_disciplina += qtd_alunos

    saida.write(f"Código da turma: {cod}, Disciplina: {nome_disc}.\n")
    saida.write(f"Numero de alunos: {qtd_alunos}, média da turma: {media_turma:.2f}\n")
    saida.write(f"Alunos aprovados: {aprovados}, Alunos Reprovados: {qtd_alunos - aprovados}. Percentual de alunos aprovados:{taxa_aprov:.1f}%\n")
    saida.write(f"{acima_media} Alunos estão acima da média da turma.\n")
    saida.write(f"Menor média: {menor:.2f}, Maior média: {maior:.2f}\n")
    saida.write("\n")

# Estatísticas globais
total_matriculas = len(total_alunos_por_matricula)
media_global = soma_geral / total_alunos_por_disciplina
aprov_global = (total_aprovados / total_alunos_por_disciplina) * 100
alunos_2mais = 0
alunos_todos_aprov = 0

saida.write(f"O total de alunos (por disciplina) do professor é: {total_alunos_por_disciplina}, o total de alunos (por matrícula) é: {total_matriculas} \n")
saida.write(f"A média global foi: {media_global:.2f}\n")
saida.write(f"A taxa de aprovação geral foi: {aprov_global:.2f}%, com um total de {total_aprovados} aprovações.\n")

for mat, dados in alunos_info.items():
    if len(dados) >= 2:
        alunos_2mais += 1
    if all(info[1] for info in dados):
        alunos_todos_aprov += 1

saida.write(f"{alunos_2mais} alunos estão em 2+ turmas, {alunos_todos_aprov} alunos passaram em todas disciplinas.\n")

mais_aprov = max(disciplinas_taxa, key=disciplinas_taxa.get)
menos_aprov = min(disciplinas_taxa, key=disciplinas_taxa.get)
saida.write(f"Disciplina com maior taxa de aprovação: {mais_aprov} ({disciplinas_taxa[mais_aprov]:.2f}%)\n")
saida.write(f"Disciplina com menor taxa de aprovação: {menos_aprov} ({disciplinas_taxa[menos_aprov]:.2f}%)\n\n")

# Estatísticas por aluno
for mat, dados in alunos_info.items():
    saida.write(f"O aluno {mat} está em {len(dados)} turma(s):\n")
    for info in dados:
        m, st, d, c = info
        status_txt = "Aprovado" if st else "Reprovado"
        saida.write(f"Turma: {c}, Disciplina: {d}, Média: {m:.2f}, Status: {status_txt}\n")

    menor_media = min(dados, key=lambda x: x[0])
    maior_media = max(dados, key=lambda x: x[0])
    aprov = sum(1 for i in dados if i[1])
    taxa = (aprov / len(dados)) * 100

    saida.write(f"A menor média foi {menor_media[0]:.2f}, em {menor_media[2]}\n")
    saida.write(f"A maior média foi {maior_media[0]:.2f}, em {maior_media[2]}\n")
    saida.write(f"O aluno tem {taxa:.0f}% de aprovação geral\n\n")

saida.close()
print("Arquivo resultado.txt gerado com sucesso.")
