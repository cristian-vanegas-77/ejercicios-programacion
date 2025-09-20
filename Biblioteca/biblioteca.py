from libro import Libro
from estudiante import Estudiante
from prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.estudiantes = []
        self.prestamos = []

    # ---- Métodos de libros ----
    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    def buscar_libro(self, id_libro):
        for libro in self.libros:
            if libro.id_libro == id_libro:
                return libro
        return None

    # ---- Métodos de estudiantes ----
    def registrar_estudiante(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def buscar_estudiante(self, codigo):
        for est in self.estudiantes:
            if est.codigo_estudiante == codigo:
                return est
        return None

    # ---- Métodos de préstamos ----
    def registrar_prestamo(self, prestamo: Prestamo):
        libro = self.buscar_libro(prestamo.id_libro)
        if libro and libro.disponible:
            libro.disponible = False
            self.prestamos.append(prestamo)
            print(" Préstamo registrado con éxito")
        else:
            print("El libro no está disponible o no existe")
