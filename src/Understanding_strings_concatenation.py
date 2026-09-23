#Combinaci+on o concatenation de strings
first_name = "cesar"
last_name = "garcia"
full_name = first_name +  " " + last_name
print(full_name.title())
print(full_name.upper())

print("hola".upper(),first_name + " " + last_name)

message = "Hola," + full_name.title() + "!"
print(message)

"""
Para separar cosas se usa + para concatenation o combinacion de strings.
La , separa automaticamente variables o strings en print, No es una concatenacion.

"""
#White Space
"""
WhiteSpace se refiere a cualquier caracter que no imprime, es decir, espacio (),
tabuladores(\t) y finales de linea(\n).

Se utilizan comunmente para organizar las salidas
de texto a usuario de tal manera que sea amigable de leer o ver para usuarios.
"""

print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes: \n\tPython \n\tC++ \n\tJavaScript")

#Concatenacion de strings utilizando f-Strings
famous_person = "Gerard Way"
message = f" {famous_person} una vez dijo: python es love"
print(message)