class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} - {self.autor} (Disponible: {self.disponible})"
