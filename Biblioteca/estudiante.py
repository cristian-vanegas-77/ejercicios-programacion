class Estudiante:
    def __init__(self, codigo_estudiante, nombres, apellidos):
        self.codigo_estudiante = codigo_estudiante
        self.nombres = nombres
        self.apellidos = apellidos

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.codigo_estudiante})"
