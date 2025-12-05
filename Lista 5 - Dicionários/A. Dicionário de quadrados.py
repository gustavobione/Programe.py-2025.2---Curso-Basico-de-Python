n = int(input())

dicionario_quadrados = {}

for i in range(1, n + 1):
    dicionario_quadrados[i] = i ** 2
for chave, valor in dicionario_quadrados.items():
    print(f"{chave}: {valor}")