n = int(input())
lista=[0]*n

for i in range(n):
    lista[i]=int(input())

#print(lista)

for i in range(n):
    for j in range(n-1):
        if (lista[j]>lista[j+1]):
            t = lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=t
    
#print(lista)

resultado=[]

for i in lista:
    if i not in resultado:
        resultado.append(i)
        
print(resultado)