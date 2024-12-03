def ternary_search(arr, left, right, target):
    if right >= left:
        # Calculando os dois pontos de divisão
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Verificar se o target está em mid1 ou mid2
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        # O target está na parte esquerda
        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)

        # O target está na parte direita
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)

        # O target está entre mid1 e mid2
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)

    return -1  # Se não encontrado

# Exemplo de uso:
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 15
result = ternary_search(arr, 0, len(arr) - 1, target)
print(f"Elemento encontrado no índice: {result}" if result != -1 else "Elemento não encontrado")
