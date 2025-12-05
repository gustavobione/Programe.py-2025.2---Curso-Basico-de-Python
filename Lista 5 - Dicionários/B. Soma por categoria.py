n = int(input())

produto = []
valor = []

for _ in range(n):
    par = str(input()).split()
    produto.append(par[0])
    valor.append(int(par[1]))

soma_por_categoria = {}

for i in range(n):
    categoria = produto[i]
    valor_total = valor[i]
    if categoria in soma_por_categoria:
        soma_por_categoria[categoria] += valor_total
    else:
        soma_por_categoria[categoria] = valor_total

for categoria, total in soma_por_categoria.items():
    print(f"{categoria}: {total}")