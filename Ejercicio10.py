n= int(input("Ingrese el numero de estudiantes: "))
alt2=0
for i in range(n):
    alt1= float(input("Ingrese la estatura del estudiante: "))
    if(alt1>alt2):
        altMax= alt1
    alt2= alt1
print("La altura maxima es:",altMax)