elementos = str(input()).split()

k = int(input())

for item in elementos:
    valor = int(item)
    resultado = valor * k

    print(resultado, end=' ')