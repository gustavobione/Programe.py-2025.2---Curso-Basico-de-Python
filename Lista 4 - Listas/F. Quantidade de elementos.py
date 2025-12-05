elementos = []

n = float(input())
elementos.append(n)

confirmacao = input()

while confirmacao.lower() == 's':
    n = float(input())
    elementos.append(n)
    confirmacao = input()

ja_exibidos = []

for elemento in elementos:
    if elemento not in ja_exibidos:
        quantidade_repeticoes = elementos.count(elemento)
        print(f"O elemento {elemento} aparece {quantidade_repeticoes} vezes na lista")
        ja_exibidos.append(elemento)