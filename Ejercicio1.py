n= int(input("Ingresa el numero N: "))
k= int(input("Ingresa el numero K: "))

for i in range(k):
    j=1
    if(n>k):
        n= n-j
        j= j+1
    elif(n==k):
        print("El valor de K es:",n,"y el valor de N es:",k)
        break
    else:
        print("El valor de K debe ser menor al de N")