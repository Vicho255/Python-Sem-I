sum=0
for i in range(10,32,2):
    print(i)
    sum=sum+i
    if i<30:
        continue
    print("Esta es la suma de los numros obtenidos",sum)