a=int(input('¿Cuantos numeros va a ingresar?\n'))
print('--------------------')
lista_pares=[]
lista_impares=[]

for i in range(a):
    b=int(input(f'Ingrese el {i+1}° numero: '))
    if b%2==0:
        lista_pares.append(b)
    elif b%2!=0:
        lista_impares.append(b)

print(lista_impares+lista_pares)

def suma_total(lista_pares,lista_impares):
    a=sum(lista_pares)+sum(lista_impares)
    print('la suma de todos los numeros ingredados es de: ',a)
    return a

def suma_par(lista_pares):
    a=sum(lista_pares)
    print('La suma de los numeros pares ingresados es de: ',a)
    return a

def suma_impar(lista_impares):
    a=sum(lista_impares)
    print('La suma de los numeros impares ingresados es de: ',a)
    return a

suma_total(lista_impares,lista_pares)
suma_par(lista_pares)
suma_impar(lista_impares)