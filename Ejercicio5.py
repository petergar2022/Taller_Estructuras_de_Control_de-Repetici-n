suma= 0
for k in range(1,1001,1):
    operacion=(k**2+1)/k
    if(operacion<=1000):
        suma= suma+operacion
    if(suma>1000):
        break
print("El numero de iteraciones maximas cercanas a 1000 es de:",k)