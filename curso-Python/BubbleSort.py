# Definindo a lista que será ordenada
lista = [1, 2, 8, 9, 4, 7, 6, 5, 3, 10, 15, 11, 12, 13, 14, 80, 20]

# Definindo a função bubble_sort que ordena uma lista usando o algoritmo Bubble Sort
def bubble_sort(arr):
    # 'arr' é o parâmetro que representa a lista a ser ordenada
    n = len(arr)  # Obtendo o tamanho da lista
    # Loop externo para percorrer toda a lista
    for i in range(n):
        # Loop interno para comparar os elementos adjacentes
        for j in range(0, n-i-1):
            # Se o elemento atual é maior que o próximo, troque-os de lugar
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Retorna a lista ordenada
    return arr

# Chamando a função bubble_sort com a lista 'lista' e imprimindo o resultado
print(bubble_sort(lista))