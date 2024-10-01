#TAREA PROG S16 FRANCISCO YANEZ JIMENEZ
#ESCRIBIENDO UN ARCHIVO DE TEXTO
# Escritura de Archivo de Texto

# Abrimos un archivo llamado my_notes.txt en modo de escritura ("w")
with open('my_notes.txt', 'w') as file:
    # Escribe tres l�neas de notas personales en el archivo
    file.write(" nota1: Estoy aprendiendo a leer y escribir archivos en Python.\n")
    file.write("Segunda nota: La pr�ctica es fundamental para mejorar las habilidades de programaci�n.\n")
    file.write("Tercera nota: Recordar siempre cerrar los archivos despu�s de usarlos.\n")
# El archivo se cierra autom�ticamente al salir del bloque 'with'

# Lectura de Archivo de Texto

# Abre el archivo 'my_notes.txt' en modo de lectura ("r")
with open('my_notes.txt', 'r') as file:
    # Lee el archivo l�nea por l�nea utilizando readline() y muestra cada l�nea en la consola
    linea = file.readline()
    while linea:
        print(linea.strip())  # .strip() elimina el salto de l�nea adicional al imprimir
        linea = file.readline()
# El archivo se cierra autom�ticamente al salir del bloque 'with' 