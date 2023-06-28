print("Ingrese las Asignatura")
asignatura = input()

print("Ingrese el Nombre del Estudiante")
estudiante = input()

print("Ingrese las notas de los laboratorios 1 y 2 en orden")
l1 = input()
l2 = input()

pro = ((float(l1)*0.3)+(float(l2)*0.7))

pro_Est = {
    "Asignatura": asignatura,
    "Estudiante": estudiante,
    "Lavoratorio 1": l1,
    "Lavoratorio 2": l2,
    "Promedio": ("{:.1f}".format(pro))
}

print(pro_Est)