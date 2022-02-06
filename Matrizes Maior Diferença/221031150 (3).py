n = int(input())
m = int(input())
matriz = []

for i in range(n):
    linha=[]
    for j in range(m):
        linha.append(int(input()))
    matriz.append(linha)

maior=0
c=0
for i in matriz:
    for j in i:
        if c==0:
            maior=j
            c=1
        if j>maior:
            maior=j

for i in range(n):
    for j in range(m):
        matriz[i][j]=(matriz[i][j])-maior

print(matriz)