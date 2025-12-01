nome_aluno = str(input())
nota_aluno = float(input())
lista_notas = []
lista_nomes = []
while nome_aluno != "fim":
    lista_nomes.append(nome_aluno)
    lista_notas.append(nota_aluno)
    nome_aluno = str(input())
    if nome_aluno != "fim":
        nota_aluno = float(input())

for i in range(len(lista_notas)-1):
    for j in range(i+1, len(lista_notas)):
        if lista_notas[i] < lista_notas[j]:
            lista_notas[i], lista_notas[j] = lista_notas[j], lista_notas[i]
            lista_nomes[i], lista_nomes[j] = lista_nomes[j], lista_nomes[i]
for k in range(len(lista_notas)):
    print(f"{lista_nomes[k]}: {lista_notas[k]:.2f}")