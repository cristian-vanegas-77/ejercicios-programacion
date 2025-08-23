from datetime import date
from libro import Libro
from estudiante import Estudiante
from prestamo import Prestamo
from biblioteca import Biblioteca

if __name__ == "__main__":
    # Crear biblioteca
    biblioteca = Biblioteca()

    # Agregar libros
    libro1 = Libro(1, "Cien años de soledad", "Gabriel García Márquez")
    libro2 = Libro(2, "El Principito", "Antoine de Saint-Exupéry")
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Registrar estudiante
    estudiante1 = Estudiante("E001", "Cristian", "Vanegas")
    biblioteca.registrar_estudiante(estudiante1)

    # Registrar préstamo
    prestamo1 = Prestamo(1, 1, "E001", date.today(), date(2025, 9, 1))
    biblioteca.registrar_prestamo(prestamo1)

    # Mostrar datos
    print("\n Libros en biblioteca:")
    for l in biblioteca.libros:
        print(l)

    print("\n Estudiantes registrados:")
    for e in biblioteca.estudiantes:
        print(e)

    print("\n Préstamos realizados:")
    for p in biblioteca.prestamos:
        print(p)
