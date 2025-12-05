n = str(input())
dicionario_agrupado = {}

while n != "fim":

    primeira_letra = n[0].lower()

    if primeira_letra not in dicionario_agrupado:
        dicionario_agrupado[primeira_letra] = [n]
    else:
        dicionario_agrupado[primeira_letra].append(n)
    
    n = str(input())

for letra, nomes in sorted(dicionario_agrupado.items()):
    print(f"{letra.upper()}: {' '.join(nomes)}")