lista_produtos = []

for i in range(5):
    nome_produto_input = input() 
    preco_compra_input = float(input())
    percentual_lucro_input = float(input())

    preco_venda_calculado = preco_compra_input + (preco_compra_input * percentual_lucro_input / 100)
    lista_produtos.append([nome_produto_input, preco_compra_input, preco_venda_calculado])

for item in lista_produtos:
    nomes_produto = item[0]
    preco_compra = item[1]
    preco_venda = item[2]

    print(f"{nomes_produto}: Compra = R${preco_compra:.2f}, Venda = R${preco_venda:.2f}")