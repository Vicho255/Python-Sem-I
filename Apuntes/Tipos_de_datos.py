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

print(estudiantes[0])
print(estudiantes[1])
print(estudiantes[2])
print(estudiantes[-2])
print(estudiantes[-5])

#Mutabilida de Listas
estudiantes[1] = "Gabriela"
print(estudiantes)

data_asig = [10023, "Programacion", 1, True]
cod,ramo,semestre,estado = data_asig

print(estudiantes + num)
print(list("Python"))
print(list(range(10)))
print("\n")

#Tuplas (No Mutables)
g1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print(type(g1))
print(g1)
print(g1[0])
print(g1.count("Daniel"))
print(g1.index("Daniel"))

#g1[0] = "Constansa"
#print(g1)

print(g1[2:5])

#Para modificar una Tupla hay que transformala a una lista

g1 = list(g1)
print(type(g1))

#SETS (Estructura fija de datos)
conjunto_vacio = set({})
conjunto_vacio1 = {}
conjunto_colores = set({"Azul","Rojo","Verde","Amarillo"})
conjunto_animales = {"Perro","Loro","Gato"}

print(type(conjunto_vacio))
print(type(conjunto_vacio1))

#print(conjunto_animales[0])
#conjunto_animales = list(conjunto_animales)
#print(conjunto_animales[0])

conjunto_colores.add("Gris")

print(conjunto_colores)
#Dicionarios
datos_personales = {
    "Nombre":"Vicente",
    "Institucion":"Ulagos",
    "Edad":18,
    "Asignaturas":{"Estructura da Datos","Programacion"}
    }
print(datos_personales)

print(len(datos_personales))

print(datos_personales["Nombre"])

datos_personales["Edad"]="19"
print(datos_personales)

datos_personales["Ciudad"]="Osorno"
print(datos_personales)

del datos_personales["Ciudad"]
print(datos_personales)
