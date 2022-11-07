sum=0
for i in range(6,62,5):
    sum= sum+i
    if(sum==402):
        print("Posicion 12: 61")
        print("Suma: 402")

assert(sum==402 and i==61)
print("Prueba Lograda")