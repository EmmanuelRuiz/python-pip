#listas, en inglés es lists
#Tiene bastantes funcionalidades para almacenar información,
#almacenan más de un tipo de dato.


numbers = [1, 3, 5, 6]
print(numbers)
print(type(numbers))

tasks = ['programar', 'estudiar']
print(tasks)

types = [1, True, 'hola']

#acceder  a un elemento de la lista
print(tasks[0])

#cambiar el contenido de una posición de una lista
tasks[0] = "jugar"
print(tasks)

#usar técnica de slicing para imprimir
print(numbers[1:3])

#también podemos saber si hay algún elemento en una lista
print(True in types)
