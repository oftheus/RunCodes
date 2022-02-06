n_candidatos = int(input())
matriculas=[]
notas=[]

for i in range(n_candidatos):
    x=int(input())
    matriculas.append(x)
    
for i in range(n_candidatos):
    g=float(input())
    notas.append(g)
    
final=[]
final.append(notas)
final.append(matriculas)

#print(final)

fim=[]

for i in range(n_candidatos):
    linha=[]
    linha.append(notas[i])
    linha.append(matriculas[i])
    fim.append(linha)
    
#print(fim)

#ordenar

for i in range(n_candidatos):
    for j in range(n_candidatos-1):
        if (fim[j]>fim[j+1]):
            t = fim[j]
            fim[j] = fim[j+1]
            fim[j+1] = t
            
#print(fim)

vetor=[]
for i in range(n_candidatos):
    vetor.append(fim[i][1])
    
print(vetor)
    








    