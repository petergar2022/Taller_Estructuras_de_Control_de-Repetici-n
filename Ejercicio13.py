numEst= int(input("Ingrese el total de estudiantes a encuestar: "))
nombreAlt= ""
nombreBaj= ""
puntajMax= 0
puntajMin= 1000000000
promPuntaj= 0
sumpuntaj=0
porcInfer= 0
porcSuper= 0
lista=[]
for i in range(numEst):
    nombrest= input("Ingrese el nombre del estudiante: ")
    notaest= float(input("Ingrese la nota del estudiante: "))
    if(notaest>puntajMax):
        nombreAlt= nombrest
        puntajMax= notaest
    if(notaest<puntajMin):
        nombreBaj= nombrest
        puntajMin= notaest
    sumpuntaj= notaest + sumpuntaj
    lista.append(notaest)

promPuntaj= sumpuntaj/numEst
for k in range(numEst):
    if(lista[k]<promPuntaj):
        porcInfer= porcInfer+1
    if(lista[k]>promPuntaj):
        porcSuper= porcSuper+1

porcSuper= (porcSuper*100)/numEst
porcInfer= (porcInfer*100)/numEst

print("\nEl estudiante con mayor nota es:",nombreAlt)
print("El estudiante con menor nota es:",nombreBaj)
print("El puntaje mayor es:",puntajMax)
print("El puntaje menor es:",puntajMin)
print("El promedio de puntaje es de:",promPuntaj)
print("El porcentaje superior al promedio de puntaje es de:",round(porcInfer,2),"%")
print("El porcentaje inferior al promedio de puntaje es de:",round(porcInfer,2),"%")