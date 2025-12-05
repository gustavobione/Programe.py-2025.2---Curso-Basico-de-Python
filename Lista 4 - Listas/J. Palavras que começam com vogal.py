lista = []

palavra = str(input())

while palavra != "fim":
    lista.append(palavra)
    palavra = str(input())

for elemento in lista:
    if elemento[0].lower() in 'aeiou':
        print(elemento)

if not any(elemento[0].lower() in 'aeiou' for elemento in lista):
    print("Nenhuma palavra digitada começa com vogal.")