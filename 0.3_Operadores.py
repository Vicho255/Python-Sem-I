a=42
b=75
c=8
d=55

#Operaciones Comunes

t=76.3
g=9.81

v=g*t
print(v)
print("{:.2f}".format(v))

print("Hola"*5)

#print("Hola"*(3.5*2))

print("Hola"*(int((10*2)/5)), "\n")

#Solo es posible multiplicar una cadena de texto por un entero(int), es imposible con un flotante(float)

print("Hola"+ str(20))

#Operadores de comparacion

print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(c<=d)
print(c>=d)

if (a!=b):
    print("Loco")
else:
    print("No Loco")  
    
#sienpre antes de una comparacion entre cadenas de texto usar la funcion len

#Operadores logicos
bencina = True
encendido = True
edad = 18

#AND
if bencina and encendido:
    print("El veiculo puede arrancar")
else:
    print("El veiculo no puede arrancar")

#OR
if bencina or encendido:
    print("El veiculo puede arrancar")
else:
    print("El veiculo no puede arrancar")

#NOT + AND
if not bencina and encendido:
    print("El veiculo puede arrancar")
else:
    print("El veiculo no puede arrancar")

#NOT + OR 
if not bencina or encendido:
    print("El veiculo puede arrancar")
else:
    print("EL vaiculo no puede arrancar")

#NOT + OR +AND
if not bencina or (encendido and edad >= 18):
    print("El veiculo puede arrancar")
else:
    print("El veiculo no puede arrancar")