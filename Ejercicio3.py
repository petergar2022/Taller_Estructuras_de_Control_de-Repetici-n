sum=0 
for i in range(97,1004,1):
    if(i%2==0):
        sum= sum+i

assert(sum==249150)
print("Prueba superada!")