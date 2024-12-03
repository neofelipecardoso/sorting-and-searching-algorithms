def quick_sort(arr):
    num_comparisons = 0

    def partition(low, high):
        nonlocal num_comparisons
        pivot = arr[high]  # Escolhe o pivô como o último elemento
        i = low - 1
        for j in range(low, high):
            num_comparisons += 1
            if arr[j] < pivot:  # Comparando palavras em ordem alfabética
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
    return arr
