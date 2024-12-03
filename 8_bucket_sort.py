def bucket_sort(arr):
    # Criar baldes
    n = len(arr)
    if n == 0:
        return arr
    # Determina o intervalo para cada balde
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / n

    # Inicializar os baldes
    buckets = [[] for _ in range(n)]

    # Colocar cada número no balde correspondente
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == n:  # Tratar o caso do número ser o maior valor
            index -= 1
        buckets[index].append(num)

    # Ordenar os baldes e concatenar os resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))  # Pode usar outro algoritmo aqui, como Insertion Sort.

    return sorted_arr

# Exemplo de uso:
arr = [0.42, 0.32, 0.23, 0.51, 0.12]
sorted_arr = bucket_sort(arr)
print("Lista ordenada:", sorted_arr)
