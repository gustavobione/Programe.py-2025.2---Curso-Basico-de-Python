n1 = float(input())
n2 = float(input())
n3 = float(input())

def calcular_media(a, b, c):
    media = (a + b + c) / 3
    return media

print(f"{calcular_media(n1, n2, n3):.2f}")