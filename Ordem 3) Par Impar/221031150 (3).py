n =int(input())
listapar=[]
listaimpar=[]
listafim=[]

for i in range(n):
    x=int(input())
    if (x%2==0):
        listapar.append(x)
    else:
        listaimpar.append(x)
        
#print(listapar)
h=len(listapar)

#ordenar lista par crescente
for i in range(h):
    for j in range(h-1):
        if listapar[j]>listapar[j+1]:
            t=listapar[j]
            listapar[j]=listapar[j+1]
            listapar[j+1]=t

#print(listapar)
            
#ordenar lista impar

#print(listaimpar)
v=len(listaimpar)

for i in range(v):
    for j in range(v-1):
        if listaimpar[j]<listaimpar[j+1]:
            t=listaimpar[j]
            listaimpar[j]=listaimpar[j+1]
            listaimpar[j+1]=t
            
#print(listaimpar)

listafim=listapar+listaimpar
print(listafim)
