lista_funcionarios = []

for i in range(10):
    cpf = input()
    nome = input()
    salario = float(input())

    dicionario_funcionario = {
        "CPF": cpf,
        "Nome": nome,
        "Salário": salario
    }

    lista_funcionarios.append(dicionario_funcionario)

media = sum(funcionario["Salário"] for funcionario in lista_funcionarios) / len(lista_funcionarios)

abaixo_media = []
acima_media = []

for funcionario in lista_funcionarios:
    if funcionario["Salário"] < media:
        abaixo_media.append(funcionario)
    elif funcionario["Salário"] > media:
        acima_media.append(funcionario)

print("Abaixo da média:")
for i in abaixo_media:
    print(f"{i['CPF']} {i['Nome']}")
print()
print("Acima da média:")
for i in acima_media:
    print(f"{i['CPF']} {i['Nome']}")