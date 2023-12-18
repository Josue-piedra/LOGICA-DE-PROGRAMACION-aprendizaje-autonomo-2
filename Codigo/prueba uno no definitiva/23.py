#Ejericicio 1: Escribir un programa que solicite al usuario las asignaturas que está tomando  y las almacene en una lista.
#El programa debe Imprimir: Bienvenido <nombre del usuario><nombre del usuario> esta estudiando <asignatura>

#donde:<nombre del usuario> Es el nombre del estudiante <asignatura> es cada una de las asignaturas de la lista.

# Solicitar al usuario su nombre
nombre_usuario = input("Ingrese su nombre: ")

# Crear una lista vacía para almacenar las asignaturas
asignaturas = []

# Solicitar al usuario las asignaturas que está tomando, separadas por comas
asignaturas_input = input("Ingrese las asignaturas que está tomando, separadas por comas: ")

# Dividir la entrada del usuario en una lista de asignaturas
asignaturas = asignaturas_input.split(',')

# Imprimir el mensaje de bienvenida y las asignaturas
print(f"Bienvenido {nombre_usuario}")
print(f"{nombre_usuario} está estudiando las siguientes asignaturas:")

# Iterar sobre la lista de asignaturas e imprimir cada una
for asignatura in asignaturas:
    print(asignatura.strip())  # strip() elimina espacios en blanco al inicio y al final de cada asignatura