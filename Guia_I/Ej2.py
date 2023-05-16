"""Escribir un programa que pida al usuario ingresar dos palabras y las guarde en
dos variables diferentes. Luego imprimir cual palabra tiene mas caracteres y cual
tiene menos caracteres"""

print("Ingrese las dos palabras a comparar")
a=input("Primera Palabra: ")
b=input("Segunda Palabra: ")

c=len(a)
d=len(b)
if c>d:
   print("La primera palabra tiene mas caracteres",c)
else:
    print("La seginda palabra tiene mas caracteres",d)