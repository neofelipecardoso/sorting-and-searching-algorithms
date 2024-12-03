# Primeiro elemento

def quick_sort_first(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort_first(less) + [pivot] + quick_sort_first(greater)

# Exemplo de uso:
arr = [10, 7, 8, 9, 1, 5]
print("Ordenado (pivô: primeiro):", quick_sort_first(arr))

# Ultimo elemento

def quick_sort_last(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    return quick_sort_last(less) + [pivot] + quick_sort_last(greater)

# Exemplo de uso:
arr = [10, 7, 8, 9, 1, 5]
print("Ordenado (pivô: último):", quick_sort_last(arr))

# elemento no meio

def quick_sort_middle(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort_middle(less) + [pivot] + quick_sort_middle(greater)

# Exemplo de uso:
arr = [10, 7, 8, 9, 1, 5]
print("Ordenado (pivô: meio):", quick_sort_middle(arr))

