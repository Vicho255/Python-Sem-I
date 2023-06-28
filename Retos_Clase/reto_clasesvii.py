def logitud(frase):
    dic_palabras={}
    palabras=frase.split()
    for pal in palabras:
        dic_palabras[pal]=len(pal)
    return dic_palabras
    
frase=input("Ingrese la frase:\n")
print(logitud(frase))