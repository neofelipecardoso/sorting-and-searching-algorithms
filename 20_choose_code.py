import time

# Algoritmos de Ordenação

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr  # Garantir que a lista ordenada seja retornada

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr  # Garantir que a lista ordenada seja retornada

# Bucket Sort
def bucket_sort(arr):
    # Criar 10 "baldes" para números de 0 a 100
    buckets = [[] for _ in range(101)]
    
    # Distribuir os números nos baldes
    for num in arr:
        if 0 <= num <= 100:
            buckets[num].append(num)
    
    # Ordenar cada balde e concatenar o resultado
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr # Garantir que a lista ordenada seja retornada

# Radix Sort
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

# Algoritmos de Busca

# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Interpolation Search
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] != arr[high]:
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    if arr[low] == target:
        return low
    return -1

# Jump Search
def jump_search(arr, target):
    n = len(arr)
    step = int(n ** 0.5)
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(n ** 0.5)
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Exponential Search
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i = i * 2
    return binary_search(arr[:min(i, len(arr))], target)

# Ternary Search
def ternary_search(arr, target):
    low, high = 0, len(arr) - 1
    while high >= low:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1

# Função para medir o tempo de execução de um algoritmo
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# Função principal do programa
def main():
    print("Elementos da lista: [22, 55, 10, 88, 4, 32, 66, 99, 45, 71]")
    # Usar uma lista fixa de exemplo
    arr = [22, 55, 10, 88, 4, 32, 66, 99, 45, 71]
    
    # Escolha do algoritmo de ordenação
    print("\nEscolha um algoritmo de ordenação:")
    print("1. Merge Sort")
    print("2. Quick Sort")
    print("3. Selection Sort")
    print("4. Bucket Sort")
    print("5. Radix Sort")
    choice_sort = int(input("Digite o número do algoritmo escolhido: "))

    # Ordenar a lista com o algoritmo escolhido
    if choice_sort == 1:
        sorted_arr, time_merge = measure_time(merge_sort, arr.copy())
    elif choice_sort == 2:
        sorted_arr, time_quick = measure_time(quick_sort, arr.copy())
    elif choice_sort == 3:
        sorted_arr, time_selection = measure_time(selection_sort, arr.copy())
    elif choice_sort == 4:
        sorted_arr, time_bucket = measure_time(bucket_sort, arr.copy())
    elif choice_sort == 5:
        sorted_arr, time_radix = measure_time(radix_sort, arr.copy())
    else:
        print("Opção inválida.")
        return

    print(f"\nLista ordenada: {sorted_arr}")
    print(f"Tempo de execução: {round(time_merge, 5)} segundos" if choice_sort == 1 else 
          f"Tempo de execução: {round(time_quick, 5)} segundos" if choice_sort == 2 else 
          f"Tempo de execução: {round(time_selection, 5)} segundos" if choice_sort == 3 else
          f"Tempo de execução: {round(time_bucket, 5)} segundos" if choice_sort == 4 else
          f"Tempo de execução: {round(time_radix, 5)} segundos")

    # Escolha do algoritmo de busca
    print("\nEscolha um algoritmo de busca:")
    print("1. Binary Search")
    print("2. Interpolation Search")
    print("3. Jump Search")
    print("4. Exponential Search")
    print("5. Ternary Search")
    choice_search = int(input("Digite o número do algoritmo escolhido: "))
    target = int(input("Digite o número a ser buscado: "))

    # Realizar a busca com o algoritmo escolhido
    if choice_search == 1:
        result, time_bin = measure_time(binary_search, sorted_arr, target)
    elif choice_search == 2:
        result, time_interp = measure_time(interpolation_search, sorted_arr, target)
    elif choice_search == 3:
        result, time_jump = measure_time(jump_search, sorted_arr, target)
    elif choice_search == 4:
        result, time_exp = measure_time(exponential_search, sorted_arr, target)
    elif choice_search == 5:
        result, time_tern = measure_time(ternary_search, sorted_arr, target)
    else:
        print("Opção inválida.")
        return

    # Resultado da busca
    if result != -1:
        print(f"\nÍndice do número {target}: {result}")
    else:
        print(f"\nNúmero {target} não encontrado.")
    
    print(f"Tempo de execução: {round(time_bin, 5)} segundos" if choice_search == 1 else
          f"Tempo de execução: {round(time_interp, 5)} segundos" if choice_search == 2 else
          f"Tempo de execução: {round(time_jump, 5)} segundos" if choice_search == 3 else
          f"Tempo de execução: {round(time_exp, 5)} segundos" if choice_search == 4 else
          f"Tempo de execução: {round(time_tern, 5)} segundos")

if __name__ == "__main__":
    main()
