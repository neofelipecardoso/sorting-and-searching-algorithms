def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:  # Palavra encontrada
            return True
        elif arr[mid] < target:  # Palavra está à direita
            low = mid + 1
        else:  # Palavra está à esquerda
            high = mid - 1
    return False  # Palavra não encontrada
