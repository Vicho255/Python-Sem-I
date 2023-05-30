###Definir una Funcion simple###

def fun():
    print("Esta es una funcion!!")

###Declarando una funcion y utilizando una lista###

def concatenar(lista1,lista2):
    return lista1 + lista2;

lista1=[1,2,3]
lista2=[4,5,6]

print(concatenar(lista1,lista2))

###Declaracion de una funcion de multiplicacion###

def multi(num1,num2):
    return num1*num2

print(multi(5,5))

###Funcion Suma y Resta Por teclado###

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

resultado=suma(a,b)
print("El resultado es de",resultado)

resultado=resta(a,b)
print("El resultado es de",resultado)