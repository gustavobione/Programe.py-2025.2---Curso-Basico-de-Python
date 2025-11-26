caractere = str(input())


if caractere.isnumeric():
    print("O caractere é um número")
elif caractere.lower() in ['+', '-', '*', '/']:
    print("O caractere é uma operação matemática")
else:
    print("O caractere é uma vogal")