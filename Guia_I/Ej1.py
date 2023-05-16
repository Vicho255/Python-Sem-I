"""Realizar un algoritmo que indique el numero menor y el numero mayor entre tres enteros leidos por consola. 
Solo se deben ingresar numeros enteros"""

a=input(int)
b=input(int)
c=input(int)

if a.isdigit and b.isdigit and c.isdigit:
    if a>b and a>c:
        print("El primer numero es mayor")
    if a<b and b>c:
        print("El segundo numero es mayor")
    if c>b and c>a:
        print("El tercero numero es mayor")

if a.isdigit and b.isdigit and c.isdigit:
    if a<b and a<c:
        print("El primer numero es menor")
    if a>b and b<c:
        print("El segundo numero es menor")
    if c<b and c<a:
        print("El tercero numero es menor")