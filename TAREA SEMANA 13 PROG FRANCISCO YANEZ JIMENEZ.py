def calcular_promedio_temperaturas(temperaturas):
    promedios = {}  # Inicializa un diccionario vacío para almacenar los promedios
    for ciudad, semanas in temperaturas.items():  # Itera sobre las ciudades y sus semanas
        suma_total = 0  # Inicializa la suma total de temperaturas para la ciudad actual
        num_temperaturas = 0  # Inicializa el contador de temperaturas para la ciudad actual
        for semana in semanas:  # Itera sobre las semanas de la ciudad
            suma_total += sum(semana)  # Suma todas las temperaturas de la semana
            num_temperaturas += len(semana)  # Cuenta el número total de temperaturas en la semana
            promedio = suma_total / num_temperaturas  # Calcula el promedio de la ciudad
            promedios[ciudad] = promedio  # Almacena el promedio en el diccionario de resultados
    return promedios  # Devuelve el diccionario con los promedios de todas las ciudades

# Ejemplo de uso:
datos_temperaturas = {
  'Bogota': [[20, 22, 21, 23], [25, 24, 26, 25], [28, 27, 29, 30], [22, 21, 23, 24]],
  'Lima': [[18, 20, 19, 21], [23, 22, 24, 23], [26, 25, 27, 26], [20, 19, 21, 22]],
  'Caracas': [[22, 24, 23, 25], [27, 26, 28, 27], [30, 29, 31, 32], [24, 23, 25, 26]]
}

resultado = calcular_promedio_temperaturas(datos_temperaturas)  # Llama a la función con los datos
print(resultado)  # Imprime el resultado