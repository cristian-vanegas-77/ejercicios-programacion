class Prestamo:
    def __init__(self, id_prestamo, id_libro, codigo_estudiante, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.id_libro = id_libro
        self.codigo_estudiante = codigo_estudiante
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def __str__(self):
        return (f"Préstamo {self.id_prestamo}: Libro {self.id_libro} "
                f"a estudiante {self.codigo_estudiante} "
                f"del {self.fecha_prestamo} hasta {self.fecha_devolucion}")
