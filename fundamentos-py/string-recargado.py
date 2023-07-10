text = 'Las rosas son rojas'

'''ver si una palabra está en un texto.'''
if "rojas" in text:
    print('Si, son rojas')


'''contar tamaño de caracteres de un texto.'''
size = len(text)
print(size)

'''cambiar texto a mayus.'''
print(text.upper())
'''cambiar texto a minus.'''
print(text.lower())
'''contar cuántas veces se repite un caracter en una variable.'''
print(text.count('a'))
'''cambiar mayuscula a minus y viceversa.'''
print(text.swapcase()) 

'''verificar si un texto empieza con una palabra '''
print(text.startswith("Las rosas"))
'''verificar si un texto termina con una palabra '''
print(text.endswith("Negras"))
'''reemplazar una palabra por otra palabra '''
print(text.replace('rosas', 'tabla'))

'''Poner el primer caracter en mayuscula '''
print(text.capitalize())

'''Poner el inicio de cada palabra de la oración en mayus '''
print(text.title())

'''evaluar si la var. es un digito '''
print(text.isdigit())

'''aquí imprime true a pesar que es un string '''
print("333".isdigit())




