contador=0

dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))

dividendo= dividendo - divisor

while(dividendo>=0):
    contador= contador+1
    dividendo= dividendo - divisor

print("La division es igual a:", contador)