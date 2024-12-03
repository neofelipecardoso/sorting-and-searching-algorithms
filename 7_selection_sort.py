def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar o índice do menor elemento
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Trocar o elemento mínimo com o elemento na posição i
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Lista ordenada:", arr)
