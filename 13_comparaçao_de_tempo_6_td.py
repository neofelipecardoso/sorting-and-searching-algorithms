import random
import time

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    num_comparisons = 0

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                num_comparisons += 1
            arr[j] = temp
        gap //= 2

    return num_comparisons

def merge_sort(arr):
    num_comparisons = 0

    def merge(left, right):
        nonlocal num_comparisons
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            num_comparisons += 1
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    return num_comparisons

def selection_sort(arr):
    num_comparisons = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            num_comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return num_comparisons

def quick_sort(arr):
    num_comparisons = 0

    def partition(low, high):
        nonlocal num_comparisons
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            num_comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)
            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(arr) - 1)
    return num_comparisons

def bucket_sort(arr):
    num_comparisons = 0
    n = len(arr)
    if n == 0:
        return num_comparisons

    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / n
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    for i in range(n):
        buckets[i].sort()
        num_comparisons += len(buckets[i]) * (len(buckets[i]) - 1) // 2  # Approximation

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return num_comparisons

def radix_sort(arr):
    num_comparisons = 0
    def counting_sort(arr, exp):
        nonlocal num_comparisons
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            num_comparisons += 1
            count[(arr[i] // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            num_comparisons += 1
            output[count[(arr[i] // exp) % 10] - 1] = arr[i]
            count[(arr[i] // exp) % 10] -= 1

        for i in range(n):
            arr[i] = output[i]

    def sort(arr):
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            counting_sort(arr, exp)
            exp *= 10

    sort(arr)
    return num_comparisons

def measure_time_and_comparisons(sort_function, arr):
    start_time = time.time()
    comparisons = sort_function(arr)
    end_time = time.time()
    return end_time - start_time, comparisons

# Lista de tamanhos
sizes = [1000, 5000, 10000]

# Exemplo de execução para diferentes tamanhos de lista
for size in sizes:
    arr = random.sample(range(size * 10), size)  # Lista aleatória
    print(f"Para a lista de tamanho {size}:")
    
    # Shell Sort
    arr_copy = arr[:]
    time_taken, comparisons = measure_time_and_comparisons(shell_sort, arr_copy)
    print(f"Shell Sort - Tempo: {time_taken:.6f}s, Comparações: {comparisons}")

    # Merge Sort
    arr_copy = arr[:]
    time_taken, comparisons = measure_time_and_comparisons(merge_sort, arr_copy)
    print(f"Merge Sort - Tempo: {time_taken:.6f}s, Comparações: {comparisons}")

    # Selection Sort
    arr_copy = arr[:]
    time_taken, comparisons = measure_time_and_comparisons(selection_sort, arr_copy)
    print(f"Selection Sort - Tempo: {time_taken:.6f}s, Comparações: {comparisons}")

    # Quick Sort
    arr_copy = arr[:]
    time_taken, comparisons = measure_time_and_comparisons(quick_sort, arr_copy)
    print(f"Quick Sort - Tempo: {time_taken:.6f}s, Comparações: {comparisons}")

    # Bucket Sort
    arr_copy = arr[:]
    time_taken, comparisons = measure_time_and_comparisons(bucket_sort, arr_copy)
    print(f"Bucket Sort - Tempo: {time_taken:.6f}s, Comparações: {comparisons}")

    # Radix Sort
    arr_copy = arr[:]
    time_taken, comparisons = measure_time_and_comparisons(radix_sort, arr_copy)
    print(f"Radix Sort - Tempo: {time_taken:.6f}s, Comparações: {comparisons}")

    print("\n")


