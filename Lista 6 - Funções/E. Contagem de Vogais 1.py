word = str(input())

def contar_vogais(palavra):
    vogais = 'aeiouAEIOU'
    contagem = 0
    for letra in palavra:
        if letra in vogais:
            contagem += 1
    return contagem

print(f"A quantidade de vogais em {word} é {contar_vogais(word)}")