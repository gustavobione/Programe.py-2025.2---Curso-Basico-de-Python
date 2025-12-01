soma = 0
quantidade = 0

confirmacao = str(input())
while confirmacao == 's' or confirmacao == 'S':
    numero = float(input())
    soma += numero
    quantidade += 1
    confirmacao = str(input())

print(f"Você digitou {quantidade} números")
print(f"A soma final é: {soma:.2f}")