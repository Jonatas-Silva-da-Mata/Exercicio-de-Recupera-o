def ordenar_livros():
    lista_livro = {}
    lista_ordenada = {}

    quantidade = int(input('Quantos livros você deseja adicionar: '))

    for i in range(quantidade):
        nome_livro = input('Digite o nome do livro: ')
        posicao_livro = input('Posição que este livro ocupa: ')
        lista_livro[nome_livro] = posicao_livro

    for i in sorted(lista_livro, key=lista_livro.get):
        lista_ordenada[i] = lista_livro[i]

    return lista_ordenada

print(ordenar_livros())
