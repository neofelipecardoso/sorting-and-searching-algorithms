class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f"{self.nome}: {self.nota}"

# Função Bucket Sort para ordenar as notas dos alunos
def bucket_sort(alunos):
    # Criando os "baldes" (buckets) para as notas de 0 a 100
    num_buckets = 10  # 10 baldes para as notas de 0 a 100
    max_nota = 100
    min_nota = 0
    interval = (max_nota - min_nota) // num_buckets + 1

    # Inicializa os baldes
    buckets = [[] for _ in range(num_buckets)]

    # Distribui os alunos para os baldes baseados nas suas notas
    for aluno in alunos:
        index = (aluno.nota - min_nota) // interval
        buckets[index].append(aluno)

    # Ordena cada balde e concatena os resultados
    alunos_ordenados = []
    for bucket in buckets:
        alunos_ordenados.extend(sorted(bucket, key=lambda aluno: aluno.nota))

    return alunos_ordenados

# Função Interpolation Search para encontrar um aluno pela nota
def interpolation_search(alunos, nota):
    low = 0
    high = len(alunos) - 1

    while low <= high and nota >= alunos[low].nota and nota <= alunos[high].nota:
        if low == high:
            if alunos[low].nota == nota:
                return alunos[low]
            return None

        # Estimando a posição usando a fórmula de interpolação
        pos = low + ((nota - alunos[low].nota) * (high - low)) // (alunos[high].nota - alunos[low].nota)

        # Verifica se a posição estimada é a que estamos procurando
        if alunos[pos].nota == nota:
            return alunos[pos]
        elif alunos[pos].nota < nota:
            low = pos + 1
        else:
            high = pos - 1

    return None

# Exemplo de uso
# Lista de alunos com notas entre 0 e 100
alunos = [
    Aluno("Alice", 85),
    Aluno("Bob", 72),
    Aluno("Charlie", 92),
    Aluno("Diana", 67),
    Aluno("Eve", 78),
    Aluno("Frank", 88),
    Aluno("Grace", 91),
    Aluno("Hank", 74)
]

# Ordenando os alunos por suas notas usando Bucket Sort
alunos_ordenados = bucket_sort(alunos)
print("Alunos ordenados por nota:")
for aluno in alunos_ordenados:
    print(aluno)

# Procurando um aluno com uma nota específica usando Interpolation Search
nota_procurada = 92
aluno_encontrado = interpolation_search(alunos_ordenados, nota_procurada)

if aluno_encontrado:
    print(f"\nAluno com nota {nota_procurada} encontrado: {aluno_encontrado}")
else:
    print(f"\nNenhum aluno com nota {nota_procurada} encontrado.")
