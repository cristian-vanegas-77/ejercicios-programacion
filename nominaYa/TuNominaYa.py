from abc import ABC, abstractmethod

# Clase abstracta
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario(self):
        pass

# -------------------------------
# Subclases
# -------------------------------

# 1. Empleado asalariado (sueldo fijo)
class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, salario_semanal):
        super().__init__(nombre)
        self.salario_semanal = salario_semanal

    def calcular_salario(self):
        return self.salario_semanal

# 2. Empleado por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        if self.horas_trabajadas <= 40:
            return self.horas_trabajadas * self.tarifa_por_hora
        else:
            horas_extra = self.horas_trabajadas - 40
            return (40 * self.tarifa_por_hora) + (horas_extra * self.tarifa_por_hora * 1.5)

# 3. Empleado por comisión
class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, ventas, tarifa_comision):
        super().__init__(nombre)
        self.ventas = ventas
        self.tarifa_comision = tarifa_comision

    def calcular_salario(self):
        return self.ventas * self.tarifa_comision

# 4. Empleado con salario base + comisión
class EmpleadoBaseMasComision(EmpleadoPorComision):
    def __init__(self, nombre, ventas, tarifa_comision, salario_base):
        super().__init__(nombre, ventas, tarifa_comision)
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base + super().calcular_salario()

# -------------------------------
# Programa de prueba (Sesión 1)
# -------------------------------
if __name__ == "__main__":
    empleados = [
        EmpleadoAsalariado("Ana", 500),
        EmpleadoPorHoras("Luis", 45, 10),
        EmpleadoPorComision("Carla", 10000, 0.06),
        EmpleadoBaseMasComision("Pedro", 5000, 0.04, 300)
    ]

    # Polimorfismo: mismo método, diferente comportamiento
    for emp in empleados:
        print(f"{emp.nombre} gana: ${emp.calcular_salario():.2f}")
