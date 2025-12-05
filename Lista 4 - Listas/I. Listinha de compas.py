itens = []
item = str(input())

while item != "fim":
    itens.append(item)
    item = str(input())

itens.sort()

for elemento in itens:
    print(elemento)