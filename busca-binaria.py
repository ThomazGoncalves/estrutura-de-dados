# A busca binária pega uma array(lista ordenada) e um item (o elemento escolhido para ser encontrado na array) 

# se o item estiver na array, a função retorna sua posição(indice) dessa maneira você é capaz de saber por qual ponto da lista deve continuar procurando 

def pesquisa_binaria(lista, item): #lista ordenada
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:

        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio -1
        else:
            baixo = meio + 1
    return None

lista = [1, 3, 5, 7]

print(pesquisa_binaria(lista, 7))
