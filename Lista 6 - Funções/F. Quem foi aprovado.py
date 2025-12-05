n = int(input())

nomes = []
notas = []

def alunos_acima_da_media(nomes, notas):
    aprovados = []
    for i in range(n):
        nome = nomes[i]
        nota = notas[i]
        if nota >= 7.0:
            aprovados.append(nome)
    return aprovados

for _ in range(len(nomes) < n):
    nome_do_aluno = str(input())
    nota_do_aluno = float(input())
    nomes.append(nome_do_aluno)
    notas.append(nota_do_aluno)

aprovados = alunos_acima_da_media(nomes, notas)
print("Os alunos que foram aprovados foram: ")
for aluno in aprovados:
    print(aluno)