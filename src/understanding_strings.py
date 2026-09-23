"""
Un string es de manera sencilla una serie de caracteres.

En python todo lo que se encuentre dentro de comillas simples ''
o dobles comillas "" es considerado String.
'le dije a un enemigo, "python es mi lenguaje favorito"'
" el lenguaje 'Python' llev el nombre por Monty Python, no por la serpiente"

"esto es un string"
'esto es un string'
"""
name = "clase de programacion"
print(name)

print(name.title()) #hace cada primera letra mayuscula y las demas minusculas.

name = name.title()
print(name)

"""
Un método es una acción que
python puede realizar en un fragmento de datos o sobre una variable.
El punto . despues de una variable, seguido de un metodo
title() dice que tiene que ejecutar
title() de la variable name.

Todos los metodos van seguidos de un parentesis 
porque en ocasiones necesitan información
adicional para funcionar, lo cual estaria
dentro de los paréntesis. En esta ocasión el metodo title()
no requiere informacion adicional para funcionar.
"""
#otros metodos
print(name.upper()) # hace mayusculas todas las letras
print(name.lower()) # hace minusculas todas las letras

# No poner NADA dentro de los parentesis de los métodos