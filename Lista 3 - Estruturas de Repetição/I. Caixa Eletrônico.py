saldo = float(input())
operacao = str(input())

saldo_anterior = saldo
saldo_atual = saldo

while operacao != 'sair':
    valor = float(input())

    if operacao == 'depositar':
        saldo_atual += valor  
    elif operacao == 'sacar':
        saldo_atual -= valor 
        
    operacao = str(input())

print(f"Seu saldo era: R$ {saldo_anterior:.2f}")
print(f"Seu novo saldo é: R$ {saldo_atual:.2f}")