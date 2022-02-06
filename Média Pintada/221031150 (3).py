n = int(input())
matriz=[]
for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input()))
    matriz.append(linha)
    
s=0
c=0

for i in range(n):
    for j in range(n):
        if (j>i and (i+j) <= (n-2) or (i+j) > (n-1) and j<i):
            s+=matriz[i][j]
            c+=1
            
print('%.2f'%(s/c))
