# Definimos la matriz bidimensional (3x3)
matriz = [
    [99, 4, 7],
    [21, 5, 1],
    [82, 8, 3]      ]

# Funci�n para ordenar una fila espec�fica utilizando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
# Intercambia los elementos si est�n en el orden incorrecto
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 0
ordenar_fila(matriz, fila_a_ordenar)
# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
