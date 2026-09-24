#Eliminación de espacios en blanco
programming_lenguaje = "    python      "

print("variable original efecto")
print(programming_lenguaje)
print("efecto del lstrip")
print(programming_lenguaje.lstrip())#Te quita los espacios de la izquierda pero deja los de la derecha
print("efecto del rstrip")
print(programming_lenguaje.rstrip())#Te quita los espacios de la derecha pero deja los de la izquierda
print(programming_lenguaje.strip())#Te quita todos los espacios

#Error de sintaxis

message = 'una fortaleza de python es su comunidad'
print(message)
message = 'una fortaleza de "python" es su comunidad'
print(message)

"""
si es un error de sintaxis el codigo no lee linea por linea si 
no que lo da directamente.
"""
