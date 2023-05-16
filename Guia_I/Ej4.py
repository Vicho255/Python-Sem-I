"""Elaborar un algoritmo que solicite al usuario su nombre y el nombre de otra
persona. Luego, mostrar en pantalla un mensaje que indique si ambos nombres
comienzan con la misma letra o si terminan con la misma letra, o si difieren tanto
en la letra inicial como en la final."""

a=input("Primer Nombre:\n")
b=input("Segundo Nombre:\n")

a1=list(a)
b1=list(b)

"""
print(a1[0])
print(a1[c])
print(b1[0])
print(b1[d])
"""

if a1[0]==b1[0]:
    print("La primera letra es igual")
elif a1[-1]==b1[-1]:
    print("La ultima letra es la igual")
else:
    print("Ninguna letra es igual")