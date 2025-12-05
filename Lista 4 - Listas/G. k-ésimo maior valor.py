t = int(input())

lista = []

for _ in range(t):
    n = int(input())
    lista.append(n)

k = int(input())
lista.sort()

print(lista[k])