# Primeiro vamos buscar o menor item na minha array

def busca_menor(array):
    menor = array[0]
    menor_indice = 0
    
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            menor_indice = i
    return menor_indice

def busca_maior(array):
    maior = array[len(array) -1]
    maior_indice = len(array) - 1
    
    for i in range(1, len(array)):
        if array[i] > maior:
            maior = array[i]
            maior_indice = i
    return maior_indice


def ordenacao_por_selecao(arr): # Ordenar do menor para o maior
    nova_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        nova_arr.append(arr.pop(menor))
    return nova_arr

def ordenacao_por_selecao_maior(arr): # Ordenar do maior para o menor
    nova_arr = []
    for i in range(len(arr)):
        maior = busca_maior(arr)
        nova_arr.append(arr.pop(maior))
    return nova_arr


arr = [2,3,4,5,1]

print(ordenacao_por_selecao_maior(arr))

