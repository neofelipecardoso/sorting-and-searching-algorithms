def interpolation_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right and target >= arr[left] and target <= arr[right]:
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1  # O alvo está à direita
        else:
            right = pos - 1  # O alvo está à esquerda
    return -1  
