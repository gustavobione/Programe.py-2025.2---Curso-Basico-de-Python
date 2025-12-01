elementos = str(input()).split()
soma = 0
for i in range(len(elementos)):
    soma += float(elementos[i])
media = soma / len(elementos)
quantidade_maiores = 0
for j in range(len(elementos)):
    if float(elementos[j]) > media:
        quantidade_maiores += 1
print(f"{quantidade_maiores}")