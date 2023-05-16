print("Ingresar nombre del primer paciente")
np1=input()
while np1.isdigit():
    print("Ingrese un nombre valido")
    np1=input()
    
print("Ingresar peso en Kg del primer paciente")
pp1=input()
while float(pp1) <= 0:
    print("Ingresar datos validos")
    pp1=input()
print("Peso Valido")

print("Ingresar la estatura en metros del primer paciente")
esp1=input()
while float(esp1) <= 0 or float(esp1)>3:
    print("Ingresar datos validos")
    esp11=input()
print("Estatura Valida")

print("Ingresar la edad del primer paciente")
ep1=input()
while not ep1.isdigit() or int(ep1) <= 0 or int(ep1)>120:
    print("Ingresar datos validos")
    ep1=input()
print("Edad Valida")

p1=(np1,pp1,esp1,ep1)

#print(p1)

print("Ingresar nombre del segundo paciente")
np2=input()
while np2.isdigit():
    print("Ingrese un nombre valido")
    np2=input()
    
print("Ingresar peso en Kg del segundo paciente")
pp2=input()
while float(pp2) <= 0:
    print("Ingresar datos validos")
    pp2=input()
print("Peso Valido")

print("Ingresar la estatura en metros del primer paciente")
esp2=input()
while float(esp2) <= 0 or float(esp2)>3:
    print("Ingresar datos validos")
    esp12=input()
print("Estatura Valida")

print("Ingresar la edad del primer paciente")
ep2=input()
while not ep2.isdigit() or int(ep2) <= 0 or int(ep2)>120:
    print("Ingresar datos validos")
    ep2=input()
print("Edad Valida")

p2=(np2,pp2,esp2,ep2)

#print(p2)

print("Ingresar nombre del tercer paciente")
np3=input()
while np3.isdigit():
    print("Ingrese un nombre valido")
    np3=input()
    
print("Ingresar peso en Kg del tercer paciente")
pp3=input()
while float(pp3) <= 0:
    print("Ingresar datos validos")
    pp3=input()
print("Peso Valido")

print("Ingresar la estatura en metros del tercer paciente")
esp3=input()
while float(esp3) <= 0 or float(esp3)>3:
    print("Ingresar datos validos")
    esp13=input()
print("Estatura Valida")

print("Ingresar la edad del tercer paciente")
ep3=input()
while not ep3.isdigit() or int(ep3) <= 0 or int(ep3)>120:
    print("Ingresar datos validos")
    ep3=input()
print("Edad Valida")

p3=(np3,pp3,esp3,ep3)

#print(p3)

print(p1,p2,p3)