lista = str(input()).split()
lista_telefonica = {}

while lista != ["fim"]:
    nome = lista[0].lower()
    numero = lista[1]
    lista_telefonica[nome] = numero
    lista = str(input()).split()

nome = str(input())

if nome.lower() in lista_telefonica:
    print(lista_telefonica[nome.lower()])
else:
    print("Essa pessoa não está na lista telefônica")