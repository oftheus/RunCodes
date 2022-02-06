n = int(input())
m = int(input())
matriz = []

for i in range(n):
    linha=[]
    for j in range(m):
        linha.append(int(input()))
    matriz.append(linha)
    
matriz_modificada = []
for i in range(n): 
  l = []
  for j in range(m):
    l.append(0)
  matriz_modificada.append(l)    

#maior n° na matriz
maior=0
c=0
for i in matriz:
    for j in i:
        if c==0:
            maior=j
            c=1
        if j>maior:
            maior=j

#menores ns° das colunas
for j in range(m):
    menor_em_modulo=maior
    for i in range(n):
        if abs(matriz[i][j])<=menor_em_modulo:
            menor_em_modulo=abs(matriz[i][j])
    #print(menor_em_modulo)
    
    for i in range(n):
        matriz_modificada[i][j] = ( matriz[i][j]+menor_em_modulo)

final=[]
for i in range(n):
    final.append(matriz_modificada[i])
print(final)
