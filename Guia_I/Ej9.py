"""Se tiene la siguiente lista de enteros:
numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]
Se solicita:
a) Eliminar el ultimo elemento de la lista
b) Agregar en la primera posicion el numero 2
c) Eliminar los numeros duplicados de la lista
d) Obtener la media y la mediana de la lista"""

a=[4, 3, 8, 12, 6, 10, 14, 3, 6]

a.pop(-1)
#print(a)
a.insert(0,2)
#print(a)
b=set(a)
#print(b)
a=list(b)
#print(a)
c=(a[0]+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7])/2
#print(c)
d=(a[3]+a[4])/2
#print(d)
lista_numeros={
    "Lista":a,
    "Media Aritmetica":c,
    "Mediana":d
}

print(lista_numeros)