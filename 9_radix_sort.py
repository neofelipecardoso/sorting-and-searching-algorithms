def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # Lista de saída
    count = [0] * 10  # Contagem de dígitos (0-9)

    # Contar a frequência dos dígitos
    for num in arr:
        index = num // exp
        count[index % 10] += 1

    # Ajuste na lista de contagem para ter a posição correta
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construção do array de saída
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # Copiar o conteúdo de output de volta para arr
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Encontrar o maior número
    max_num = max(arr)

    # Realizar counting sort para cada dígito
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Exemplo de uso:
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Lista ordenada:", arr)
