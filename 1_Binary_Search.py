def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # O alvo está na metade direita
        else:
            right = mid - 1  # O alvo está na metade esquerda
    return -1  


arr = [1,2,3,4,5,6,7]
target= 7

print(binary_search(arr,target)) # retorna o valor na posição do array, logo começa no 0, não no 1. Por isso vai retornar, nesse caso, 6
