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
    
