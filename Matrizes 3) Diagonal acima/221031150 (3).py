n = int(input())
matriz = []

for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input()))
    matriz.append(linha)
    
ele_pri=[]
for i in range(n):
    ele_pri.append(matriz[i][i])
    
acima=0
soma=0

for i in range(n):
    for j in range(n):
        if j>i:
            acima+=matriz[i][j]
        soma+=matriz[i][j]

print(acima)

#media

media=soma/(n*n)
abaixo=0
for i in range(n):
    for j in range(n):
        if matriz[i][j]<media:
            abaixo+=1
            
print(abaixo)