a=input('Ingrese la palabra a verificar: \n')
lista=list(a)
aux=-1
dux=0
for i in lista:
    aux=aux+1
    dux=dux-1
    if lista[aux]==lista[dux]:
        print('Palindromo')
    elif lista[0]!=lista[-1]:
        print('No Palindromo')
        break