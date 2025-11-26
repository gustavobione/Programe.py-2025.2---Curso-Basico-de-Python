nome = str(input())
sobrenome = str(input())
idade = int(input())
nome_completo = f"{nome} {sobrenome}"

if idade < 12:
    print(f"A categoria do atleta {nome_completo} é a infantil.")
elif 12 <= idade < 18:
    print(f"A categoria do atleta {nome_completo} é a juvenil.")
elif 18 <= idade < 36:
    print(f"A categoria do atleta {nome_completo} é a adulta.")
else:
    print(f"A categoria do atleta {nome_completo} é a master.")