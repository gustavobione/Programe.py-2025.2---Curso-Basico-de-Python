primeiro = int(input())
segundo = int(input())
soma = primeiro + segundo

print(f"A soma dos números é: {soma}")
print()
print("Os números pares dentro da sequência são:")
for pares in range(primeiro, segundo + 1):
    if pares % 2 == 0:
        print(pares)
print()
print("Os números ímpares dentro da sequência são:")
for impares in range(primeiro, segundo + 1):
    if impares % 2 != 0:
        print(impares)