lista_nombres=[]
def nombres():
    a=1
    while a:
        nombre=str(input('Ingrese el nombre:\n'))
        if nombre!='salir':
            lista_nombres.append(nombre)
        elif nombre=='salir':
            break
    print(lista_nombres)
    return lista_nombres
def contar(lista_nombres):
    nums=[]
    for i in lista_nombres:
        nums.append(len(i))
        print(nums)
        return nums
nombres()
contar(lista_nombres)