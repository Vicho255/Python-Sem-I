tem_min={9, 5, 2, 7, 6, 1}
tem_max= {12, 14, 11, 10, 15, 9}
### Verificar si la temperatura 9°C está en ambos sets ###
a=bool(tem_max.intersection(tem_min))
if a:
    print('Si se encuentra')
else:
    print('No se encuentra')
### Comprobar si al menos la temperatura 6°C y 17°C está en alguno de los sets ###
for i in tem_max:
    if i==6:
        print('6° encontrado en Temperaturas maximas')
    elif i==17:
        print('17° encontrado en Temperaturas maximas')
for i in tem_min:
    if i==6:
        print('6° encontrado en Temperaturas minimas')
    elif i==17:
        print('17° encontrado en Temperaturas minimas')
### Elevar a 4 todas las temperaturas dentro de los sets ###
tmp_min=set()
for i in tem_min:
    a=i**4
    tmp_min.add(a)
print(tmp_min)
tmp_max=set()
for i in tem_max:
    a=i**4
    tmp_max.add(a)
print(tmp_max)
### Unir ambos sets en uno solo ###
temps=set(tmp_max.union(tmp_min))
print(temps)