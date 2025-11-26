n1 = float(input())
n2 = float(input())
operacao = str(input())

if operacao == '+':
    print(f"Você escolheu a operação de adição. O resultado dessa adição é {n1 + n2:.2f}")
elif operacao == '-':
    print(f"Você escolheu a operação de subtração. O resultado dessa subtração é {n1 - n2:.2f}")
elif operacao == '*':
    print(f"Você escolheu a operação de multiplicação. O resultado dessa multiplicação é {n1 * n2:.2f}")
elif operacao == '/':
    print(f"Você escolheu a operação de divisão. O resultado dessa divisão é {n1 / n2:.2f}")