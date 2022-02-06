n = int(input())

#achar matriz a
matrizA = []
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input()))
    matrizA.append(linha)

#achar matriz b
B=[]
for i in range(n):
    B.append([0]*n)
    
for i in range(n):
    for j in range(n):
        pe=0
        for k in range(n):
            pe=pe+matrizA[i][k]*matrizA[k][j]
        B[i][j]=pe
matrizB=[]        
for i in range(n):
    matrizB.append(B[i])

#achar transposta de a
at=[] #transposta de a
rez=[[matrizA[j][i] for j in range(n)] for i in range(n)]
for r in rez:
    at.append(r)   

#criar matriz com 0
real=[] #matriz com 0's

for i in range(n):
    l=[]
    for j in range(n):
        l.append(0)
    real.append(l)

#achar matriz c
for i in range(n):
    for j in range(n):
        real[i][j]=at[i][j]+ matrizB[i][j]

c=[]
for q in real:
    c.append(q)
    
print(c)