def merge_sort(arr):
    num_comparisons = 0

    def merge(left, right):
        nonlocal num_comparisons
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            num_comparisons += 1
            if left[i] < right[j]:  # Comparando palavras em ordem alfabética
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

    return sort(arr)
