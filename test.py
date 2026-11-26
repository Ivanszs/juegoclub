from obj.cliente import Cliente
from obj.juego import Juego
from obj.alquiler import Alquiler

cli1 = Cliente("Juan", "Perez", "38123456", "1145678901", 1)
print("--- Datos del Cliente ---")
cli1.mostrarDatos()

print("")
jue1 = Juego("Monopoly", "Estrategia", 1500.0, 1)
print("--- Datos del Juego ---")
jue1.mostrarDatos()

print("")
alq1 = Alquiler(cli1, jue1, 3, 1)
print("--- Datos del Alquiler ---")
alq1.mostrarDatos()
print("Total con descuento de $500: $", alq1.calcularTotal(500))
