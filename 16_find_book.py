class Livro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __repr__(self):
        return f"{self.titulo} ({self.isbn})"

# Função de Binary Search para procurar por ISBN
def binary_search_livros(livros, isbn):
    low, high = 0, len(livros) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if livros[mid].isbn == isbn:  # ISBN encontrado
            return livros[mid]
        elif livros[mid].isbn < isbn:  # ISBN está à direita
            low = mid + 1
        else:  # ISBN está à esquerda
            high = mid - 1
    return None  # ISBN não encontrado

# Lista de livros (não ordenada)
livros = [
    Livro(9780143127796, "A Arte da Guerra", "Sun Tzu"),
    Livro(9780439139601, "Harry Potter e a Pedra Filosofal", "J.K. Rowling"),
    Livro(9780199535569, "Orgulho e Preconceito", "Jane Austen"),
    Livro(9780061122415, "O Sol é para Todos", "Harper Lee"),
    Livro(9780451524935, "1984", "George Orwell")
]

# Ordenando os livros por ISBN
livros.sort(key=lambda livro: livro.isbn)

# Procurando um livro pelo ISBN usando Binary Search
isbn_procurado = 9780061122415
livro_encontrado = binary_search_livros(livros, isbn_procurado)

# Exibindo o resultado
if livro_encontrado:
    print(f"Livro encontrado: {livro_encontrado}")
else:
    print("Livro não encontrado.")
