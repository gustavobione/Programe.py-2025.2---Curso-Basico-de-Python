numero = float(input())
expoente = int(input())

def elevar_a_potencia(base, exp):
    resultado = base ** exp
    return resultado

print(f"{elevar_a_potencia(numero, expoente):.2f}")