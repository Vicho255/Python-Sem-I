r1={
    "ID":14,
    "Nombre":"Los Rios",
    "Superficie":18429,
    "Habitantes":404432
}
r2={
    "ID":12,
    "Nombre":"Magallanes",
    "Superficie":1382291,
    "Habitantes":166533
}

r={
    "Los Rios":r1,
    "Magallanes":r2
}

print(r)

a=(r1["Habitantes"])/(r1["Superficie"])
#print("{:.1f}".format(a))

b=(r2["Habitantes"])/(r2["Superficie"])
#print("{:.1f}".format(b))

r1.update(Densidad="{:.1f}".format(a))
#print(r1)
r2.update(Densidad="{:.1f}".format(b))
#print(r2)

r1.update(Capital="Valdivia")
#print(r1)
r2.update(Capital="Punta Arenas")
#print(r2)

r1.update(Comunas=("Rio Bueno","La Union","Paillaco"))
#print(r1)
r2.update(Comunas=("Cabo de Hornos","Puerto Williams","Porvenir"))
#print(r2)

e=("Ranco","Valdivia")
f=("Antártica Chilena","Magallanes","Tierra delFuego","Última Esperanza")

r1.update(Provicias=e)
r2.update(Provicias=f)

print("Diccionario Actualizado\n",r)