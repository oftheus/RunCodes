n = int(input())
m = int(input())

matriz = []
for i in range(n):
    linha=[]
    for j in range(m):
        linha.append(int(input()))
    matriz.append(linha)
#print(matriz)    

#lista temporária
tam = (n*m)
V   = [0]*(tam)    

ind=0
for i in range(n):
    for j in range(m):
        V[ind]=matriz[i][j]
        ind   =ind+1
        
#ordernar vetor temporário
for i in range(tam):
    for j in range(tam-1):
        if (V[j]<V[j+1]):
            t      = V[j]
            V[j]   = V[j+1]
            V[j+1] = t

#print(V)

real=[] #matriz com 0's
for i in range(n):
    l=[]
    for j in range(m):
        l.append(0)
    real.append(l)
    
ind=0
for i in range(m):
    for c in range(n):
        real[c][i]=V[ind]
        ind+=1
        
print(real)