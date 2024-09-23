#Creamos un Diccionario
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "nacionalidad": "Ecuatoriana",
    "fecha_nacimiento": "1993-05-15",
    "discapacidad": False,
    "ciudad": "Guaranda",
    "profesion": "Ingeniero"
}

#Acceder y Modificar Valores
#Accedemos al valor de la clave "ciudad"
ciudad_actual = informacion_personal["ciudad"]
print(f"Ciudad actual: {ciudad_actual}")

#Modificamos el valor de "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

#Agregamos una nueva clave-valor para la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"

#Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    # Si "telefono" no existe, lo agregamos con un número ficticio
    informacion_personal["telefono"] = "0991234567"

# Eliminamos la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]

#Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)
