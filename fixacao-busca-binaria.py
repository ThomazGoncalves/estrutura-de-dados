def busca_binaria(lista,item):
    menor = 0
    maior = len(lista) - 1

    while menor <= maior:
        meio = (menor + maior) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            maior = meio - 1
        else:
            menor = menor + 1
    return None

lista = [3,5,6,7,8,9]

print(busca_binaria(lista, 5))