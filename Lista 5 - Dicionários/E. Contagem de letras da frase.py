frase = str(input())

dicionario_contagem = {}

for letra in frase:
    if letra.isalpha():
        letra_minuscula = letra.lower()
        if letra_minuscula in dicionario_contagem:
            dicionario_contagem[letra_minuscula] += 1
        else:
            dicionario_contagem[letra_minuscula] = 1

for letra, contagem in sorted(dicionario_contagem.items()):
    print(f"{letra.upper()}: {contagem}")