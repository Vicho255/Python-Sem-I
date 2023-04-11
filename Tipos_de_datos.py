#01. Datos de tipo Numerico
estatura = 1.70
peso = 87
complejo = 1 + 4j

print("Imprecion del numero complejo", complejo)

#Transformacion de datos real a estero
print(int(peso))
print(float(estatura))

#Operacion aritmetica
imc = peso/estatura**2
print("Mi IMC es de:", imc, "\n")

print("Mi IMC es de: {:.2f}".format(imc))

#02. Datos de tipo cadena de caracteres
asisgnatura = "Programacion"
carrera = "Ingieneria Civil Informatica"
print("la aisgnatura", asisgnatura, "corresponde a la carrear", carrera)
#funcion len, cuenta la cantidad de caracteres y la cantidad de elementos dentro de una lista
print(len(carrera))

#03. Datos de tipo booleanos
ampolleta = False
interruptor = True

#Con type podemos saver que tipo de dato estamos tratando
print(type(ampolleta))

#04. Datos de tipo Array (Objetos de tipo coleccion)
estudiantes = ["Matias", "Carlos", "Miguel", "Cristobal", "Carlos"]
num = [1, 2, 3, 4, 5, 6]
lenguaje = ["Python"]
print(estudiantes)
print(num)
print(lenguaje)
#Listas de Python
#arreglo (array = [0, 1, 2, 3])/ lista (array1 = [0, "loco", true, 2])
nueva_lista = list()
print("Esta es una nueva lista", nueva_lista)

otra_lista = []
print("Esta es una nueva lista", otra_lista)
print(type(otra_lista))

lista_compuesta = [2, "looco", ampolleta, 283*832]
print(lista_compuesta)

#lista_listas = [estudiantes, num, lenguaje, nueva_lista, otra_lista, lista_compuesta]
#print(lista_listas)
#print(len(lista_compuesta))

#Count(), cuenta la cantidad de veses que se repite un elemto dentro de una lista 
print(estudiantes.count("Carlos"))