n=int(input())

matriz =[]

for i in range(n):
    linha=[]
    for j in range(n):
        linha.append(int(input()))
    matriz.append(linha)
#print(matriz)

#elementos da diagonal principal
ele_pri=[]
for i in range(n):
    ele_pri.append(matriz[i][i])

#elementos da diagonal secundária
ele_sec=[]
for i in range(n):
    ele_sec.append(matriz[i][n-1-i])

#troca diagonal
for i in range(n):
    matriz[i][i]=ele_sec[i]
    matriz[i][n-1-i]=ele_pri[i]

#print(matriz)

#inverter 1linha

L = len(matriz[0])

for i in range(int(L/2)):
    n = (matriz[0])[i]
    (matriz[0])[i]=(matriz[0])[L - i - 1]
    (matriz[0])[L - i - 1] = n
    
#print((matriz[0]))
print(matriz)
    




