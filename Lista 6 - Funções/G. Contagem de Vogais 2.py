word = str(input())

def contar_vogais(texto):
    resultado = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in texto:
        letra_minuscula = letra.lower()

        if letra_minuscula in resultado:
            resultado[letra_minuscula] += 1
            
    return resultado

print(contar_vogais(word))