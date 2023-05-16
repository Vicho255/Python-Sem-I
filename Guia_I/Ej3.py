"""Desarrollar un programa que al momento de ingresar los lados de un triangulo
(a, b y c) en consola, indique si es equilatero, isosceles o escaleno. Tambien se
solicita calcular el area utilizando la formula de Heron:"""

print("Ingrese los lados del triangulo")

a=float(input("Lado 1: "))
b=float(input("Lado 2: "))
c=float(input("Lado 3: "))


if a==b and b==c:
    print("Es un triangulo Equilatero")
elif a!=b and b!=c:
    print("Es un triangulo Escaleno")
elif (a!=b or a!=c) and (a==b or a==c):
    print("Es un triangulo Isosceles")

per=a+b+c
print(per)
sep=per/2

Area=(sep*(sep-a)*(sep-b)*(sep-c))**(1/2)

print("De Area: {:.2f}".format(Area))