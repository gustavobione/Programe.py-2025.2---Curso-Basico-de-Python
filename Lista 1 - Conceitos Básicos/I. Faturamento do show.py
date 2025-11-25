Quantidade_ingressos = int(input())
percentual_meia_entrada = int(input())
valor_ingresso = float(input())

total_meia = Quantidade_ingressos * (percentual_meia_entrada / 100)
total_inteira = Quantidade_ingressos - total_meia
faturamento_meia = total_meia * (valor_ingresso / 2)
faturamento_inteira = total_inteira * valor_ingresso
faturamento_total = faturamento_meia + faturamento_inteira

print(f"Quantidade de ingressos meia-entrada: {total_meia:.0f}")
print(f"Quantidade de ingressos inteiros: {total_inteira:.0f}")
print(f"Faturamento com meia-entrada: R${faturamento_meia:.2f}")
print(f"Faturamento com inteira: R${faturamento_inteira:.2f}")
print(f"Faturamento total: R${faturamento_total:.2f}")