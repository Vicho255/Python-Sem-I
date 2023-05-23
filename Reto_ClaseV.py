num=int(input("Ingrese el numero \n"))

if num % 2== 0:
    print("El Numero es par")
else:
    print("El Numero es inpar")

###Sacado de ChatGPT###
def primo(num):
    if num<=1:
        return False
    for i in range(2, int((num**0.5)+1)):
        if num % i == 0:
            return False
    return True

if primo(num):
    print("Primo")
else:
    print("No primo") 

if num<50:
    print("El Numero es menor que 50")
else:
    print("El numero es mayor que 50")