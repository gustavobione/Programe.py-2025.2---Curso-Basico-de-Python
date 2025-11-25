salário = float(input())
horas_por_dia = int(input())
dias_trabalhados = int(input())
valor_hora = salário / (horas_por_dia * dias_trabalhados)

print(f"Eu recebo uma mixuruca de R$ {valor_hora:.1f} por hora trabalhada.")