Ci = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
Cal= [134, 99, 245, 50]

min=Cal.index(min(Cal))
print({Ci[min]},{Cal[min]})

max=Cal.index(max(Cal))
print({Ci[max]},{Cal[max]})

for i in range(len(Ci)):
    if Cal[i] >= 0 and Cal[i] <= 50:
        print(Ci[i],", Bueno")
    elif Cal[i] >= 51 and Cal[i] <=100:
        print(Ci[i],", Moderado")
    elif Cal[i] >= 101 and Cal[i] <=150:
        print(Ci[i],", Dañina para grupos de saluda sensible")
    elif Cal[i] >= 151 and Cal[i] <=200:
        print(Ci[i],", Dañina a la Salud")
    elif Cal[i] >= 201 and Cal[i] <=300:
        print(Ci[i],", Muy dañina a la Sañud")
    else:
        print(Ci[i],", Peligrosa")