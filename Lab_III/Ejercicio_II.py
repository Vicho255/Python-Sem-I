a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]
f = [4,5,6]
#Concatenar todas las listas e imprimir la lista obtenida#
d=a+b+c
print(d)
#Agregar el número 20 en la penúltima posición de la lista#
d.insert(-1,20)
print(d)
#Ordenar la lista de forma descendente#
d.sort(reverse=1)
print(d)
#Insertar la lista [4,5,6] en la última posición de la lista ordenada#
d.append(f)
print(d)
d.pop()
#print(d)
#Sumar todos los números dentro de la lista#
g=(sum(d))+(sum(f))
print(g)
#Obtener el promedio simple de la lista#
h=g/(len(d)+len(f))
print(h)