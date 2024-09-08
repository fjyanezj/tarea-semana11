# Definimos las dimensiones de la matriz
ciudades = 3  # Ejemplo: 3 ciudades
dias_semana = 7  # Lunes a Domingo
semanas = 2  # Ejemplo: 2 semanas

# Creamos una matriz 3D con temperaturas aleatorias
import random

# Generar la matriz 3D
temperaturas = [[[random.randint(15, 35) for _ in range(dias_semana)] for _ in range(semanas)] for _ in range(ciudades)]

# Imprimir la matriz generada
for ciudad in range(ciudades):
    print(f"Ciudad {ciudad + 1}:")
    for semana in range(semanas):
        print(f"  Semana {semana + 1}: {temperaturas[ciudad][semana]}")
    print()

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for ciudad in range(ciudades):
    print(f"Promedio de temperaturas para la Ciudad {ciudad + 1}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(dias_semana):
            suma_temperaturas += temperaturas[ciudad][semana][dia]
        promedio = suma_temperaturas / dias_semana
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()
