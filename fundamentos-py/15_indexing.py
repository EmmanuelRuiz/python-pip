text = "Ella sabe python"
print(text[0])

#Cómo imprimir el último caracter
size = len(text)
print('size => ', size)
print(text[size - 1])
#Cómo imprimir el último caracter
print(text[-1])

#slicing
print(text[0:5])
print(text[10:16])
print(text[:10])#Empieza desde la posición 0
print(text[5:])#Termina hasta la última posición
print(text[::2])#Imprimir de inicio a fin la palabra, e ir saltando cada 2 espacios.
