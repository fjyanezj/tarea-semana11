# ESTUDIANTE FRANCISCO YANEZ JIMENEZ SEMESTRE 1 PARALELO C
# Definimos la matriz bidimensional (3x3)
matriz = [
    [1, 2, 31],
    [4, 5, 62],
    [7, 8, 93]              ]
# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Valor que deseamos buscar
valor_a_buscar = 5

# Realizar la búsqueda
posicion = buscar_valor(matriz, valor_a_buscar)
if posicion:
    print(f"Valor {valor_a_buscar} encontrado en la posición: {posicion}")
else:
    print(f"Valor {valor_a_buscar} no se encontró en la matriz.")
